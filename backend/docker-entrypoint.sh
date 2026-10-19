#!/bin/sh
set -e

python -m app.db.seed_data
python -m app.db.seed_chapters_6_10
python -m app.db.seed_chapters_11_15
python -m app.db.add_chapter2_numbers_video
python -m app.db.add_chapter4_family_video
python -m app.db.add_chapter5_ser_estar_video

exec uvicorn app.main:app --host 0.0.0.0 --port 8000
