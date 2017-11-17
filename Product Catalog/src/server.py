import pymongo
from flask import Flask, request, jsonify,abort
from flask_pymongo import PyMongo
from bson.json_util import dumps
import json
import bson
from bson.objectid import ObjectId
from bson import json_util
from pymongo import errors
from client import mongo_client

app = Flask(__name__)

client = mongo_client()

#The GET request returns all the books in the database.
 
@app.route('/v1/books', methods=['GET'])
def books():
    response = client.get_all()
    data = json.loads(response)
    if data["data"] is None:
        abort(404)
    return jsonify(data)

# The GET request with oid returns a particular document having that Id
# The PUT request decrements the quantity of the book in the inventory

@app.route('/v1/books/<oid>', methods=['GET','PUT'])
def book_by_id(oid):    
    if request.method =='PUT':
        response = client.put_one(oid)
        data = json.loads(response)
        if data["Status"] == 'OK':
             return jsonify({"Status":"OK"})
    elif request.method == 'GET':
        response = client.get_one(oid)
        data = json.loads(response)
        print(data['data'])
        if data["data"] is None:
             abort(404)
        return jsonify(data)
    #return data



@app.errorhandler(404)
def not_found(e):
    return 'Not found'


if __name__ == '__main__':
    app.run(debug=True)
