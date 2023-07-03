from sqlalchemy import Boolean, Column, ForeignKey, Integer, MetaData, String, Table

from src.auth.models import user
from src.database import Base

metadata = MetaData()

post = Table(
    "post",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("text", String, nullable=True),
    Column("views", Integer, default=0),
    Column("user_id", Integer, ForeignKey(user.c.id)),
)

user_post = Table(
    "user_post",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("post_id", Integer, ForeignKey(post.c.id)),
    Column("like", Boolean, nullable=False),
)


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=True)
    views = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey(user.c.id))


class UserPost(Base):
    __tablename__ = "user_post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(user.c.id))
    post_id = Column(Integer, ForeignKey(post.c.id))
    like = Column(Boolean, nullable=False)
