from django.shortcuts import render, redirect
from .models import Article
from .forms import Form

def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()  # 데이터베이스에 저장
            return redirect('/list')

    else:
        form = Form()
    # 디스패치 작업
    return render(request, 'write.html', {'form': form})


def list(request):
    articleList = Article.objects.all().order_by('-cdate')
    loginuser = str(request.user)

    eq_str = ''
    if loginuser != 'AnonymousUser':
        eq_str = 'true'

    ctx = {
        'articleList': articleList,
        'eq_str': eq_str
    }
    return render(request, 'list.html', ctx)


def view(request, num=1):
    article = Article.objects.get(id=num)
    return render(request, 'view.html', {'article': article})