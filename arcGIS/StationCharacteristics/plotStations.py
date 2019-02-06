import arcpy

#Set environment settins
arcpy.env.workspace = r"C:\Users\andymetcalf\Documents\research\globalWindTrends\arcGIS\StationCharacteristics\StationCharacteristics.gdb"
arcpy.env.overwriteOutput = True

print(arcpy.env.workspace)
#Set the local variables
in_table = r"C:\Users\andymetcalf\Documents\research\globalWindTrends\data_light\ID_Info.csv"
out_feature_class = "stationLocations"
x_coords = "LON"
y_coords = "LAT"

#Make the layer
arcpy.management.XYTableToPoint(in_table,
                                out_feature_class,
                                x_coords,
                                y_coords)

# Print the total rows
print(arcpy.GetCount_management(out_feature_class))