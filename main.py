# main.py
from db import connect_to_db
from retrieve import retrieve_all, retrieve_one
from addDoc import add_one, add_many
from update import update_one, update_many
from delete import delete_one, delete_many

def main():
    db = connect_to_db()
    members_collection = db["members"]
    course_collection = db["course"]
    lesson_collection = db["lesson"]

    while True:
        print("\nOptions:")
        print("1. Retrieve all documents")
        print("2. Retrieve a single document")
        print("3. Print all documents")
        print("4. Print a single document")
        print("5. Loop through multiple documents")
        print("6. Add a single document")
        print("7. Add multiple documents")
        print("8. Update a single document")
        print("9. Update multiple documents")
        print("10. Delete a document")
        print("11. Delete multiple documents")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(retrieve_all(members_collection))
        elif choice == '2':
            query = {"_id": input("Enter document ID: ")}
            print(retrieve_one(members_collection, query))
        elif choice == '3':
            print(retrieve_all(course_collection))
        elif choice == '4':
            query = {"CourseID": int(input("Enter CourseID: ")), "MemberID": int(input("Enter MemberID: "))}
            # query = {"_id": input("Enter document ID: ")}
            print(retrieve_one(lesson_collection, query))
        elif choice == '5':
            for doc in retrieve_all(members_collection):
                print(doc)
        elif choice == '6':
            data = {"CourseID": int(input("Enter CourseID: ")), "MemberID": int(input("Enter MemberID: "))}
            print(add_one(course_collection, data))
        elif choice == '7':
            data = [
                {"CourseID": 11, "MemberID": 51},
                {"CourseID": 22, "MemberID": 52},
                {"CourseID": 33, "MemberID": 53},
                {"CourseID": 44, "MemberID": 54}
            ]
            print(add_many(course_collection, data))
        elif choice == '8':
            query = {"CourseID": int(input("Enter CourseID to update: "))}
            update = {"$set": {"MemberID": int(input("Enter new MemberID: "))}}
            print(update_one(course_collection, query, update))
        elif choice == '9':
            query = {"MemberID": int(input("Enter MemberID to update: "))}
            update = {"$set": {"CourseID": int(input("Enter new CourseID: "))}}
            print(update_many(course_collection, query, update))
        elif choice == '10':
            query = {"CourseID": int(input("Enter CourseID: ")), "MemberID": int(input("Enter MemberID: "))}
            # query = {"_id": input("Enter document ID to delete: ")}
            print(delete_one(course_collection, query))
        elif choice == '11':
            query = {"MemberID": int(input("Enter MemberID to delete: "))}
            print(delete_many(course_collection, query))
        elif choice == '12':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 12.")

if __name__ == "__main__":
    main()




 
 
 
 
 
 
 
 

