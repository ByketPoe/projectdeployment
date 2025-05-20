# Science Data DAO
# Object for accessing, updating and deleting science data from database
# Author: Emma Farrell

class SciDAO:
    # get all collections          
    def getAllCollections(self):
        #TODO implement
        return {"name":1, "collectiontypeid":1, "startdate":"2025-04-04 00:00:00", "enddate":"2025-06-04 00:00:00", "locationname":"Rockall", "measurement":"Temperature", "units":"Celsius"}
    # get all collection types 
    def getAllCollectionTypes(self):
        #TODO implement
        return {"id":1, "collectiontype":"time series"}
    # find by id
    def getDataByID(self, id):
        #TODO implement
        return {"id":1, "collectionname":"collection1", "datum":"2.2", "lat":"0", "long":"0", "datetime":"2025-06-04 00:00:00"}
    # create a collection
    def createCollection(self, colname):
        #TODO implement
        return colname
    # add data to collection
    def createData(self, colname, data):
        #TODO implement
        return {"id":1, "collectionname":"collection1", "datum":"2.2", "lat":"0", "long":"0", "datetime":"2025-06-04 00:00:00"}
    # update collection
    def updateCollection(self, colname):
        #TODO implement
        return {"name":"collection1", "collectiontypeid":1, "startdate":"2025-04-04 00:00:00", "enddate":"2025-06-04 00:00:00", "locationname":"Rockall", "measurement":"Temperature", "units":"Celsius"}
    # update data
    def updateData(self, colname, data):
        #TODO implement
        return {"id":1, "collectionname":"collection1", "datum":"2.2", "lat":"0", "long":"0", "datetime":"2025-06-04 00:00:00"}
    # delete a collection    
    def deleteCollection(self, id):
        #TODO implement
        return True
    # delete data   
    def deleteData(self, id):
        #TODO implement
        return True
        
sciDAO = SciDAO()

if __name__ == "__main__":
    collection = {"name":"collection2", "collectiontypeid":1, "startdate":"2025-04-04 00:00:00", "enddate":"2025-06-04 00:00:00", "locationname":"Rockall", "measurement":"Temperature", "units":"Celsius"} 
    data = {"id":2, "collectionname":"collection1", "datum":"2.2", "lat":"0", "long":"0", "datetime":"2025-06-04 00:00:00"}
    print ("test getallCollections")
    print (f"\t{sciDAO.getAllCollections()}")
    print ("test getallCollectionTypes")
    print (f"\t{sciDAO.getAllCollectionTypes()}")
    print ("test finddataById(1)")
    print (f"\t{sciDAO.getDataByID(1)}")
    print ("test create collection")
    print (f"\t{sciDAO.createCollection(collection)}")
    print ("test create data")
    print (f"\t{sciDAO.createCollection(data)}")
    print ("test update collection")
    print (f"\t{sciDAO.updateCollection(collection)}")
    print ("test update data")
    print (f"\t{sciDAO.updateData(collection, data)}")
    print ("test delete collection")
    print (f"\t{sciDAO.deleteCollection(1)}")
    print ("test delete data")
    print (f"\t{sciDAO.deleteData(1)}")