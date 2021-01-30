from django.urls import path
from . import views

urlpatterns = [
    # url을 매핑하는데 있어서 정규표현식은 복잡하기 때문에 사용하지 않는 것이 좋다
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]