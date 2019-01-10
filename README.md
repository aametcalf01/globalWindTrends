# globalWindTrends
Step 1: Ran ID_Lat_Lon.ipynp (/users/a/a/aametcal/isd-lite/scripts/dataCleaning) 
    which did the following:
    - opens isd-history.csv
    - creates new "ID" field = "USAF"+"WBAN"
    -  Deletes records w/ both lat and lon == 0 or lat and lon == null
    - Starts with 28,646 records and winnows the dataset down to 28,228 recores
    - Writes to file "ID-Info.csv", which is basically "isd-history" with the records mentioned above
    removed
    - Writes to file "IDs_23686.csv", which is simply a list of the remaining IDs.

Step 2: created a field in ArcGIS LatLonKey called DateDiff which is the difference in years between start and
    end times.  This should be helpful for future queries.
