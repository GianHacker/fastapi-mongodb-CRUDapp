# Shema helps to serialize & also convert mongodb json to our UI needed json

def studentEntity(db_item) -> dict:
    return{
        "id": str(db_item["_id"]),
        "name": db_item["student_name"],
        #"email": db_item["student_email"],
        "phone": db_item["student_phone"]
    }

def listOfStudentEntities(db_itemList) -> list:
    list_student_Entity = []
    for item in db_itemList:
        list_student_Entity.append(studentEntity(item))
    return list_student_Entity