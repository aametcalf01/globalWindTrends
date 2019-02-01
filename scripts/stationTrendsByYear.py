import sys
import os
import pandas as pd
import numpy as np
from calcAngleDir import calcAngleDir

# span of years to calculate trends over 
# set is inclusive, i.e., [beginYear, endYear]
beginYear = int(sys.argv[1])
endYear = int(sys.argv[2])


#Below is the function to calculate the stats
def calcAnnualStationStats(beginYear, endYear):
    
    #change to directory where data is stored
    os.chdir("/users/a/a/aametcal/scratch/isd-lite/data")
    
    #loop through the years specified by function
    for year in range(beginYear, endYear+1):
        
        #change to the directory for a specific year
        os.chdir(str(year))
        
        # make a list of all the files in a certain year
        lst = [f for f in os.listdir() if not f.startswith('.')]
        
        # looping through the files in that specific year
        for file in lst:
            
            # read data into pandas data frame
            df = pd.read_csv(file, compression='gzip', header=None, sep=r"\s+",
                             engine = "python",
                             names = ["Year","Month","Day","Hour","Temperature","DewPoint", "SLP",
       "Direction","Speed","CoverageCode", "Depth1","Depth6"])
            

            # Create python lists for direction and speed list
            # We use this instead of np.arrays since calcAngleDir takes
            # as input lists
            directionList = df.Direction.tolist()
            speedList = df.Speed.tolist()
            
            #calculate prevailing wind for that year
            prevail = calcAngleDir(directionList,speedList)
   
            #make numpy array for speed to calculate mean and median
            speedArray = np.asarray(speedList)
         
            meanSpeed = np.mean(speedArray)
            medianSpeed = np.median(speedArray)
            
            #make a one row pandas df to append
            column_names = ["year","meanWindSpeed", "medianWindSpeed", "prevailingWind"]
            d = pd.DataFrame(columns = column_names)
            d.loc[0] = [str(year),meanSpeed,medianSpeed,prevail]
            
            #make filename out of original filename ex. 029070-99999-1902.gz
            filename = str(file[:-8])
            path = "/users/a/a/aametcal/scratch/isd-lite/annual/"+filename+".csv"
            
            #if file does not exist, write header
            if not os.path.isfile(path):
                d.to_csv(path,header = column_names,index=False,float_format='%.0f')
            else: # if it exists append without writing the header
                # (mode = 'a' for append)
                d.to_csv(path,mode='a',header=False,index=False,float_format='%.0f')

        os.chdir("../") #head back to grab anther year
    return

#call calcAnnualStationStats
calcAnnualStationStats(beginYear, endYear)



