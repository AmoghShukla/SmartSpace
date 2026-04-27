from fastapi import FastAPI


app = FastAPI(title="SmartSpace : Workspace ooking & Resource Management API")


@app.get('/')
def home():
    return {
        'message' : 'SmartSpace Application is up and running!!!'
    }