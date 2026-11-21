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


PRICES = [("u10", "1만 원 미만"), ("10-15", "1만~1.5만 원"), ("15-20", "1.5만~2만 원"), ("20+", "2만 원 이상")]
FOR_WHOM = [("me", "나를 위해"), ("kid", "아이·조카에게"), ("gift", "친구·연인 선물"), ("souvenir", "제주 기념품")]
WHO_AM = [("student", "대학생"), ("worker", "직장인"), ("teacher", "교사·교육자"), ("etc", "기타")]


class Survey(models.Model):
    fav = models.CharField("마음에 드는 친구", max_length=10, choices=FRIENDS)
    price = models.CharField("적정 가격", max_length=10, choices=PRICES)
    for_whom = models.CharField("누구를 위해", max_length=10, choices=FOR_WHOM)
    who_am = models.CharField("응답자", max_length=10, choices=WHO_AM)
    major = models.CharField("전공·직업", max_length=40, blank=True)
    kit_interest = models.BooleanField("교육키트 관심", default=False)
    comment = models.CharField("한마디", max_length=300, blank=True)
    created = models.DateTimeField("응답 시각", auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "성인 설문 응답"
        verbose_name_plural = "성인 설문 응답"

    def __str__(self):
        return f"{self.get_who_am_display()} · {self.get_fav_display()} · {self.get_price_display()}"
