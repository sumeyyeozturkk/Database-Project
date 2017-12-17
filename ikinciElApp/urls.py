from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.user_profile, name='profile'),
    url(r'^AddProduct/$', views.AddProduct, name='AddProduct'),
    url(r'^product/$', views.product_list, name = 'product'),
    url(r'^basket/$',views.basket_list, name ='basket'),
    url(r'^basket/(?P<id>[0-9]+)$',views.addToBasket, name ='basket'),
    url(r'^buy/(?P<id>[0-9]+)$',views.buy_product, name ='buy'),
    url(r'^pdf/(?P<id>[0-9]+)$',views.write_pdf_product, name ='pdf'),
    url(r'^pdf2/$',views.write_pdf_user, name ='pdf2'),
    url(r'^profile_list/$', views.user_profile_list, name = 'profile_list'),



]
urlpatterns += staticfiles_urlpatterns()