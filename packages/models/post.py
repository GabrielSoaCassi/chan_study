from sqlmodel import Field, Relationship, SQLModel
from packages.models.thread import Thread
from datetime import datetime


class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    thread_id: int = Field(foreign_key="threads.id")
    content: str = Field(nullable=False)
    created_at: datetime|None = Field(default=datetime.now)
    thread: Thread = Relationship(back_populates="posts")

    def __init__(self, thread_id: int, content: str):
        self.thread_id = thread_id
        self.content = content

    def to_dict(self) -> dict:
        return {"content": self.content, "created_at": self.created_at}
