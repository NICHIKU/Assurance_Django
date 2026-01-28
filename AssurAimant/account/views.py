from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, UpdateView, ListView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model

from .forms import ModificationForm
User = get_user_model()

class UserProfileView(ListView):
    model = User
    template_name = 'account/profile.html'
    context_object_name = 'profile'

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

    


