""" An example of how to connect to MongoDB """
import sys
from pymongo import MongoClient
import pprint
# from pymongo.errors import ConnectionFailure

def main(): 
  """ Connect to MongoDB """
  try:
    client = MongoClient('localhost', 27017)
    print ("Connected successfully" )
  except ConnectionFailure as e:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)
    sys.exit(1)

  db = client['whosdiary']
  coll = db['log']
  # a = coll.find_one({'text':'hi '})
  # a = coll.find_one({},{'room':1, 'from':1,'to':1,'text':1})
  num =len(coll.distinct("from"))
  print("number of user : " + str(num))
  # pprint.pprint(a)
  # print(coll.find({'text':'hi '}).count())
  # print(coll.find().count())
  





if __name__ == "__main__":
  main()
