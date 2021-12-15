import cv2
import mediapipe as mp
import time
import handtracking as ht
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.optim import SGD
import matplotlib.pyplot as plt
from ann import ArtificialNeuralNetwork


def dist_points(x1, x2, y1, y2):
    # Find the distance between two points
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)


def point_inside(x, y, x_center, y_center, radius):
    # Return the distance between two points
    if ((x - x_center) ** 2 + (y - y_center) ** 2) < radius ** 2:
        return True
    else:
        return False


def countdown(input_t):
    # FUNCTION USED TO COUNT DOWN THE TIME TO START RECORDING
    # time in seconds
    s_contdown = time.time() 
    t = 0
    while t >= 0:
        sucess, img = cap.read()    # save image that the webcam records
        img = cv2.flip(img,1)

        t = input_t - int(time.time() - s_contdown) 
        msg = str(t)
        cv2.putText(img, msg, (300, 240), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

        cv2.imshow("Image", img) # Display img
        cv2.waitKey(1)  # keep displaying img


def tip_mcp_distance(lm_list):
    # FUNCTION TO RECORD THE DISTANCE FROM EACH FINGER TO ITS MCP
    if len(lm_list) != 0:
        thumb = dist_points(lm_list[4][1], lm_list[1][1], lm_list[4][2], lm_list[1][2])
        index = dist_points(lm_list[8][1], lm_list[5][1], lm_list[8][2], lm_list[5][2])
        middle = dist_points(lm_list[12][1], lm_list[9][1], lm_list[12][2], lm_list[9][2])
        ring = dist_points(lm_list[16][1], lm_list[13][1], lm_list[16][2], lm_list[13][2])
        pinky = dist_points(lm_list[20][1], lm_list[17][1], lm_list[20][2], lm_list[17][2])
        distance_list = np.array([thumb, index, middle, ring, pinky])
        return distance_list


def finger_tip_distance(lm_list):
    # FUNCTION TO RECORD THE DISTANCE FROM ONE FINGER TIP TO THE OTHERS FINGER TIPS
    distance_list = []
    if len(lm_list) != 0:
        for i in range(1, 5):
            for j in range(1+i, 6):
                ft1 = 5*i - 1*i
                ft2 = 5*j - 1*j
                x = dist_points(lm_list[ft1][1], lm_list[ft2][1], lm_list[ft1][2], lm_list[ft2][2])
                distance_list.append(x)
        return np.array(distance_list)

def normalization(x):
    # NORMALIZATION FUNCTION
    x_max = max(x)
    x_min = min(x)
    return (x - x_min) / (x_max - x_min)

cap = cv2.VideoCapture(0)   # capture video in the webcam
detector = ht.handDetector(max_hands=1) # Start hand detector (if max_hands not specified max_hands=2)

no_gesture = int(input("How many gestures you want to train? "))

gesture_label = []
for i in range(no_gesture):
    gesture_label.append(input(f"Put the label of the gesture {i+1}: "))

#########################################################################################
dataset_tip_mcp = np.array(["thumb", "index", "middle", "ring", "pinky"]) # label for tip-mcp
dataset_tip_distance = np.array(["t_i", "t_m", "t_r", "t_p", "i_m", "i_r", "i_p", "m_r", "m_p", "r_p"]) # label for tip-tip
dataset = np.hstack([dataset_tip_distance, np.array(["label"])])# select dataset label
epocs = 2000

p_time = 0  # start previous time = 0
for i in range(no_gesture):

    ready = False
    
    while ready == False:
        sucess, img = cap.read()    # save image that the webcam records
        img = cv2.flip(img,1)   # mirror the img for better user interaction exp (the user see the img as in a mirror)

        img = detector.find_hands(img, False)  # find and draw Hands landmarks in the img
        lm_list = detector.find_positions(img)  # calculate the landmark positions in pixel

        msg = "Put the tip of the index finger on the red circle to start"
        cv2.putText(img, msg, (50, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

        r_circle = 20
        x_circle = 320
        y_circle = 240
        c_center = (x_circle, y_circle)
        circle = cv2.circle(img, c_center, r_circle, (0, 0, 255), thickness=-1)
            
        cv2.imshow("Image", img) # Display img
        cv2.waitKey(1)  # keep displaying img

        # CHECK IF THE FINGER IS INSIDE THE CIRCLE RADIUS
        # if finger inside the circle radius start countdown to record
        if (len(lm_list) != 0) and (point_inside(lm_list[8][1], lm_list[8][2], x_circle, y_circle, r_circle)):
            circle = cv2.circle(img, c_center, r_circle, (0, 255, 0), thickness=-1)
            ready = True
            
            countdown(3)






    r_time = 0  # running time
    s_time = time.time()    # starting time
    pre_time = 0  # start previous time = 0

    t = 0
    while t <= 5:
        sucess, img = cap.read()    # save image that the webcam records
        img = cv2.flip(img,1)   # mirror the img for better user interaction exp (the user see the img as in a mirror)

        img = detector.find_hands(img, False)  # find and draw Hands landmarks in the img
        lm_list = detector.find_positions(img)  # calculate the landmark positions in pixel

        # CALCULATE AND DISPLAY FPS
        cur_time = time.time()
        fps = 1/(cur_time-pre_time)
        pre_time = cur_time
        cv2.putText(img, "FPS: " + str(int(fps)), (500, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
        # END

        t = cur_time - s_time

        cv2.putText(img, "RECORDING...", (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

        ###################################################################################
        data = finger_tip_distance(lm_list)

        # SAVE DATA JUST IF IT IS NOT NONE TYPE
        if data is None:
            pass
        elif (data.any() != None):
            data = np.hstack([data, gesture_label[i]])  # add the label column to the row of values
            dataset = np.vstack([dataset, data])    # stack values in one single dataset


        cv2.imshow("Image", img) # Display img
        cv2.waitKey(1)  # keep displaying img


df = pd.DataFrame(dataset[1:, :], columns=dataset[0, :]).to_csv("hand_data.csv", index=False) # save data as .csv file
X = dataset[1:, :-1].astype(float) # remove string column with the name of the variable

# NORMALIZE THE INPUT VALUES
# for i in range(len(X[0])):
#     X[i] = normalization(X[i])

label = dataset[1:, -1] # colect label column in the dataset
Y = np.zeros([len(label), len(gesture_label)]) # create n x m zero matrix to save as true the column related to the correct value and false otherwise
for i in range(len(label)):
    j = gesture_label.index(label[i]) # locate the column related to the correct label value
    Y[i][j] = 1

device = 'cuda' if torch.cuda.is_available() else 'cpu' # use GPU if available
input_layer = torch.from_numpy(X).float().to(device)    # set the input data as the correct format
output_layer = torch.from_numpy(Y).float().to(device)   # set the output data as the correct format

print(len(gesture_label))
ann = ArtificialNeuralNetwork(len(X[0]), len(Y[0])).to(device) # start ann
loss_func = nn.MSELoss()    # select loss function
opt = SGD(ann.parameters(), lr=0.001)   #select optm function
loss_history = []   # empty list to store loss value

# Start training during n epocs
for _ in range(epocs):
    opt.zero_grad()
    y_pred = ann(input_layer)
    loss_value = loss_func(y_pred, output_layer)
    loss_value.backward()
    opt.step()
    loss_history.append(loss_value)

# PLOT LOSS HISTORY
plt.plot(loss_history)
plt.show()

while True:
    sucess, img = cap.read()    # save image that the webcam records
    img = cv2.flip(img,1)   # mirror the img for better user interaction exp (the user see the img as in a mirror)

    img = detector.find_hands(img, False)  # find and draw Hands landmarks in the img
    lm_list = detector.find_positions(img)  # calculate the landmark positions in pixel

    # CALCULATE AND DISPLAY FPS
    cur_time = time.time()
    fps = 1/(cur_time-pre_time)
    pre_time = cur_time
    cv2.putText(img, "FPS: " + str(int(fps)), (500, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
    # END

    # IF RECORDING LM VALUES PASS THROUGH THE TRAINED NN AND PREDICT THE GESTURE
    if (len(lm_list) != 0):
        ###################################################################################
        data = finger_tip_distance(lm_list)
        data = torch.from_numpy(data).float().to(device)
        predict = ann(data).cpu().detach().numpy()
        val = max(predict)
        print(predict)
        
        # SHOW JUST IF THE PROBABILITY OF THE GESTURE IS HIGHER THAN THE DESIRED VALUE
        # if val >= 0.5:
        msg = gesture_label[predict.argmax()]
        cv2.putText(img, msg, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
    
    cv2.imshow("Image", img) # Display img
    cv2.waitKey(1)  # keep displaying img