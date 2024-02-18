# member.py
from db import Database

class MemberManager:
    def __init__(self):
        self.db = Database()
        self.collection = self.db.get_collection("members")

    def get_all_members(self):
        return list(self.collection.find())

    def get_member_by_id(self, member_id):
        return self.collection.find_one({"_id": member_id})

    def add_member(self, member_data):
        return self.collection.insert_one(member_data)

    def update_member(self, member_id, update_data):
        return self.collection.update_one({"_id": member_id}, {"$set": update_data})

    def delete_member(self, member_id):
        return self.collection.delete_one({"_id": member_id})

    def close_connection(self):
        self.db.close_connection()


 
 
 
 
 
 
 
 

