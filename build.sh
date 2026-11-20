#!/usr/bin/env bash
# 빌드 단계: 패키지 설치와 정적 파일 모으기만 (DB는 아직 연결하지 않음)
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
