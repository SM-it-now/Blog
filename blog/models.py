from django.db import models
import os
from django.contrib.auth.models import User

# Create your models here.

# Post 모델의 제목, 내용, 생성일자를 생성하고, created_at과 updated_at을 날짜필드로 받고 auto_now_add 와 auto_now 인자를 추가해서 admin 페이지에서 추가할때 자동 설정되도록 함.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    hook_text = models.CharField(max_length=100, blank=True)
    head_img = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 작성자를 User의 외래기로 설계하고 SET_NULL을 사용해서, 만약 작성자가 탈퇴 및 삭제되더라고 None로 표시되고 포스트는 남아있게 구현.
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)

    # get_absolute_url을 상세페이지 이동 url로 사용하기 위한 함수 구현.
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    # 상세페이지의 file 확장자 명을 출력하기 위한 함수
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    # 상세페이지의 file 확장자를 찾아내는 함수.
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
