import arcpy

#Set environment settings
arcpy.env.workspace = r"C:\Users\andymetcalf\Documents\research\globalWindTrends\data_light\tempNDVI"

# Get and print a list of GRIDs from the workspace
rasters = arcpy.ListRasters("*", "TIF")
print(rasters)

# arcpy.management.Mosaic(rasters,rasters[0])





#arcpy.management.Mosaic("T0_NDVI;T1_NDVI", r"C:\Users\andymetcalf\Documents\research\globalWindTrends\arcGIS\test\test.gdb\T0_NDVI", "LAST", "FIRST", None, None, "NONE", 0, "NONE")