from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView
from django.contrib.auth.mixins import LoginRequiredMixin

# register a new user
def base(req):
    print(req.user)
    print(req.user.is_authenticated)
    return render(req,"first_page.html")


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			# login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,"register/register.html", context={"register_form":form})


#login class

class MyLoginView(LoginView):
    template_name = 'register/login.html'

class MyLogoutView(LoginRequiredMixin,LogoutView):
    template_name = "register/logout.html"

class MyPasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    template_name = "register/changepass.html"
    success_url = "/changepassdone/"


class MyPasswordChangeDoneView(LoginRequiredMixin,PasswordChangeDoneView):
    template_name = "register/changepassdone.html"



class MyPasswordResetView(PasswordResetView):
    template_name = "register/Passwordresetview.html"
    success_url = reverse_lazy('password_reset_done')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name="register/prconfirmdone.html"


def detail_user(req):
    us = User.objects.all()
    print(us)
    return HttpResponse("helllo")

def profile(req):
    if req.user.is_authenticated:
        print(req.user)
        u= User.objects.get(username=req.user)
        user = req.user
        full_name = user.get_full_name()
        # print(full_name)
        gps = user.groups.all()
        return render(req,'register/profile.html',{'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')