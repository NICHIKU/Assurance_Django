from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password
from .forms import CustomUserForm
from .models import CustomUser

# Create your views here.

def home_view(request):
    return render(request, 'base.html')

class RegisterView(View):
    template_name = 'account/register.html'
    
    def get(self, request):
        form = CustomUserForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = CustomUser(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                username=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            return redirect('login')
        return render(request, self.template_name, {'form': form})