from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.views import View
from django.views.generic import UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.utils.decorators import method_decorator
from core.decorators import verification_required
from .forms import CustomLoginForm, CustomUserForm
from .forms import ModificationForm
from .models import CustomUser

user = get_user_model()

@method_decorator(verification_required, name='dispatch')
class UserProfileView(ListView):
    model = user
    template_name = 'account/profile.html'
    context_object_name = 'profile'
 
@method_decorator(verification_required, name='dispatch')
class AccountModificationView(UpdateView):
    template_name = 'account/profile_modif.html'
    success_url = reverse_lazy('profile')
    
    def get(self, request):
        form = ModificationForm(
            initial={
                'first_name' : request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,

                # Nullable values :
                'age': getattr(request.user, 'age', '') if getattr(request.user, 'age', None) is not None else '',
                'smoker': 'yes' if getattr(request.user, 'smoker', False) else 'no',
                'height': getattr(request.user, 'height', '') if getattr(request.user, 'height', None) is not None else '',
                'weight': getattr(request.user, 'weight', '') if getattr(request.user, 'weight', None) is not None else '',
                'sex': getattr(request.user, 'sex', '') if getattr(request.user, 'sex', None) is not None else '',
                'region': getattr(request.user, 'region', '') if getattr(request.user, 'region', None) is not None else '',
                'children': getattr(request.user, 'children', '') if getattr(request.user, 'children', None) is not None else '',
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
            
            # Handle nullable fields
            user.age = form.cleaned_data.get('age')
            user.children = form.cleaned_data.get('children')
            user.height = form.cleaned_data.get('height')
            user.weight = form.cleaned_data.get('weight')
            user.sex = form.cleaned_data.get('sex')
            user.region = form.cleaned_data.get('region')
            
            # Compute BMI only if height and weight are provided
            if user.height and user.weight:
                user.bmi = user.compute_bmi()
            
            # Handle smoker field conversion
            smoker_value = form.cleaned_data.get('smoker')
            user.smoker = smoker_value == 'yes'

            user.save()

            return redirect('profile')
        
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