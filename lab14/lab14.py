import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://test_dbuser:YlqlJdJ0l3Jb5Jwv@cluster0.xfdev1b.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test_database"]
collection = db["test_collection"]

#se numesc posts/documents
post0 = {"_id": 0, "name": "Andrew","age":20}
post1 = {"_id": 1, "name": "Ben","age":21}
post2 = {"_id": 2, "name": "Coral","age":22}
post3 = {"_id": 3, "name": "Darius","age":23} 
post4 = {"_id": 4, "name": "Eustachio","age":24}
post5 = {"_id": 5, "name": "Florin","age":25} 
post6 = {"_id": 6, "name": "Garry","age":26}
post7 = {"_id": 7, "name": "Marius","age":27}   
post8 = {"_id": 8, "name": "Terry","age":28}
post9 = {"_id": 9, "name": "Joseph","age":29} 

collection.insert_many([post0,post1,post2,post3,post4,post5,post6,post7,post8,post9])

#collection.insert_one(post4)


#results = collection.delete_one({"_id":3})  #detele the post where id = 4
#results = collection.delete_many({}) #to delete all posts

#results = collection.update_one({"_id":4}, {"$set":{"name":"Margareta"}})

#pt a afisa tot 
results = collection.find({})
for x in results:
     print(x)

#results = collection.delete_one({"_id":3})  #detele the post where id = 4
#results = collection.delete_many({}) #to delete all posts

#results = collection.update_one({"_id":4}, {"$set":{"name":"Margareta"}})

#post_count = collection.count_documents({})  #prints the number of documents/posts
#print(post_count)

