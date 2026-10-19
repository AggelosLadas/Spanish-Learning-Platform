from pydantic import BaseModel
from datetime import datetime


class SectionOut(BaseModel):
    id: int
    chapter_id: int
    order_index: int
    type: str
    content_json: dict | list

    class Config:
        from_attributes = True


class ChapterListItem(BaseModel):
    id: int
    order_index: int
    title_greek: str
    title_spanish: str
    difficulty_level: str
    is_published: bool
    section_count: int = 0

    class Config:
        from_attributes = True


class ChapterDetail(BaseModel):
    id: int
    order_index: int
    title_greek: str
    title_spanish: str
    difficulty_level: str
    is_published: bool
    created_at: datetime | None = None
    sections: list[SectionOut] = []

    class Config:
        from_attributes = True
