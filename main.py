from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.post("/api/posts/", response_model=_schemas.Post)
async def create_post(
    post: _schemas.CreatePost,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_post(post=post, db=db)


@app.get("/api/posts/", response_model=List[_schemas.Post])
async def get_posts(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_posts(db=db)


@app.get("/api/posts/{post_id}/", response_model=_schemas.Post)
async def get_post(
    post_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    post = await _services.get_post(db=db, post_id=post_id)
    if post is None:
        raise _fastapi.HTTPException(status_code=404, detail="Post does not exist")

    return post


@app.delete("/api/posts/{post_id}/")
async def delete_post(
    post_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    post = await _services.get_post(db=db, post_id=post_id)
    if post is None:
        raise _fastapi.HTTPException(status_code=404, detail="Post does not exist")

    await _services.delete_post(post, db=db)

    return "successfully deleted the post"


@app.put("/api/posts/{post_id}/", response_model=_schemas.Post)
async def update_post(
    post_id: int,
    post_data: _schemas.CreatePost,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    post = await _services.get_post(db=db, post_id=post_id)
    if post is None:
        raise _fastapi.HTTPException(status_code=404, detail="Post does not exist")

    return await _services.update_post(
        post_data=post_data, post=post, db=db
    )