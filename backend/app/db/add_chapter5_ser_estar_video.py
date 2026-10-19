"""
Add YouTube video section to chapter 5 (SER & ESTAR) in an existing database.
Run: python -m app.db.add_chapter5_ser_estar_video
"""
from app.db.database import SessionLocal
from app.models.chapter import Chapter
from app.models.section import Section

VIDEO_URL = "https://www.youtube.com/watch?v=gZCueT89J6E"
VIDEO_CONTENT = {
    "title": "Βίντεο: SER & ESTAR",
    "youtube_url": VIDEO_URL,
    "description": "Δες την εξήγηση για τη διαφορά μεταξύ SER και ESTAR πριν συνεχίσεις με την κλίση και τους κανόνες.",
}


def add_video():
    db = SessionLocal()

    chapter = db.query(Chapter).filter(Chapter.order_index == 5).first()
    if not chapter:
        print("Chapter 5 (SER & ESTAR) not found. Run seed first.")
        db.close()
        return

    existing = (
        db.query(Section)
        .filter(
            Section.chapter_id == chapter.id,
            Section.type == "video",
        )
        .first()
    )
    if existing:
        print("Video section already exists for chapter 5. Skipping.")
        db.close()
        return

    sections = (
        db.query(Section)
        .filter(Section.chapter_id == chapter.id, Section.order_index >= 2)
        .order_by(Section.order_index.desc())
        .all()
    )
    for section in sections:
        section.order_index += 1

    video = Section(
        chapter_id=chapter.id,
        order_index=2,
        type="video",
        content_json=VIDEO_CONTENT,
    )
    db.add(video)
    db.commit()
    db.close()
    print("Video section added to chapter 5 (SER & ESTAR).")


if __name__ == "__main__":
    add_video()
