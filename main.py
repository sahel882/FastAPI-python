from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message: 'Hello from API'"}

@app.get("/posts")
def get_posts():
    return {"Getting posts I see"}

@app.post("/createPost")
def create_post(post: Post):
    print(post.model_dump())
    print(post.published)
    return {"data": post}