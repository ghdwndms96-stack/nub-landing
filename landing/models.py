from django.db import models

FRIENDS = [
    ("nanubo", "나눕오"), ("pin", "핀"), ("gurbang", "구르방"),
    ("seo", "세오"), ("bibi", "비비"), ("mong", "몽이"),
]


class Post(models.Model):
    nick = models.CharField("닉네임", max_length=16, default="익명")
    who = models.CharField("응원한 친구", max_length=10, choices=FRIENDS)
    pledge = models.CharField("실천 약속", max_length=40)
    msg = models.CharField("응원 메시지", max_length=300)
    created = models.DateTimeField("작성 시각", auto_now_add=True)
    hidden = models.BooleanField("숨김", default=False,
                                 help_text="체크하면 페이지에서 보이지 않아요")

    class Meta:
        ordering = ["-created"]
        verbose_name = "응원 메시지"
        verbose_name_plural = "응원 메시지"

    def __str__(self):
        return f"{self.nick} → {self.get_who_display()}: {self.msg[:20]}"
