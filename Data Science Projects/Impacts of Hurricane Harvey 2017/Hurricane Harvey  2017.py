import pandas as pd
import matplotlib.pyplot as plt
from math import isnan
from mpl_toolkits.basemap import Basemap
import numpy as np

# Importing data
df = pd.read_csv("StormEvents_2017.csv")

# Dataframe preview
print(df.head())
print(df.shape, "\n")

# Check if all variables has the correct data type
print(df.dtypes)
print('''The time has data type "object" while it should be "datetime".
Several values should be categorical, as "State, "Month", "Event_Type", etc.  \n''')

# Correcting data type
df["Begin_Date_Time"] = pd.to_datetime(df["Begin_Date_Time"], errors="ignore")
df["End_Date_Time"] = pd.to_datetime(df["End_Date_Time"], errors="ignore")
df["State"] = pd.Categorical(df["State"])
df["Month"] = pd.Categorical(df["Month"])
df["Event_Type"] = pd.Categorical(df["Event_Type"])
df["CZ_Name"] = pd.Categorical(df['CZ_Name'])
df['Timezone'] = pd.Categorical(df['Timezone'])
print(df.dtypes)
print(df.head(), "\n")

# Reorder month category
month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
df["Month"].cat.reorder_categories(month_order)

# Select just the data that is relevant (from August 17th to September 3th)
harley_df = df[(df["Begin_Date_Time"] >= '2017-08-17 00:00:00') & (df["Begin_Date_Time"] < '2017-09-04 00:00:00')].copy() 
print(harley_df.head())
print(harley_df.shape, "\n")

# Check for missing values
print(harley_df.isnull().sum(), "\n")

# Raplace NaN costs and damage for 0
harley_df['Damage_Property'].fillna(0, inplace=True)
harley_df['Property_Cost'].fillna(0, inplace=True)
harley_df['Damage_Crops'].fillna(0, inplace=True)
harley_df['Crop_Cost'].fillna(0, inplace=True)
print(harley_df.isnull().sum(), "\n")

# Find States that suffered at most with the related storm events
most_impacted_states = harley_df.groupby("State")["Property_Cost"].sum().sort_values(ascending=False)
print(most_impacted_states.head())
print(f"""Texas represents {most_impacted_states[0]/most_impacted_states.sum() * 100:.2f} percent of the total costs.
Therefore, is recomend the insurance company to send people to Texas. \n""")

# Ocurrance of Events in Texas
texas_df = harley_df[harley_df["State"] == "TEXAS"].copy()
texas_df.reset_index(inplace=True)
print(texas_df.head())
print(texas_df.shape, "\n")
plt.hist(texas_df["Event_Type"])
plt.xlabel("Event_Type")
plt.ylabel("Ocurrance")
plt.title("Ocurrance of events in Texas")
plt.xticks(rotation=45)
plt.show()

print("""As shown in the bar plot above, flash flood was the weather event that most occured in the states of Texas 
from August 17th and September 3rd.
Flash floods occour along rivers, on coastlines, in urban areas and dry creek beds. To support the
informations collected with the bar diagram, the location of those events will evaluated. \n""")

# Location of events
print(texas_df[["Begin_Lat", "Begin_Lon"]].isnull().sum())
print("""More than 20 percent of the begin latitude and longitude data is missing,
therefore this data cannot be deleted.
The latitude and longitude missing will be replaced by the median latitude and longitude of the County
related to the weather event. In case there is no latitude or longitude registered for the County
it will be replaced by the median latitude and longitude from Texas""")
for index, row in texas_df.iterrows():
    if isnan(texas_df[texas_df["CZ_Name"] == texas_df.at[index, "CZ_Name"]]["Begin_Lat"].median()) == False:
        texas_df.at[index, 'Begin_Lat'] = texas_df[texas_df["CZ_Name"] == texas_df.at[index, "CZ_Name"]]["Begin_Lat"].median()
        texas_df.at[index, 'Begin_Lon'] = texas_df[texas_df["CZ_Name"] == texas_df.at[index, "CZ_Name"]]["Begin_Lon"].median()
    else:
        texas_df.at[index, 'Begin_Lat'] = texas_df["Begin_Lat"].median()
        texas_df.at[index, 'Begin_Lon'] = texas_df["Begin_Lon"].median()
print(texas_df[["Begin_Lat", "Begin_Lon"]].isnull().sum())

# Geoplot
my_map = Basemap(projection='merc',
            resolution = 'l', area_thresh = 1000.0,
            llcrnrlon=texas_df["Begin_Lon"].min() - 1, llcrnrlat=texas_df["Begin_Lat"].min() - 1, #min longitude (llcrnrlon) and latitude (llcrnrlat)
            urcrnrlon=texas_df["Begin_Lon"].max() + 1, urcrnrlat=texas_df["Begin_Lat"].max() + 1) #max longitude (urcrnrlon) and latitude (urcrnrlat)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'white', alpha = 0.3)
my_map.shadedrelief()       
my_map.etopo()
xs,ys = my_map(np.asarray(texas_df.Begin_Lon), np.asarray(texas_df.Begin_Lat))
texas_df['xm'] = xs.tolist()
texas_df['ym'] = ys.tolist()
for index,row in texas_df.iterrows():
    x,y = my_map(texas_df.Begin_Lon, texas_df.Begin_Lat)
    my_map.plot(row.xm, row.ym,markerfacecolor =([1,0,0]),  marker='o', markersize= 5, alpha = 0.75)
plt.title('Weather events distribution')
plt.show()
print('''\nAs expected, the geographical diagram support the information collected with the bar diagram. The majority of
the events occured at the costside or close to a montain area (near rivers).\n''')

# Counties with the most weather event ocurrancy
most_event_ocurrancy = texas_df.groupby(["Event_Type", "CZ_Name"]).size()
most_event_ocurrancy = most_event_ocurrancy.to_frame(name = 'size').reset_index()
most_event_ocurrancy = most_event_ocurrancy.groupby("CZ_Name")["size"].sum().sort_values(ascending=False)
print(most_event_ocurrancy.head(), "\n")

# Counties with highest property cost
high_property_cost = texas_df.groupby("CZ_Name")["Property_Cost"].sum().sort_values(ascending=False)
print(high_property_cost.head(), "\n")
print(f"""The 5 counties with the highest property cost represents {high_property_cost.head().sum()/high_property_cost.sum()*100:.2f} percent
of the total property cost.
Due to the proximity of the counties the best decision that the company can do is to focus on sending employers for the 
region covering already more than 80 percent of the total property cost in the whole United States 
in a small region of the country""")
hpc_counties = texas_df[(texas_df["CZ_Name"]=="GALVESTON") | (texas_df["CZ_Name"]=="FORT BEND") | 
    (texas_df["CZ_Name"]=="MONTGOMERY") | (texas_df["CZ_Name"]=="HARRIS") | (texas_df["CZ_Name"]=="JEFFERSON")].copy()

# Geoplot all waether events due to the Harley Hurricane
my_map = Basemap(projection='merc',
            resolution = 'l', area_thresh = 1000.0,
            llcrnrlon=harley_df["Begin_Lon"].min() - 1, llcrnrlat=harley_df["Begin_Lat"].min() - 1, #min longitude (llcrnrlon) and latitude (llcrnrlat)
            urcrnrlon=harley_df["Begin_Lon"].max() + 1, urcrnrlat=harley_df["Begin_Lat"].max() + 1) #max longitude (urcrnrlon) and latitude (urcrnrlat)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'white', alpha = 0.3)
my_map.shadedrelief()       
my_map.bluemarble()
xs,ys = my_map(np.asarray(harley_df.Begin_Lon), np.asarray(harley_df.Begin_Lat))
harley_df['xm'] = xs.tolist()
harley_df['ym'] = ys.tolist()
for index,row in harley_df.iterrows():
    x,y = my_map(harley_df.Begin_Lon, harley_df.Begin_Lat)
    my_map.plot(row.xm, row.ym,markerfacecolor =([1,0,0]),  marker='o', markersize= 5, alpha = 0.75)
plt.title('Weather events distribution')
plt.show()

# Geoplot most affected counties
my_map = Basemap(projection='merc',
            resolution = 'l', area_thresh = 1000.0,
            llcrnrlon=harley_df["Begin_Lon"].min() - 1, llcrnrlat=harley_df["Begin_Lat"].min() - 1, #min longitude (llcrnrlon) and latitude (llcrnrlat)
            urcrnrlon=harley_df["Begin_Lon"].max() + 1, urcrnrlat=harley_df["Begin_Lat"].max() + 1) #max longitude (urcrnrlon) and latitude (urcrnrlat)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'white', alpha = 0.3)
my_map.shadedrelief()       
my_map.bluemarble()
xs,ys = my_map(np.asarray(hpc_counties.Begin_Lon), np.asarray(hpc_counties.Begin_Lat))
hpc_counties['xm'] = xs.tolist()
hpc_counties['ym'] = ys.tolist()
for index,row in hpc_counties.iterrows():
    x,y = my_map(hpc_counties.Begin_Lon, hpc_counties.Begin_Lat)
    my_map.plot(row.xm, row.ym,markerfacecolor =([1,0,0]),  marker='o', markersize= 5, alpha = 0.75)
plt.title('Weather events distribution')
plt.show()

my_map = Basemap(projection='merc',
            resolution = 'l', area_thresh = 1000.0,
            llcrnrlon=texas_df["Begin_Lon"].min() - 1, llcrnrlat=texas_df["Begin_Lat"].min() - 1, #min longitude (llcrnrlon) and latitude (llcrnrlat)
            urcrnrlon=texas_df["Begin_Lon"].max() + 1, urcrnrlat=texas_df["Begin_Lat"].max() + 1) #max longitude (urcrnrlon) and latitude (urcrnrlat)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'white', alpha = 0.3)
my_map.shadedrelief()       
my_map.bluemarble()
xs,ys = my_map(np.asarray(hpc_counties.Begin_Lon), np.asarray(hpc_counties.Begin_Lat))
hpc_counties['xm'] = xs.tolist()
hpc_counties['ym'] = ys.tolist()
for index,row in hpc_counties.iterrows():
    x,y = my_map(hpc_counties.Begin_Lon, hpc_counties.Begin_Lat)
    my_map.plot(row.xm, row.ym,markerfacecolor =([1,0,0]),  marker='o', markersize= 5, alpha = 0.75)
plt.title('Weather events distribution')
plt.show()
