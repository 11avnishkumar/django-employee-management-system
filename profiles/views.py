from django.shortcuts import render
from .forms import ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required


# Profile Views
@login_required
def profile(request):
    template_name = 'profiles/profile.html'
    return render(request, template_name)


# Profile Views
# @login_required
def profile_update_form(request):
    user_form = UserUpdateForm(request.POST or None,instance=request.user)
    profile_form = ProfileUpdateForm(request.POST or None,instance=request.user.profile)
    if profile_form.is_valid() and user_form.is_valid():
        profile_form.save()
        user_form.save()
    context = {
        'profile_form': profile_form,
        'user_form': user_form
    }    
    template_name = 'profiles/profile_update.html'
    return render(request, template_name,context)    
