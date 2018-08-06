from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Photo
from .forms import PhotoForm
from .forms import SignupForm


def hello(request):
    return render(request, 'main.html')

def detail(request, pk):
    # photo = Photo.objects.get(pk=pk)
    photo = get_object_or_404(Photo, pk=pk)
    messages = (
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),
    )
    return HttpResponse('\n'.join(messages))


@login_required
def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            return redirect(obj)

    ctx = {
        'form': form,
    }
    return render(request, 'edit.html', ctx)

def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        # 유효성 검증에 통과한 경우 (username의 중복과 password1, 2의 일치 여부)
        if signup_form.is_valid():
            # SignupForm의 인스턴스 메서드인 signup() 실행, 유저 생성
            signup_form.signup()
            return redirect('/hello/')
    else:
        signup_form = SignupForm()

    context = {
        'signup_form': signup_form,
    }
    return render(request, 'signup.html', context)

def memberlist(request):
    members = User.objects.all()
    context = {
        'members': members
    }
    return render(request, 'memberlist.html', context)

