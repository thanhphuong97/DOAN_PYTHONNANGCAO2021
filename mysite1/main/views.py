from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm
from django.views import View
from .models import Post
def home(request):
    return render(request,'home.html')

# User Register
def register(request):
    form=UserCreationForm
    if request.method=='POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'Tạo tài khoản thành công')
        else:
            messages.success(request,'Tạo thất bại')
    return render(request,'registration/register.html',{'form':form})


class ClassPost(View):
    def get(self, request):
        post = PostForm
        return render(request, '/comment.html', {'post': post})


def post_view(request):
    if request.method == 'POST':
        context = PostForm(request.POST)
        if context.is_valid():
            context.save()
            return HttpResponse('Da luu')
        else:
            HttpResponse('Chua luu')
    else:
        HttpResponse('Khong co post request')