from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.save, name='save'),
    path('comment/', views.list, name='comment'),
    path('index/', views.index, name='index'),
    path('accounts/register/', views.register, name='register'),
    path('report/', views.ClassPost.as_view(), name='report'),
]

urlpatterns += staticfiles_urlpatterns()
