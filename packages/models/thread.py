# models.py
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime


class Thread(SQLModel, table=True):
    __tablename__ = "threads"
    id: int | None = Field(default=None, primary_key=True, index=True)
    title: str = Field(nullable=False)
    created_at: datetime|None = Field(default=datetime.now)
    posts: list["Post"] | None = Relationship(back_populates="thread")

    def __init__(self, title: str):
        self.title = title

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "created_at": self.created_at,
        }
