from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from accounts.forms import SignUpForm
from django.views.generic import TemplateView
from django.contrib.auth import logout

# Create your views here.

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "로그인 페이지"
        return context

class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "accounts/signup.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("accounts:login")
        else: 
            print(form.errors)
        return render(request, "accounts/signup.html", {"form": form})

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username if self.request.user.is_authenticated else None
        return context

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

    


