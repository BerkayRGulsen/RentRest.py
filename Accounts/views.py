from django.shortcuts import render, redirect

from .forms import SignupForm, VisitorForm
from Reservations.models import Visitor, Car, Branch, Reservations


def registerPage(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            eml = form.cleaned_data.get('email')
            # Added username after video because of error returning customer name if not added
            Visitor.objects.create(
                user=user,
                username=user.username,
                first_name=firstname,
                last_name=lastname,
                email=eml,
                role='customer'
            )

            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def profile(request):
    visitor = request.user.visitor
    form = VisitorForm(instance=visitor)

    reservations = visitor.reservations_set.all()

    if request.method == 'POST':
        form = VisitorForm(request.POST, request.FILES, instance=visitor)
        if form.is_valid():
            form.save()

    context = {'form': form, 'reservations': reservations, }
    return render(request, 'registration/profile.html', context)


def managerProfile(request, ):
    visitor = request.user.visitor
    if request.method == 'POST':
        form = VisitorForm(request.POST, request.FILES, instance=visitor)
        if form.is_valid():
            form.save()
    branches = Branch.objects.filter(manager=visitor)
    form = VisitorForm(instance=visitor)
    context = {'branches': branches, 'form': form, }
    return render(request, 'registration/managerProfile.html', context)
