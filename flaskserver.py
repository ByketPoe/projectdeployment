from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
        return "This is index"

# get all collections
@app.route('/data', methods=['GET'])
def getdata():
        # get info on all collections
        
        return "getdata"

# get all collection types
@app.route('/data', methods=['GET'])
def getcollectiontypes():
        # get info on all collection types
        
        return "getdata"

# get data by id
@app.route('/data/<int:id>', methods=['GET'])
def getdatabycid(id):
        # get data by collection id
        return "get data by id"

# create
@app.route('/data', methods=['POST'])
def createdata():
        jsonstring = request.json
        return f"create {jsonstring}"

# update
@app.route('/data/<int:id>', methods=['PUT'])
def updatedata(id):
        jsonstring = request.json
        return f"update {id} {jsonstring}"

# delete
@app.route('/data/<int:id>', methods=['DELETE'])
def deletedata(id):
        return f"delete {id}"

if __name__ == "__main__":
    app.run(debug = True)