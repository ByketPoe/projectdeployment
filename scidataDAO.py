# Science Data DAO
# Object for accessing, updating and deleting science data from database
# Author: Emma Farrell

import mysql.connector
import glob
if glob.glob("db_config.py"):
    print(True)
    import db_config as cfg
else:
    import db_configpa as cfg

class SciDAO:
    conn = ""
    cursor = ""
    host = ""
    user = ""
    pw = ""
    db = ""

    dbvalues = {
        "collection": ["id", "name", "collectiontypeid", "startdate", "enddate", "location", "measurement", "units"],
        "collection_type": ["id", "collectiontype"],
        "data": ["id", "collectionid", "datum", "latitude", "longitude", "datecollected"]
    }

    def __init__(self):
        self.host = cfg.sql["host"]
        self.user = cfg.sql["user"]
        self.pw = cfg.sql["password"]
        self.db = cfg.sql["database"]
    
    def getcursor(self):
        self.conn = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.pw,
            database = self.db,
        )
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def closeAll(self):
        self.conn.close()
        self.cursor.close()

    def fetchAll(self, sqlstring, querytable):
        cursor = self.getcursor()
        cursor.execute(sqlstring)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result, querytable))
        self.closeAll()
        return returnArray

    def fetchOne(self, sqlstring, values, querytable): # values is a tuple
        cursor = self.getcursor()
        cursor.execute(sqlstring, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result, querytable)
        self.closeAll()
        return returnvalue

    def commitChange(self, changeitem, sqlstring, values, committype): # values is a tuple, commit type is a string (UPDATE, CREATE, DELETE)
        cursor = self.getcursor()
        cursor.execute(sqlstring, values)
        self.conn.commit()
        if committype.upper() == "CREATE":
            newid = cursor.lastrowid
            changeitem["id"] = newid
            self.closeAll()
            return changeitem
        else:
            self.closeAll()
            print(committype, "completed on item: ", changeitem)

    def fetchCount(self, sqlstring): # values is a tuple
        cursor = self.getcursor()
        cursor.execute(sqlstring)
        result = cursor.fetchall()
        returnvalue = self.convertToDictionary(result, ["count"])
        self.closeAll()
        return returnvalue
    
    # get count of collections        
    def getCollectionsCount(self):
        #TODO comment
        sqlstring = "SELECT COUNT(*) FROM collection"
        returnArray = self.fetchCount(sqlstring)
        return returnArray

    # get all collections          
    def getAllCollections(self):
        #TODO comment
        sqlstring = "SELECT C.id, name, CT.collectiontype, startdate, enddate, location, measurement, units FROM collection C JOIN collection_type CT ON C.collectiontypeid = CT.id"
        returnArray = self.fetchAll(sqlstring, self.dbvalues["collection"])
        return returnArray
    # get all collection types 
    def getAllCollectionTypes(self):
        #TODO comment
        sqlstring = "SELECT * FROM collection_type"
        returnArray = self.fetchAll(sqlstring, self.dbvalues["collection_type"])
        return returnArray
    # get all data
    def getAllData(self):
        #TODO comment
        sqlstring = "SELECT D.id, C.name, datum, latitude, longitude, datecollected FROM data D JOIN collection C ON D.collectionid = C.id"
        returnArray = self.fetchAll(sqlstring, self.dbvalues["data"])
        return returnArray
    # find collection by id
    def getCollectionByID(self, id):
        #TODO comment
        sqlstring = "SELECT * FROM collection WHERE id = %s"
        returnArray = self.fetchOne(sqlstring, id, self.dbvalues["collection"])
        return returnArray
    # find data by id
    def getDataByID(self, id):
        #TODO test
        sqlstring = "SELECT * FROM data WHERE id = %s"
        returnArray = self.fetchOne(sqlstring, id, self.dbvalues["data"])
        return returnArray
    # create a collection
    def createCollection(self, collection):
        #TODO comment
        sqlstring = "INSERT INTO collection (name, collectiontypeid, startdate, enddate, location, measurement, units) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (collection["name"], collection["collectiontypeid"], collection["startdate"], collection["enddate"], collection["location"], collection["measurement"], collection["units"])
        self.commitChange(collection, sqlstring, values, "CREATE")
        return collection
    # add data to collection
    def createData(self, data):
        #TODO comment
        sqlstring = "INSERT INTO data (collectionid, datum, latitude, longitude, datecollected) VALUES (%s, %s, %s, %s, %s)"
        values = (data["collectionid"], data["datum"], data["latitude"], data["longitude"], data["datecollected"])
        self.commitChange(data, sqlstring, values, "CREATE")
        return data
    # update collection
    def updateCollection(self, collection, id):
        #TODO comment
        sqlstring = "UPDATE collection SET name = %s, collectiontypeid = %s, startdate = %s, enddate = %s, location = %s, measurement = %s, units = %s WHERE id = %s"
        values = (collection["name"], collection["collectiontypeid"], collection["startdate"], collection["enddate"], collection["location"], collection["measurement"], collection["units"], id)
        self.commitChange(collection, sqlstring, values, "UPDATE")
    # update data
    def updateData(self, data, id):
        #TODO comment
        sqlstring = "UPDATE data SET collectionid = %s, datum = %s, latitude = %s, longitude = %s, datecollected = %s WHERE id = %s"
        values = (data["collectionid"], data["datum"], data["latitude"], data["longitude"], data["datecollected"], id)
        self.commitChange(data, sqlstring, values, "UPDATE")
    # delete a collection    
    def deleteCollection(self, id):
        #TODO comment
        sqlstring = "DELETE FROM collection WHERE id = %s"
        values = (id,)
        self.commitChange(None, sqlstring, values, "DELETE")
    # delete data   
    def deleteData(self, id):
        #TODO comment
        sqlstring = "DELETE FROM data WHERE id = %s"
        values = (id,)
        self.commitChange(None, sqlstring, values, "DELETE")
    def convertToDictionary(self, resultLine, attkeys):
        dictOut = {}
        currentkey = 0
        for attrib in resultLine:
            dictOut[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return dictOut
        
sciDAO = SciDAO()

if __name__ == "__main__":
    collection = {"name":"cool", "collectiontypeid":2, "startdate":"2025-05-04 00:00:00", "enddate":"2025-07-04 00:00:00", "location":"Lough Key", "measurement":"Salinity", "units":"g/L"} 
    data = {"collectionid":1, "datum":"5.9", "latitude":"12.678", "longitude":"25.806796", "datecollected":"2025-07-04 21:37:22"}
    print(sciDAO.createCollection(collection))
    # print(sciDAO.createData(data))
    # sciDAO.updateCollection(collection, 2)
    # sciDAO.updateData(data, 1)
    # sciDAO.deleteCollection(2)
    # sciDAO.deleteData(1)
    # sciDAO.createData(data)
    # print(sciDAO.getAllCollections())
    # print(sciDAO.getAllCollectionTypes())
    # print(sciDAO.getAllData())
    print(sciDAO.getCollectionsCount())