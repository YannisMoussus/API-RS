import datetime as _dt
import sqlalchemy as _sql

import database as _database


class Post(_database.Base):
    __tablename__ = "posts"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    text = _sql.Column(_sql.String, index=True)
    like = _sql.Column(_sql.String, index=True)
    share = _sql.Column(_sql.String, index=True)
    comment = _sql.Column(_sql.String, index=True)
    username = _sql.Column(_sql.String, index=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)