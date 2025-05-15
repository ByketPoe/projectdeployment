from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
        return "This is index"

# get all
@app.route('/data', methods=['GET'])
def getdata():
        return "getdata"

# get by id
@app.route('/data/<int:id>', methods=['GET'])
def getdatabyid(id):
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