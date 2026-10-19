from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.chapter import Chapter
from app.models.section import Section
from app.schemas.chapter import ChapterListItem, ChapterDetail, SectionOut

router = APIRouter(prefix="/api/chapters", tags=["chapters"])


@router.get("", response_model=list[ChapterListItem])
def list_chapters(db: Session = Depends(get_db)):
    chapters = db.query(Chapter).filter(Chapter.is_published == True).order_by(Chapter.order_index).all()
    result = []
    for ch in chapters:
        item = ChapterListItem(
            id=ch.id,
            order_index=ch.order_index,
            title_greek=ch.title_greek,
            title_spanish=ch.title_spanish,
            difficulty_level=ch.difficulty_level,
            is_published=ch.is_published,
            section_count=len(ch.sections),
        )
        result.append(item)
    return result


@router.get("/{chapter_id}", response_model=ChapterDetail)
def get_chapter(chapter_id: int, db: Session = Depends(get_db)):
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Το κεφάλαιο δεν βρέθηκε")
    return chapter


@router.get("/{chapter_id}/sections", response_model=list[SectionOut])
def get_chapter_sections(chapter_id: int, db: Session = Depends(get_db)):
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Το κεφάλαιο δεν βρέθηκε")
    sections = (
        db.query(Section)
        .filter(Section.chapter_id == chapter_id)
        .order_by(Section.order_index)
        .all()
    )
    return sections
