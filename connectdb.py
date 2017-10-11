""" An example of how to connect to MongoDB """
import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main(): 
  """ Connect to MongoDB """
  try:
    client = MongoClient('localhost', 27017)
    print ("Connected successfully" )
  except ConnectionFailure as e:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)
    sys.exit(1)

# Getting a Database
  # db = client.test_database
  db = client['test-database']
# Getting a Collection = table
  coll = db['coll']

  post = {"author": "Mike",
          "text": "My first blog post!",
          "tags": ["mongodb", "python", "pymongo"],}
# Inserting a Document
  posts = db.posts2
  post_id = posts.insert_one(post).inserted_id
  print (post_id, db.collection_names(include_system_collections=False))
  print ('all the text',posts.find_one())


if __name__ == "__main__":
  main()
