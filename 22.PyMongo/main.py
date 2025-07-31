import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://rbsinh:Bhargav123@cluster0.mt6yj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db=cluster["test"]
collection=db["test"]
post = {"_id": 0,"name":"tim","score":5}
collection.insert_one(post)
collection.insert_many([post1,post2])

results=collection.find({"_id":"5"})
# results =collection.find_one({"_id":0})
# results =collection.find({})
print(results)

for result in results:
    print(result["_id"])

results=collection.delete_one({"_id":0})
results=collection.delete_many({}) ##Delete everything

results =collection.update_one({"_id":5},{"$set":{"name":"tim"} })
