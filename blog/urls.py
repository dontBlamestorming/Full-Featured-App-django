from django.urls import path
from . import views
from .views import PostListView

# url을 매핑하는데 있어서 정규표현식은 복잡하기 때문에 사용하지 않는 것이 좋다
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    # -> blog/post_list.html을 찾고있다
    # <app>/<model>_<viewtype>.html
    path('about/', views.about, name='blog-about'),
]
