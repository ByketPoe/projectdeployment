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
        return f"create {jsonstring}"

# update
@app.route('/datacollections/<int:id>', methods=['PUT'])
def updatedata(id):
        jsonstring = request.json
        return f"update {id} {jsonstring}"

# delete
@app.route('/datacollections/<int:id>', methods=['DELETE'])
def deletedata(id):
        return f"delete {id}"

if __name__ == "__main__":
    app.run(debug = True)