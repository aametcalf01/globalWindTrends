# globalWindTrends
Step 1: Ran ID_Lat_Lon.ipynp (globalWindTrends/scripts/dataCleaning/ID_Lat_Lon.ipynb) 
    which did the following:
    - opens isd-history.csv
    - creates new "ID" field = "USAF"+"WBAN"
    -  Deletes records w/ both lat and lon == 0 or lat and lon == null
    - Starts with 28,646 records and winnows the dataset down to 28,228 recores
    - Writes to file "ID-Info.csv", which is basically "isd-history" with the records mentioned above
    removed
    - Writes to file "IDs_23686.csv", which is simply a list of the remaining IDs.
