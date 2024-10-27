from django.urls import path
from app import views
urlpatterns=[
    path('',views.home,name='homepage'),
    path('register',views.register,name='registerpage'),
    path('login',views.loginv,name='loginpage'),
    path('profile',views.profile,name='profilepage'),
    path('update',views.update,name='updatepage'),
    path('logout',views.logoutv,name='logoutpage'),
    path('create',views.create,name='createpage'),
    path('tweet',views.mytweetview,name='mytweetpage'),
    path('delete/<int:rid>',views.delete,name='deletepage'),
    
    
]