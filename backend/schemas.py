from pydantic import BaseModel

class CommentCreate(BaseModel):
    task: str
    text: str

class Comment(CommentCreate):
    id: int

    class Config:
        from_attributes = True  # fix for Pydantic v2 warning
