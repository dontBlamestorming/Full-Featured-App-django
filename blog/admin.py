from django.contrib import admin
from .models import Post

'''
    관리자 패널을 통해 업데이트를 생성하고 다른 사용자를 삭제하는 방법
    admin 페이지를 보기 위해서 실제로 모델을 등록해야한다.
'''

admin.site.register(Post)


