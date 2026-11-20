import json
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from .models import Post, FRIENDS

WHO = {k for k, _ in FRIENDS}
WAIT_SECONDS = 20  # 같은 사람이 연달아 도배하지 못하게


@ensure_csrf_cookie
def index(request):
    return render(request, "landing/index.html")


def _client_ip(request):
    fwd = request.META.get("HTTP_X_FORWARDED_FOR", "")
    return fwd.split(",")[0].strip() if fwd else request.META.get("REMOTE_ADDR", "")


@require_http_methods(["GET", "POST"])
def posts(request):
    if request.method == "GET":
        qs = Post.objects.filter(hidden=False)
        counts = {k: 0 for k in WHO}
        for w in qs.values_list("who", flat=True):
            counts[w] = counts.get(w, 0) + 1
        items = [{"id": p.id, "nick": p.nick, "who": p.who, "pledge": p.pledge,
                  "msg": p.msg, "t": int(p.created.timestamp() * 1000)}
                 for p in qs[:100]]
        return JsonResponse({"posts": items, "counts": counts})

    try:
        data = json.loads(request.body or b"{}")
    except ValueError:
        return JsonResponse({"error": "잘못된 요청이에요"}, status=400)
    if data.get("website"):  # 사람에게는 보이지 않는 칸(스팸 봇 차단)
        return JsonResponse({"ok": True})
    who = str(data.get("who", ""))
    pledge = str(data.get("pledge", "")).strip()[:40]
    msg = str(data.get("msg", "")).strip()[:300]
    nick = str(data.get("nick", "")).strip()[:16] or "익명"
    if who not in WHO or not pledge or not msg:
        return JsonResponse({"error": "친구, 약속, 응원 한마디를 모두 채워 주세요"}, status=400)
    key = "post-wait:" + _client_ip(request)
    if cache.get(key):
        return JsonResponse({"error": "조금만 기다렸다가 다시 남겨 주세요"}, status=429)
    cache.set(key, 1, WAIT_SECONDS)
    Post.objects.create(nick=nick, who=who, pledge=pledge, msg=msg)
    return JsonResponse({"ok": True}, status=201)
