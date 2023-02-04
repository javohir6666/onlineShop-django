from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from .models import CustomUser
from django.views import View
from django.shortcuts import get_object_or_404


def add_user_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username")


        try:
            user = CustomUser.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                email=email,
            )
            user.save()
            messages.success(request, "Registration successfully. You can login now!")
            return HttpResponseRedirect("/users/login")
        except:
            messages.error(request, "Failed to Register")
            return HttpResponseRedirect("/users/login")
        
def logOut(request):
    logout(request)
    return redirect('login')

class ProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        online = timezone.now()
        if user.last_login == online:
            online = str("online")
        else:
            online = str("online")
        return render(request, 'pages/profile.html', {"customuser": user,
                                                      'online': online})
        
class UpdateProfileView(View, LoginRequiredMixin):
    login_url = 'login'
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            username = request.POST.get("username")


            try:
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email = email
                user.password = password
                user.save()
                
                messages.success(request, "Account has been updated!")
                return HttpResponseRedirect(f"/users/profile/{request.user}")
            except:
                messages.error(request, "Failed to updating account")
                return HttpResponseRedirect(f"/users/profile/{request.user}")
        return render(request, 'pages/update_profile.html',{'user': user})