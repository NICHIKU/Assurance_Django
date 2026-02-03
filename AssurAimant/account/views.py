from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.views import View
from django.views.generic import UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.utils.decorators import method_decorator
from core.decorators import verification_required
from .forms import CustomLoginForm, CustomUserForm
from .forms import ModificationForm
from .models import CustomUser


user = get_user_model()

@method_decorator(verification_required, name='dispatch')
class UserProfileView(View):
    template_name = 'account/profile.html'
    
    def get(self, request):
        return render(request, self.template_name, {'user': request.user})
 
@method_decorator(verification_required, name='dispatch')
class AccountModificationView(View):
    template_name = 'account/profile_modif.html'
    
    def get(self, request):
        form = ModificationForm(
            initial={
                'first_name' : request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,

                # Nullable values :
                'age': getattr(request.user, 'age', None),
                'smoker': 'yes' if getattr(request.user, 'smoker', False) else 'no',
                'height': getattr(request.user, 'height', None),
                'weight': getattr(request.user, 'weight', None),
                'sex': getattr(request.user, 'sex', ''),
                'region': getattr(request.user, 'region', ''),
                'children': getattr(request.user, 'children', None),
            }
        )

        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = ModificationForm(request.POST)
        if form.is_valid():
            user = request.user

            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            
            # Handle optional fields
            if form.cleaned_data['age'] is not None:
                user.age = form.cleaned_data['age']
            if form.cleaned_data['children'] is not None:
                user.children = form.cleaned_data['children']
            if form.cleaned_data['height'] is not None:
                user.height = form.cleaned_data['height']
            if form.cleaned_data['weight'] is not None:
                user.weight = form.cleaned_data['weight']
                
            # Calculate BMI only if both height and weight are available
            if user.height and user.weight:
                user.bmi = user.weight / (user.height / 100) ** 2
                
            user.smoker = (form.cleaned_data.get('smoker') == 'yes')
            user.sex = form.cleaned_data['sex']
            user.region = form.cleaned_data['region']

            user.save()

            return redirect('profile_modif')
        
        return render(request, self.template_name, {'form': form})

@verification_required
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