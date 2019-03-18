import pymongo


client = pymongo.MongoClient('localhost', 27017)
mydb = client['avg']
mycol = mydb['games']
x = mycol.find_one()
