from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import UserProfile
from .forms import UserForm
from django.contrib import admin

# Create your views here.

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect("/admin/bbs")
            else:
                return render(request, 'accounts/login.html',{'error_message':'用户没有激活,联系管理员'})
        else:
            return render(request, 'accounts/login.html',{'error_message':'用户名或密码错误'})
    else:
        return render(request,'accounts/login.html')

def custom_register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        # 如果数据合法保存到user
        user = form.save(commit=False)
        print(form.cleaned_data)
        user.set_password(form.cleaned_data['password'])
        user.save()

        #同步保存到profile
        profile = UserProfile()
        profile.user = user
        profile.save()
        login(request, user)
        return render(request,'accounts/login.html')
    context = {

        "form": form
    }
    return render(request, 'accounts/register.html', context)

def custom_logout(request):
    logout(request)
    return redirect('accounts:login')

"""data:<QueryDict: {'csrfmiddlewaretoken': ['eIPZDw8bZkvPJPkJcyB8p7oNH9Aw8YfZqTztmluY0LU2QZTpoAYk2m27x84vWo0V'], 'username': ['simp'], 'email': ['1286490880@qq.com'], 'phoneNumber': ['1286490880'], 'gridRadios': ['1']}>----f:<MultiValueDict: {'picture': [<InMemoryUploadedFile: 微信图片_201811052
10714.jpg (image/jpeg)>]}>
"""

@login_required
def update_userprofile(request):
    try:
        if request.method == 'POST':
            #获取数据
            data = request.POST
            f = request.FILES

            # print(f'data:{data}----f:{f}')
            user = User.objects.get(username=data['username'])
            # print(f'user:{dir(user)}')
            profile = UserProfile.objects.get(user=user)
            # form = UserForm()
            # user1 = UserForm.objects.get(username=user)
            
            if profile:
                user.email =data['email']
                # print(dir(profile))
                # profile.email = data['email']
                # print( data['email'])
                profile.sex = data['gridRadios']
                # print(data['gridRadios'])
                profile.phone_number = data['phoneNumber']

                # print(data['phoneNumber'])
                profile.picture = f['picture']
                # print(f'profile.email{profile.email}')
                # print(f'profile.sex{profile.sex}')
                # print(f'profile.phone_number{profile.phone_number}')
                profile.save()
                user.save()
    except Exception as e:
        print(e)
        print("这里有异常了")

    return redirect('bbs:my_page')