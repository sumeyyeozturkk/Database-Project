from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.user_profile, name='profile'),
    url(r'^AddProduct/$', views.AddProduct, name='AddProduct'),
]
urlpatterns += staticfiles_urlpatterns()