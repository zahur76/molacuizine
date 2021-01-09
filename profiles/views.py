from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def profile(request):
    """ Display the user's profile. """

    # Request profile for logged in user
    profile = get_object_or_404(UserProfile, user__username=request.user)
    # Obtain all orders for userprofile called above
    orders = profile.orders.all()

    if request.method == 'POST':

        form = UserProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')

    if request.method == 'GET':

        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
    }
    return render(request, 'profiles/profile.html', context)
