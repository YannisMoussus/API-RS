from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_post(
    post: _schemas.CreatePost, db: "Session"
) -> _schemas.Post:
    post = _models.Post(**post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return _schemas.Post.from_orm(post)


async def get_all_posts(db: "Session") -> List[_schemas.Post]:
    posts = db.query(_models.Post).all()
    return list(map(_schemas.Post.from_orm, posts))


async def get_post(post_id: int, db: "Session"):
    post = db.query(_models.Post).filter(_models.Post.id == post_id).first()
    return post


async def delete_post(post: _models.Post, db: "Session"):
    db.delete(post)
    db.commit()


async def update_post(
    post_data: _schemas.CreatePost, post: _models.Post, db: "Session"
) -> _schemas.Post:
    post.text = post_data.text
    post.like = post_data.like
    post.share = post_data.share
    post.comment = post_data.comment
    post.username = post_data.username

    db.commit()
    db.refresh(post)

    return _schemas.Post.from_orm(post)