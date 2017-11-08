"""
This file contains the basic crud operations required for
the myorders(financial data) module
_id -> primary key of the collection (automatically generated by
mongoDB)
userId -> getFromUserSessions
cartId -> getFromShoppingCart
totalAmount -> getFromShoppingCart
"""

from pymongo import MongoClient
from pprint import pprint
mongo_cluster = ("mongodb://kajal:kajal@cluster0-shard-00-00-pjkz1.mongodb.net:27017,"
                "cluster0-shard-00-01-pjkz1.mongodb.net:27017,"
                "cluster0-shard-00-02-pjkz1.mongodb.net:27017"
                "/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")

client = MongoClient(mongo_cluster)

#Database name
db = client["bookstore"]

#Collection name
myCart = db["shoppingCart"]


#API call to user database
userDetails = {
               "userName" : "abcde"
              }

def getUserDetails():
    return userDetails

userId = userDetails["userName"]

"""
addToMyOrders: This method adds transaction of orders to the my orders
"""
def addToMyOrders(userId, cartId):
    #dummy details
    #APICallToProductCatalog
    #productDetails = "curl http://localhost:5000/books/"+productId


    #document to insert
    item = {}

    #Check the schema for user database
    item['userId'] = userDetails['userName']

    #check the exact attribute name for the image
    cartId = myCart.insert_one(item).inserted_id
    #print(cartId)
    
"""
getCartDetails: display the transactions details 
    cartId: id of cart whose cart content is to be displayed
"""
def getCartDetails(cartId):
    items = myCart.find({"cartId":cartId})
    for item in items:
        pprint(item)
        
 #method to delete the transaction  
 -@application.route("/cart/<cartId>>",methods=['DELETE'])
 -def deleteOrders(orderId, cartId):
 +@app.route("/v1/cart",methods=['DELETE'])
 +def deleteOrders():
      try:
 -        myOrders.delete_one({"orderId":orderId, "cartId" : cartId})
 +        orderId = request.json['orderId']
 +        cartId = request.json['cartId']
 +        result = myCart.delete_one({"orderId":orderId, "cartId" : cartId})
 +        #data = dumps(result)
 +        return jsonify({"Status" : "OK", "data" : "data"})
      except Exception, e:
          return jsonify(status='ERROR',message=str(e))
    
 #method to update the transactions
"""
updateMyOrders : This method updates the orders
    userId:
    cartId:
    amt:

"""
def updateMyOrders(userId, cartId, amt):
    if newQty == 0:
        deleteProduct(userId, cartId)
    else:
        myCart.update_one({"userId":userId, "cartId": cartId},
        {"$set": {"amt":amt} })       

"""
addToMyOrders(userId, cartId)
pprint(myOrders.find_one())
"""

"""
getOrderDetails(cartId)
pprint(findProduct(userId, cartId))
"""

"""
addToMyOrders(userId, cartId)
"""

updateMyOrders(userId, cartId)
