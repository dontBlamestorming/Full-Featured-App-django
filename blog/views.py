from django.shortcuts import render

# MVC 패턴으로 앱 개발을 할 것으로 보인다.

# 테스트용 첫번째 게시물 데이터 더미
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    # 템플릿을 '참조'하는 방식으로 렌더링하려는 템플릿 이름
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title' : 'About'})


# 모든 뷰에 동일한 태그가 중복되서 뿌려질 이유가 없다.
# 따라서 모든 뷰에 대해 반복되는 html를 만들어야 한다. 가장 좋은 방법은 템플릿을 사용하는 것이다.
# blog -> template -> blog -> template.html
# http 대신에 렌더링된 템플릿을 response할 수 있다.