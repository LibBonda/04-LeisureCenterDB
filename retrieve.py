# retrieve document/s
def retrieve_all(collection):
    return list(collection.find())

def retrieve_one(collection, query):
    return collection.find_one(query)




 
 
 
 
 
 
 
 

