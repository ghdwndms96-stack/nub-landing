#!/usr/bin/env bash
# 실행 단계: DB가 준비될 때까지 기다렸다가 테이블을 만들고 서버를 켬
set -o errexit
for i in $(seq 1 10); do
  python manage.py migrate --no-input && break
  echo "DB 연결 대기 중... ($i/10)"; sleep 6
done
if [ -n "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser --no-input >/dev/null 2>&1 || true
fi
exec gunicorn nub_site.wsgi:application
