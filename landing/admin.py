import csv
from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone
from .models import Post


@admin.action(description="선택한 응원 메시지를 엑셀(CSV)로 내려받기")
def export_csv(modeladmin, request, queryset):
    now = timezone.localtime().strftime("%Y%m%d-%H%M")
    resp = HttpResponse(content_type="text/csv; charset=utf-8")
    resp["Content-Disposition"] = f'attachment; filename="nub-cheers-{now}.csv"'
    resp.write("﻿")  # 엑셀에서 한글이 깨지지 않도록
    w = csv.writer(resp)
    w.writerow(["번호", "날짜", "시간", "응원한 친구", "닉네임", "실천 약속", "응원 메시지", "숨김"])
    for p in queryset.order_by("created"):
        t = timezone.localtime(p.created)  # 한국 시간
        w.writerow([p.id, t.strftime("%Y-%m-%d"), t.strftime("%H:%M:%S"),
                    p.get_who_display(), p.nick, p.pledge, p.msg, "예" if p.hidden else ""])
    return resp


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("created", "who", "nick", "pledge", "msg", "hidden")
    list_filter = ("who", "hidden", "created")
    list_editable = ("hidden",)
    search_fields = ("nick", "msg", "pledge")
    date_hierarchy = "created"
    actions = [export_csv]
    list_per_page = 100
