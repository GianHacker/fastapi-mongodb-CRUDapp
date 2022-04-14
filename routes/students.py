#import statements
from fastapi import APIRouter
from models.students import Student
from config.database import connection
from schemas.students import studentEntity, listOfStudentEntities
from bson import ObjectId


student_router = APIRouter()


# Getting all Students
@student_router.get("/students")
async def findAllStudents():
    return listOfStudentEntities(connection.local.student.find())

# Get a single student with the matching ID
@student_router.get("/student/{studentId}")
async def find_student_byID(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

# Creating a student
@student_router.post("/student")
async def createStudent(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntities(connection.local.student.find())

# Update a student with the matching Id
@student_router.put("/student/{studentId}")
async def update_student(studentId, student: Student):
    # find the student and then update it with new student data
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set":dict(student)}
    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

# Delete a student with the help of Id
@student_router.delete("/student/{studentId}")
async def delete_student(studentId):
    # find the student and then delete it and also returns the same student object
    connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)})
    return "Deleted the student details for the selected ID" #studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))



    
