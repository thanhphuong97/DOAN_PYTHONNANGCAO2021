from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.views import View
from .models import Post


def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


# User Register
def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        regForm = UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request, 'Tạo tài khoản thành công')
        else:
            messages.success(request, 'Tạo thất bại')
    return render(request, 'registration/register.html', {'form': form})


class ClassPost(View):
    def get(self, request):
        post = PostForm
        return render(request, './reports/report.html', {'post': post})


def list(request):
    list = Post.objects.all()
    context = {'list': list}
    return render(request, "./reports/conment.html", context)


def save(request):
    if request.method == 'POST':
        context = PostForm(request.POST)
        if context.is_valid():
            context.save()
            return HttpResponse('Đóng góp của bạn đã được gửi thành công đến chúng tôi. Rẩt cảm ơn bạn!')
        else:
            HttpResponse('Chua luu')
    else:
        HttpResponse('Khong co post request')
