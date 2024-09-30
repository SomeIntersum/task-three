from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from travels.forms import TravelForm
from travels.models import Travel, TravelImage


# Create your views here.
def home(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'travels/home.html', {'users': users})


def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    travels = user.travels.all()
    return render(request, 'travels/user_detail.html', {'user': user, 'travels': travels})


def travel_detail(request, travel_id):
    travel = get_object_or_404(Travel, id=travel_id)
    images = travel.images.all()
    return render(request, 'travels/travel_detail.html', {'travel': travel, 'images': images})


@login_required
def my_travels(request):
    travels = request.user.travels.all()
    return render(request, 'travels/my_travels.html', {'travels': travels})


@login_required
def create_travel(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            travel = form.save(commit=False)
            travel.user = request.user
            travel.save()

            images = request.FILES.getlist('images')
            for image in images:
                TravelImage.objects.create(
                    travel=travel,
                    image=image,
                    caption=request.POST.get('caption', '')
                )

            return redirect('my_travels')
    else:
        form = TravelForm()

    return render(request, 'travels/create_travel.html', {'form': form})
