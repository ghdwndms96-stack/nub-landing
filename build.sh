#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
# 관리자 계정: Render 환경변수 DJANGO_SUPERUSER_USERNAME / _PASSWORD / _EMAIL 이 있으면 처음 한 번 만들어짐
if [ -n "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser --no-input || true
fi
