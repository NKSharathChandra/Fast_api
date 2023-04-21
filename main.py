from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index():
    return { 'data':{'name':'Sharath'}} 

@app.get('/about')
def about():
    return { 'subject' :{'dept':'cse'}}