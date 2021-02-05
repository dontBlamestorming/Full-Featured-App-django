from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

'''
    from django.contrib.auth.forms import UserCreationForm
    UserCreationForm - 유효성 검사 제공
    1. 적절한 정보를 입력했는가?
    2. 기입한 2개의 암호가 일치하는가?
    3. 이미 존재하는 아이디를 입력하지는 않았는가(admin을 조회하는 듯)?
    
    from django.contrib.auth.decorators import login_required
    1. url를 통해 부적절한 페이지 이동
    2. 로그인 한 후 profile/로 이동하게 만들기 위한 모듈
'''

def register(request):
    '''
        1. POST 방식으로 브라우저가 요청을 보내면, User가 만든 form이 'form'에 저장
        2. django에서 제공하는 템플릿(html)에 유효한 값인 경우(if문)
        3. 'form.save()'를 통해 admin에 저장
        4. 유효한 값중 username을 추출하여 success method에 요청과 텍스트를 넘기고
        5. 홈으로 rediect
    '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            messages.success(request, f'Your account has been created! You are now able to log in')
            # return redirect('blog-home') # home.html은 base.html에 상속(?)
            return redirect('login')
    else:
        form = UserRegisterForm()   # 처음 방문시에는 여기가 읽히겠지
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

'''
    messages 에러에 사용할 수 있는 method
    messages.debug
    messages.info
    messages.success
    messages.warning
    messages.error
'''