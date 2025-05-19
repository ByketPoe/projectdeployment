# Science Data DAO
# Object for accessing, updating and deleting science data from database
# Author: Emma Farrell

class SciDAO:
    # get all collections          
    def getAllCollections(self):
        #TODO implement
        return [{"id":"1", "collectiontypeid":1, "startdate":"2025-04-04 00:00:00", "enddate":"2025-06-04 00:00:00", "locationname":"Rockall", "measurement":"Temperature", "units":"Celsius"}]
    # get all collection types 
    def getAllCollectionTypes(self):
        #TODO implement
        return [{"id":"1", "collectiontype":"time series"}]
    # find by id
    def getDataByID(self, id):
        #TODO implement
        return [{"id":"1", "collectionid":1, "datum":"2.2", "lat":"0", "long":"0", "datetime":"2025-06-04 00:00:00"}]
    # create a book
    def create(self, book):
        return {"id":1,"title":"blah","author":"someone","price":999}
    #update 
    def update(self,id , book):
        return {"id":1,"title":"blah","author":"someone","price":999}
    # delete a book of a given id    
    def delete(self, id):
        return True
        
sciDAO = SciDAO()

if __name__ == "__main__":
    book = {"id":1,"title":"blah","author":"someone","price":999} 
    print ("test getall")
    print (f"\t{sciDAO.getAll()}")
    print ("test findById(1)")
    print (f"\t{sciDAO.findByID(1)}")
    print ("test create")
    print (f"\t{sciDAO.create(book)}")
    print ("test update")
    print (f"\t{sciDAO.update(1,book)}")
    print ("test delete")
    print (f"\t{sciDAO.delete(1)}")