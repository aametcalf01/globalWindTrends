# globalWindTrends
Step 1: Ran ID_Lat_Lon.ipynp (globalWindTrends/scripts/dataCleaning/ID_Lat_Lon.ipynb) 
    which did the following:
    - opens isd-history.csv
    - creates new "ID" field = "USAF"+"WBAN"
    -  Deletes records w/ both lat and lon == 0 or lat and lon == null
    - Starts with 29,963 records and winnows the dataset down to 27,813 recores
    - Writes to file "ID-Info.csv", which is basically "isd-history" with the records mentioned above
    removed
    - Writes to file "IDs_27813.csv", which is simply a list of the remaining IDs.

Step 2: created totalStationMap in ArcGIS Pro from "ID-Info.csv" created in step 1. This map shows all of the stations remaining after data cleaning in step 1.   Used totalStationMap.py file with arcpy to create the point shapefile.  
