import arcpy

#Set environment settings
arcpy.env.workspace = r"C:\Users\andymetcalf\Documents\research\globalWindTrends\arcGIS\totalStationMap\totalStationMap.gdb"

print(arcpy.env.workspace)