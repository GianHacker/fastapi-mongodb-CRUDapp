# Import statement for importing required modules / classes
from fastapi import FastAPI
from routes.students import student_router


# Create app
app = FastAPI()

#register the router
app.include_router(student_router)

