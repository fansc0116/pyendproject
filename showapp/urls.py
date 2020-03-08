from django.urls import path
from showapp import views

app_name='showapp'

urlpatterns =[
    path('index/',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('get_code/',views.get_code,name='get_code'),
    path('check_user/',views.check_user,name='check_user'),
    path('add_banner/',views.add_banner,name='add_banner'),
    path('loadbanner/',views.loadbanner,name='loadbanner'),
    path('del_banner/',views.del_banner,name='del_banner'),
    path('loadusers/',views.loadusers,name='loadusers'),
    path('add_user/',views.add_user,name='add_user'),
    path('del_user/',views.del_user,name='del_user'),
]