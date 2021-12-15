import datetime as _dt
import pydantic as _pydantic


class _BasePost(_pydantic.BaseModel):
    text: str
    like: str
    share: str
    comment: str
    username: str


class Post(_BasePost):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True


class CreatePost(_BasePost):
    pass