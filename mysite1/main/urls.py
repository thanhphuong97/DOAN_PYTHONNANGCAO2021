from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('accounts/register/',views.register,name='register'),
    path('commment/', views.ClassPost.as_view(), name='comment'),

]