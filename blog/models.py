from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

'''
    ORM(Object Relational Mapping)
    - 코드의 객체를 작성, 수정하면서 DB의 테이블을 컨트롤할 수 있게 한다.
'''

class Post(models.Model):   # 각 클래스는 DB에서 자체 테이블이 될 것
    title = models.CharField(max_length=100)
    content = models.TextField()    # max_length를 설정할 필요 없음
    # date_posted = models.DateTimeField(auto_now_add=True) 게시물이 Add된 시점이 기준이 될 것 - 정적
    date_posted = models.DateTimeField(default=timezone.now)
    # 게시물이 Add된 시점이 기준이 될 것 + 내가 원하는 경우 날짜를 변경하는 옵션 추가할 것 - 동적
    # Q - timezone.now와 timezone.now()의 차이가 무엇인지?
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Q - on_delete가 왜 필요한지 이해못하였음

    def __str__(self):
        return self.title



