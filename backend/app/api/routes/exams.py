from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.exam import Exam
from app.models.question import Question
from app.schemas.exam import ExamOut

router = APIRouter(prefix="/api/exams", tags=["exams"])


@router.get("/{chapter_id}", response_model=ExamOut)
def get_exam(chapter_id: int, db: Session = Depends(get_db)):
    exam = db.query(Exam).filter(Exam.chapter_id == chapter_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Η εξέταση δεν βρέθηκε")

    questions = (
        db.query(Question)
        .filter(Question.chapter_id == chapter_id)
        .all()
    )

    return ExamOut(
        id=exam.id,
        chapter_id=exam.chapter_id,
        title=exam.title,
        passing_score_pct=exam.passing_score_pct,
        questions=questions,
    )
