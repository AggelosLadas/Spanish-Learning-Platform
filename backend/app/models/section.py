from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db.database import Base


class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=False)
    order_index = Column(Integer, nullable=False)
    type = Column(String, nullable=False)  # "text", "vocab", "example", "grammar", "tip", "video"
    content_json = Column(JSON, nullable=False)

    chapter = relationship("Chapter", back_populates="sections")
