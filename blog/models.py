from django.db import models

# Create your models here.

# Post 모델의 제목, 내용, 생성일자를 생성하고, created_at과 updated_at을 날짜필드로 받고 auto_now_add 와 auto_now 인자를 추가해서 admin 페이지에서 추가할때 자동 설정되도록 함.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title