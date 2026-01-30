from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.views import View
from django.views.generic import UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .forms import CustomLoginForm, CustomUserForm
from .forms import ModificationForm
from .models import CustomUser
from django.utils.decorators import method_decorator
from .decorators import verification_required


User = get_user_model()

@method_decorator(verification_required, name='dispatch')
class UserProfileView(ListView):
    model = User
    template_name = 'account/profile.html'
    context_object_name = 'profile'
 
@method_decorator(verification_required, name='dispatch')
class AccountModificationView(UpdateView):
    model = User
    form_class = ModificationForm
    template_name = 'account/profile_modif.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user
    
    def post(self, request):
        form = ModificationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'account/profile_modif.html', {'form': form})

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
    
class UserLoginView(LoginView):
    template_name = 'authentification/login.html'
    form_class = CustomLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')