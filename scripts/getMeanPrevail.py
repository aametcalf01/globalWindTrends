#This script was created to calculated the slopes of the regression OLS regression 
#on the annual mean wind speed for continuous records from 'start' to 'end'.  The output 
#is a .csv file called stationAttr.csv (housed in the data-light directory with the 
#following attributes:
#stationNumber: the station id
#slope: the OLS regression slope of the annual mean wind speeds
#lowBound: the lower 95% confidence bound of the OLS slope
#hightBound: the upper 95% confidence bound of the OLS slope
#slopeInt: {1 if lowBound & highBound >0, -1 if lowBound & highBound>0, else 0}
            #==> indicates positive or negative trend
#pw<start>: prevailing wind "start"
#pw<end>: prevailing wind "end"

#imports
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import statsmodels.api as sm
import csv
import math

def calcAngleDiff(a1,a2):
    """function we use to calculate the different between prevailing wind
    vectors"""
    a1 = math.radians(a1)
    a2 = math.radians(a2)
    return abs(math.degrees(math.atan2(math.sin(a2-a1), math.cos(a2-a1))))

start = 1990
end = 2017
startAbr = str(90)
endAbr = str(17)
span = end-start+1 #this span is inclusive of start and end years

#get a list of all of the stations in the annual directory
os.chdir("/users/a/a/aametcal/scratch/isd-lite/annual"+startAbr)
annualStationList = os.listdir()

#get a list of all of the id's that we previously selected
#when preprocessing data
os.chdir("/users/a/a/aametcal/isd-lite/data_light/")
df = pd.read_csv('IDs_27813.csv',header = None)
statList = df[0].tolist()

#take off the .csv from the annualStationList
for i in range(len(annualStationList)):
    annualStationList[i] = annualStationList[i][0:-4]
    
#turn into sets so we can perform intersect
statSet = set(statList)
annualStationSet = set(annualStationList)

#perform intersect to get stations for analysis
stationSet = statSet.intersection(annualStationSet)

#turn stationSet into a list
stationList = list(stationSet)

#add back the .csv
for i in range(len(stationList)):
    stationList[i] = stationList[i]+".csv"
    

#Compute desired atributes for stations that have continuous
#data ranging from "start"-"end" (landsat data range)

os.chdir("/users/a/a/aametcal/scratch/isd-lite/annual"+startAbr)

with open("/users/a/a/aametcal/isd-lite/data_light/meanPrevail"+startAbr+".csv", mode = 'w') as csv_file:
    fieldnames = ["stationNumber",
                  "slope",
                  "lowBound",
                  "hightBound",
                  "slopeInt",
                  "meanWind",
                  "mw"+str(start),
                  "mw"+str(end),
                  "pw"+str(start),
                  "pw"+str(end),
                  "pwDiff"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    for station in stationList:
        sdf = pd.read_csv(station)
        if len(sdf) !=span:
            continue
        else:
            X = sdf.year
            #add a column of ones for intercept
            X_ = sm.add_constant(X)
            y = sdf.meanWindSpeed

            model = sm.OLS(y,X_).fit()
            #get the 95% confidence interval
            ci = model.conf_int(alpha=0.05)

            #calculate values for dictionary
            slope = model.params[1]
            lowBound = ci[0][1]
            highBound = ci[1][1]
            #print(slope, lowBound, highBound)
            stationNumber = station[0:-4]
            pwStart = sdf.prevailingWind.values[0]
            pwEnd = sdf.prevailingWind.values[-1] 
            
            mwStart = sdf.meanWindSpeed.values[0]
            mwEnd = sdf.meanWindSpeed.values[-1]
            mws = sdf.meanWindSpeed.mean()
            
            pwDiff = calcAngleDiff(pwStart,pwEnd)

            if (lowBound<0 and highBound<0):
                slopeInt = -1
            elif (lowBound>0 and highBound>0):
                slopeInt = 1
            else:
                slopeInt = 0
            
            writer.writerow({"stationNumber":stationNumber,
                  "slope":slope,
                  "lowBound":lowBound,
                  "hightBound":highBound,
                  "slopeInt":slopeInt,
                  "meanWind":mws,
                  "mw"+str(start):mwStart,
                  "mw"+str(end):mwEnd,
                  "pw"+str(start):pwStart,
                  "pw"+str(end):pwEnd,
                  "pwDiff":pwDiff})
        