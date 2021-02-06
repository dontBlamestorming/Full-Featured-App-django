from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    print("This is Post.object", Post.objects.all())

    # return HttpResponse('<h1>Blog Home</h1>')
    # 템플릿을 '참조'하는 방식으로 렌더링하려는 템플릿 이름
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'


def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title' : 'About'})

'''
    모든 뷰에 동일한 태그가 중복되서 뿌려질 이유가 없다.
    따라서 모든 뷰에 대해 반복되는 html를 만들어야 한다. 가장 좋은 방법은 템플릿을 사용하는 것이다.
    blog -> template -> blog -> template.html
    http 대신에 렌더링된 템플릿을 response할 수 있다.
'''

'''
    Part 10 - Create, Update, and Delete Posts
    지금까지는 함수 기반 View를 사용했지만 class기반 View를 사용해보자.
    클래스 기반 View는 함수기반보다 기본 제공되는 기능이 더 많다.
'''