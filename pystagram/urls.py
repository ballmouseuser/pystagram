from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from photos.views import hello
from photos.views import detail
from photos.views import create
from photos.views import signup
from photos.views import memberlist
from django.urls import path
from communityboard.views import *

urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^photos/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^photos/upload/$', create, name='create'),
    url(r'^users/', include('profiles.urls'), name='users'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', auth_views.login, name='login',  kwargs={'template_name': 'login.html'}),
    url(r'^accounts/logout/', auth_views.logout, name='logout', kwargs={'next_page': '/hello/'}),
    url(r'^signup/$', signup, name='signup'),
    url(r'^memberlist/$', memberlist, name='memberlist'),
    path('write/', write, name='write'),
    path('list/', list, name='list'),
    path('view/<int:num>/', view),
]
urlpatterns += static('/upload_files/', document_root=settings.MEDIA_ROOT)

