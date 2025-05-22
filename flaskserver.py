from flask import Flask, request, jsonify, abort
from scidataDAO import sciDAO

app = Flask(__name__)

@app.route('/')
def index():
        return "This is index"

# get all collections
@app.route('/datacollections', methods=['GET'])
def getcollections():
        # get info on all collections
        return jsonify(sciDAO.getAllCollections())
        
# get all collection types
@app.route('/datacollectiontypes', methods=['GET'])
def getcollectiontypes():
        # get info on all collection types
        return jsonify(sciDAO.getAllCollectionTypes())

# get data by id
@app.route('/datacollections/<int:id>', methods=['GET'])
def getdatabycid(id):
        # get data by collection id
        return jsonify(sciDAO.getDataByID(id))

# create collection
@app.route('/datacollections', methods=['POST'])
def createcollection():
        # create new collection of data
        jsonstring = request.json
        collection = {}
        if "name" not in jsonstring:
                abort(403)
        collection["name"] = jsonstring["name"]
        if "collectiontypeid" not in jsonstring:
                abort(403)
        collection["collectiontypeid"] = jsonstring["collectiontypeid"]
        if "startdate" not in jsonstring:
                abort(403)
        collection["startdate"] = jsonstring["startdate"]
        if "enddate" not in jsonstring:
                abort(403)
        collection["enddate"] = jsonstring["enddate"]
        if "locationname" not in jsonstring:
                abort(403)
        collection["locationname"] = jsonstring["locationname"]
        if "measurement" not in jsonstring:
                abort(403)
        collection["measurement"] = jsonstring["measurement"]
        if "units" not in jsonstring:
                abort(403)
        collection["units"] = jsonstring["units"]
        return jsonify(sciDAO.createCollection(collection))

# create data
@app.route('/datacollections', methods=['POST'])
def createdata():
        # create new data entry
        jsonstring = request.json
        data = {}
        if "id" not in jsonstring:
                abort(403)
        data["id"] = jsonstring["id"]
        if "collectionname" not in jsonstring:
                abort(403)
        data["collectionname"] = jsonstring["collectionname"]
        if "datum" not in jsonstring:
                abort(403)
        data["datum"] = jsonstring["datum"]
        if "lat" not in jsonstring:
                abort(403)
        data["lat"] = jsonstring["lat"]
        if "long" not in jsonstring:
                abort(403)
        data["long"] = jsonstring["long"]
        if "datetime" not in jsonstring:
                abort(403)
        data["datetime"] = jsonstring["datetime"]
        return jsonify(sciDAO.createData(data["collectionname"], data))

# update collection
@app.route('/datacollections/<int:id>', methods=['PUT'])
def updatedata(id):
        # update existing collection 
        jsonstring = request.json
        collection = {}
        if "name" in jsonstring:
                collection["name"] = jsonstring["name"]
        if "collectiontypeid" in jsonstring:
                collection["collectiontypeid"] = jsonstring["collectiontypeid"]
        if "startdate" in jsonstring:
                collection["startdate"] = jsonstring["startdate"]
        if "enddate" in jsonstring:
                collection["enddate"] = jsonstring["enddate"]
        if "locationname" in jsonstring:
                collection["locationname"] = jsonstring["locationname"]
        if "measurement" in jsonstring:
                collection["measurement"] = jsonstring["measurement"]
        if "units" in jsonstring:
                collection["units"] = jsonstring["units"]
        return jsonify(sciDAO.updateCollection(collection))

# update data
@app.route('/data/<int:id>', methods=['PUT'])
def updatedata(id):
        jsonstring = request.json
        return f"update {id} {jsonstring}"

# delete collection
@app.route('/datacollections/<str:name>', methods=['DELETE'])
def deletedata(name):
        return jsonify(sciDAO.deleteCollection(name))

# delete data
@app.route('/data/<int:id>', methods=['DELETE'])
def deletedata(id):
        return jsonify(sciDAO.deleteData(id))

if __name__ == "__main__":
    app.run(debug = True)