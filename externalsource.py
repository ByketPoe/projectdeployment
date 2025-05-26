import requests
import pandas as pd
# import geopandas as gpd
from xml.dom.minidom import parseString
# from shapely.geometry import Point, Polygon, LineString
# import matplotlib.pyplot as plt
import folium

class runExternal:
    def runAll():
        m = folium.Map(location=(51.455211, -10.683017), zoom_start=6)


        url = "https://atlas.marine.ie/arcgis/services/21_Appendix_E_Maps_of_Fish_Spawning_and_Nursery_Grounds/MapServer/WMSServer?request=GetCapabilities&service=WMS"
        page = requests.get(url)
        doc = parseString(page.content)
        coordDict = {"cols":[], "geometry":[]}
        #print(doc.toprettyxml())

        boundingBoxNodes = doc.getElementsByTagName("EX_GeographicBoundingBox")
        polygonindex = 0 
        for boundingBoxNode in boundingBoxNodes:
            coordDict["cols"].append(polygonindex)
            geometry = []
            westnode = boundingBoxNode.getElementsByTagName("westBoundLongitude").item(0)
            west = westnode.firstChild.nodeValue.strip()
            west = float(west)
            # print(type(west))
            #geometry.append(west)

            eastnode = boundingBoxNode.getElementsByTagName("eastBoundLongitude").item(0)
            east = eastnode.firstChild.nodeValue.strip()
            east = float(east)
            #geometry.append(east)

            southnode = boundingBoxNode.getElementsByTagName("southBoundLatitude").item(0)
            south = southnode.firstChild.nodeValue.strip()
            south = float(south)
            #geometry.append(south)

            northnode = boundingBoxNode.getElementsByTagName("northBoundLatitude").item(0)
            north = northnode.firstChild.nodeValue.strip()
            north = float(north)
            #geometry.append(north)
            tuple1 = (south, west)
            tuple2 = (north, west)
            tuple3 = (north, east)
            tuple4 = (south, east)
            geometry.append(tuple1)
            geometry.append(tuple2)
            geometry.append(tuple3)
            geometry.append(tuple4)
            #geometry = tuple(geometry)
            #line = Polygon(geometry)
            #print(poly)
            # coordDict["geometry"].append(line)
            coordDict["geometry"].append(geometry)
            polygonindex += 1

        df = pd.DataFrame(coordDict)

        for poly in df["geometry"]:
            folium.vector_layers.Polygon(poly, tooltip="Nursing Boundary").add_to(m)

        m.save("templates/map.html")
        return "True"

if __name__ == "__main__":
    runExternal.runAll()