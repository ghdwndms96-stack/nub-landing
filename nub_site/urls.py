from django.contrib import admin
from django.urls import path
from landing import views

admin.site.site_header = "눕 NUB 관리자"
admin.site.site_title = "눕 NUB"

urlpatterns = [
    path("", views.index, name="index"),
    path("api/posts/", views.posts, name="posts"),
    path("admin/", admin.site.urls),
]
