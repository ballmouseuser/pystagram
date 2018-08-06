from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


def profile(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    name1 = user.username
    name2 = request.user
    name2 = str(name2)

    content = '';

    if name1 == name2:
        content = 'true'

    ctx = {
        'user': user,
        'eq_ctx': content
    }

    return render(request, 'profile.html', ctx)

