from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()

@app.get('/')
def index():
    return { 'data':'blog list'} 

@app.get('/blog')
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} blogs from the db'}
    else:
        return {'data' : 'all the blogs'}
    
@app.get('/blog/unpublished')
def unpublished():
    return {'data':'unpublished'}


@app.get('/blog/{id}')
def show(id:int):
        return { 'data': id}

@app.get('/blog/{id}/comments')
def comments(id:int):
    if(id==1):
      return {'data':{'comment1','comment2' }}
    elif(id==2):
       return {'data':{'comment3','comment4'}}
    else:
        return {'data':'other comments'}
    

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {f"Thsi is the blog created with title {blog.title}"}

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
    


         