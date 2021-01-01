from django.shortcuts import render, redirect

from Reservations.forms import FilteredListCars

strr = []
endd = []
print(strr)


def home(request):
    form = FilteredListCars()
    context = {'form': form}
    return render(request, 'reservations/home.html', context)


def carList(request, ):
    from Reservations.models import Car
    cars = Car.objects.all()
    context = {'cars': cars, }
    return render(request, 'reservations/carList.html', context)


def filteredCarList(request):
    from Reservations.models import Car
    from Reservations.models import Branch
    form = FilteredListCars(request.GET)

    if form.is_valid():
        branch = form.cleaned_data.get('branch')
        str = form.cleaned_data.get('takeDate')
        strr.append(str)
        end = form.cleaned_data.get('returnDate')
        endd.append(end)




    realBranch = Branch.objects.get(place=branch)

    cars = Car.objects.filter(branch=realBranch, isActive=True)
    filteredCars = []
    for car in cars:
        if not car.takeDate or (str > car.returnDate[len(car.takeDate) - 1]):
            filteredCars.append(car)
            continue
        for i in range(len(car.takeDate) - 1):
            if (str < car.takeDate[i] and end < car.returnDate[i]) or (
                    str > car.returnDate[i] and end < car.takeDate[i + 1]):
                filteredCars.append(car)
    context = {'cars': filteredCars, 'takeDate': str, 'returnDate': end, }
    return render(request, 'reservations/filteredCarList.html', context)


def rent(request, id):
    from Reservations.models import Reservations
    from Reservations.models import Car
    take = strr[len(strr) - 1]
    give = endd[len(strr) - 1]
    car = Car.objects.get(id=id)
    car.takeDate.append(take)
    car.returnDate.append(give)
    car.save()
    Reservations.objects.create(receiveDate=take, deliveryDate=give, buyer=request.user.visitor, car=car)
    return render(request, 'reservations/rent.html')
