from fastapi import FastAPI #Imports the FastAPI module

app = FastAPI()  #Creates app object to handle all API routes and requests

@app.get("/")         #Defines GET route at /
def read_root():        #Function read_root handles request
    return {"message": "Hello Shoaib"}       #Returns JSON response  

@app.get("/about")
def read_about():
    return {"message": "My name is Shoby"}
