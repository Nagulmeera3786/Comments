from sqlalchemy.orm import Session
import models, schemas

def get_comments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comment).offset(skip).limit(limit).all()

def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(task=comment.task, text=comment.text)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def update_comment(db: Session, comment_id: int, comment: schemas.CommentCreate):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not db_comment:
        raise Exception("Comment not found")
    db_comment.task = comment.task
    db_comment.text = comment.text
    db.commit()
    db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not db_comment:
        raise Exception("Comment not found")
    db.delete(db_comment)
    db.commit()
