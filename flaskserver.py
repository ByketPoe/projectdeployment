from flask import Flask, request, jsonify, abort, render_template
from scidataDAO import sciDAO
import externalsource 

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

#get map
@app.route('/map')
def getmap():
        return render_template('map.html')

# get external
@app.route('/getexternal', methods=['GET'])

def getexternal():
        # get info on all collections
        return externalsource.runExternal.runAll()

# get collections count
@app.route('/datacollectionscount', methods=['GET'])
def getcollectionscount():
        # get info on all collections
        return jsonify(sciDAO.getCollectionsCount())

# get all collections
@app.route('/datacollections', methods=['GET'])
def getcollections():
        # get info on all collections
        return jsonify(sciDAO.getAllCollections())

# show collection types page
@app.route('/datacollectiontypes', methods=['GET'])
def renderctypes():
        return render_template('collectiontypes.html')
       
# get all collection types
@app.route('/getdatacollectiontypes', methods=['GET'])
def getcollectiontypes():
        # get info on all collection types
        return jsonify(sciDAO.getAllCollectionTypes())

# show data page
@app.route('/data', methods=['GET'])
def renderdata():
        return render_template('createdata.html')

# get all data
@app.route('/getdata', methods=['GET'])
def getdata():
        # get info on all data
        return jsonify(sciDAO.getAllData())

# get collection by id
@app.route('/datacollections/<int:id>', methods=['GET'])
def getcollectionbyid(id):
        # get data by collection id
        return jsonify(sciDAO.getCollectionByID((id,)))
# get data by id
@app.route('/data/<int:id>', methods=['GET'])
def getdatabyid(id):
        # get data by collection id
        return jsonify(sciDAO.getDataByID((id,)))

# create collection
@app.route('/datacollections/', methods=['POST'])
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
        if "location" not in jsonstring:
                abort(403)
        collection["location"] = jsonstring["location"]
        if "measurement" not in jsonstring:
                abort(403)
        collection["measurement"] = jsonstring["measurement"]
        if "units" not in jsonstring:
                abort(403)
        collection["units"] = jsonstring["units"]
        return jsonify(sciDAO.createCollection(collection))
# create data
@app.route('/data/', methods=['POST'])
def createdata():
        # create new data entry
        jsonstring = request.json
        data = {}
        if "collectionid" not in jsonstring:
                abort(403)
        data["collectionid"] = jsonstring["collectionid"]
        if "datum" not in jsonstring:
                abort(403)
        data["datum"] = jsonstring["datum"]
        if "latitude" not in jsonstring:
                abort(403)
        data["latitude"] = jsonstring["latitude"]
        if "longitude" not in jsonstring:
                abort(403)
        data["longitude"] = jsonstring["longitude"]
        if "datecollected" not in jsonstring:
                abort(403)
        data["datecollected"] = jsonstring["datecollected"]
        return jsonify(sciDAO.createData(data))

# update collection
@app.route('/datacollections/<int:id>', methods=['PUT'])
def updatecollection(id):
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
        if "location" in jsonstring:
                collection["location"] = jsonstring["location"]
        if "measurement" in jsonstring:
                collection["measurement"] = jsonstring["measurement"]
        if "units" in jsonstring:
                collection["units"] = jsonstring["units"]
        return jsonify(sciDAO.updateCollection(collection, id))
# update data
@app.route('/data/<int:id>', methods=['PUT'])
def updatedata(id):
        # update existing data 
        jsonstring = request.json
        data = {}
        if "collectionid" in jsonstring:
                data["collectionid"] = jsonstring["collectionid"]
        if "datum" in jsonstring:
                data["datum"] = jsonstring["datum"]
        if "latitude" in jsonstring:
                data["latitude"] = jsonstring["latitude"]
        if "longitude" in jsonstring:
                data["longitude"] = jsonstring["longitude"]
        if "datecollected" in jsonstring:
                data["datecollected"] = jsonstring["datecollected"]       
        return jsonify(sciDAO.updateData(data, id))

# delete collection
@app.route('/datacollections/<int:id>', methods=['DELETE'])
def deletecollection(id):
        return jsonify(sciDAO.deleteCollection(id))
# delete data
@app.route('/data/<int:id>', methods=['DELETE'])
def deletedata(id):
        return jsonify(sciDAO.deleteData(id))

if __name__ == "__main__":
    app.run(debug = True)