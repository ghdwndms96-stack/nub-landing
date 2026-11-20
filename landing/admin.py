from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("created", "who", "nick", "pledge", "msg", "hidden")
    list_filter = ("who", "hidden")
    list_editable = ("hidden",)
    search_fields = ("nick", "msg", "pledge")
