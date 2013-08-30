from django.http import Http404
from advertisement.models import Car, CarModel, CarBrand
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import operator

PRODUCTION=range(1930,2014)
FUEL_TYPES_HTML=["Diesel",
                 "Electric",
                 "LPG", "LPG/Petrol",
                 "Natural gas",
                 "Hybrid",
                 "Petrol"]
GEARBOX_TYPES_HTML=["Manual", "Automatic", "Semi-automatic"]
DEFAULT_VALUE='---'
DEFAULT_VALUE_NUM=1

def home(request):
    latest_car_list = Car.objects.order_by('-created')[:5]
    context = {'latest_car_list': latest_car_list}
    return render(request, 'advertisement/home.html', context)

def added(request):
    return render(request, 'advertisement/added.html')

def detail(request,car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'advertisement/detail.html',{'car': car})

def search(request):
    models = CarModel.objects.all()
    if request.method == 'POST':
        model_id = request.POST.get('model_id', DEFAULT_VALUE)
        production_from = request.POST.get('production_from', DEFAULT_VALUE_NUM)
        production_to = request.POST.get('production_to', DEFAULT_VALUE_NUM)
        price_from = request.POST.get('price_from', DEFAULT_VALUE_NUM)
        price_to = request.POST.get('price_to', DEFAULT_VALUE_NUM)
        power_from = request.POST.get('power_from', DEFAULT_VALUE_NUM)
        power_to = request.POST.get('power_to', DEFAULT_VALUE_NUM)        
        fuel_type2 = request.POST.get('fuel_type', DEFAULT_VALUE)
        gearbox_type2 = request.POST.get('gearbox_type', DEFAULT_VALUE)
        max_mileage = request.POST.get('max_mileage', DEFAULT_VALUE_NUM)
        auxiliary_heating = request.POST.get('auxiliary_heating', 'off')
        central_locking = request.POST.get('central_locking', 'off')
        cruise_control = request.POST.get('cruise_control', 'off')
        electric_heated_seats = request.POST.get('electric_heated_seats', 'off')
        electric_windows = request.POST.get('electric_windows', 'off')
        navigation_system = request.POST.get('navigation_system', 'off')
        parking_sensors = request.POST.get('parking_sensors', 'off')
        power_assisted_steering = request.POST.get('power_assisted_steering',
                                                   'off')
        sunroof = request.POST.get('sunroof', 'off')
        ABS = request.POST.get('ABS', 'off')
        ESP = request.POST.get('ESP', 'off')
        four_wheel_drive = request.POST.get('four_wheel_drive', 'off')
        immobilizer = request.POST.get('immobilizer', 'off')
        particulate = request.POST.get('particulate', 'off')
        xenon_headlights = request.POST.get('xenon_headlights', 'off')
        taxi = request.POST.get('taxi', 'off')
        disabled_accessible = request.POST.get('disabled_accessible', 'off')
        full_service_history = request.POST.get('full_service_history', 'off')
        print("sunroof=")
        print(sunroof)        
        results_car_list = Car.objects.all()
        if model_id != DEFAULT_VALUE:
            results_car_list = results_car_list.filter(car_model=model_id)
        if production_from != DEFAULT_VALUE:
            results_car_list = results_car_list.filter(production__gte=
                                                       production_from)
        if production_to != DEFAULT_VALUE:
            results_car_list = results_car_list.filter(production__lte=
                                                       production_to)
        if price_from != '':
            results_car_list = results_car_list.filter(price__gte=price_from)
        if price_to != '':
            results_car_list = results_car_list.filter(price__lte=price_to)
        if power_to != '':
            results_car_list = results_car_list.filter(power__lte=power_to)
        if power_from != '':
            results_car_list = results_car_list.filter(power__gte=power_from)
        if fuel_type2 != DEFAULT_VALUE:
            results_car_list = results_car_list.filter(fuel_type=fuel_type2)
        if gearbox_type2 != DEFAULT_VALUE:
            results_car_list = results_car_list.filter(gearbox_type=
                                                       gearbox_type2)
        if max_mileage != '':
            results_car_list = results_car_list.filter(mileage__lte=
                                                       max_mileage)
    #Extras
        if auxiliary_heating == 'on':
            results_car_list = results_car_list.filter(auxiliary_heating=True)
        if central_locking == 'on':
            results_car_list = results_car_list.filter(central_locking=True)
        if cruise_control == 'on':
            results_car_list = results_car_list.filter(cruise_control=True)
        if electric_heated_seats == 'on':
            results_car_list = results_car_list.filter(electric_heated_seats=
                                                       True)
        if electric_windows == 'on':
            results_car_list = results_car_list.filter(electric_windows=True)
        if navigation_system == 'on':
            results_car_list = results_car_list.filter(navigation_system=True)
        if parking_sensors == 'on':
            results_car_list = results_car_list.filter(parking_sensors=True)
        if power_assisted_steering == 'on':
            results_car_list = results_car_list.filter(power_assisted_steering=
                                                       True)
        if sunroof == 'on':
            results_car_list = results_car_list.filter(sunroof=True)
        if ABS == 'on':
            results_car_list = results_car_list.filter(ABS=True)
        if ESP == 'on':
            results_car_list = results_car_list.filter(ESP=True)
        if four_wheel_drive == 'on':
            results_car_list = results_car_list.filter(four_wheel_drive=True)
        if immobilizer == 'on':
            results_car_list = results_car_list.filter(immobilizer=True)
        if particulate == 'on':
            results_car_list = results_car_list.filter(particulate=True)
        if xenon_headlights == 'on':
            results_car_list = results_car_list.filter(xenon_headlights=True)
        if taxi == 'on':
            results_car_list = results_car_list.filter(taxi=True)
        if disabled_accessible == 'on':
            results_car_list = results_car_list.filter(disabled_accessible=True)
        if full_service_history == 'on':
            results_car_list = results_car_list.filter(full_service_history=
                                                       True)
        results_car_list = Car.objects.order_by('price')
        return render(request,
                      'advertisement/results.html',
                      {'results_car_list':results_car_list}
                      )
    return render(request,
                  'advertisement/search.html',
                  {'models':models,
                   'PRODUCTION':PRODUCTION,
                   'FUEL_TYPES_HTML':FUEL_TYPES_HTML,
                   'GEARBOX_TYPES_HTML':GEARBOX_TYPES_HTML,
                  }
                  )

def add(request):
    models = CarModel.objects.all()
    if request.method == 'POST':
        car_model2 = request.POST.get('model_id')
        production2 = request.POST.get('production')
        price2 = request.POST.get('price')
        power2 = request.POST.get('power')   
        fuel_type2 = request.POST.get('fuel_type')
        gearbox_type2 = request.POST.get('gearbox_type')
        mileage2 = request.POST.get('mileage')
        color2 = request.POST.get('color')
        fuel_consumption2 = request.POST.get('fuel_consumption')
        engine_size2 = request.POST.get('engine_size')
        auxiliary_heating = request.POST.get('auxiliary_heating', 'off')
        central_locking = request.POST.get('central_locking', 'off')
        cruise_control = request.POST.get('cruise_control', 'off')
        electric_heated_seats = request.POST.get('electric_heated_seats', 'off')
        electric_windows = request.POST.get('electric_windows', 'off')
        navigation_system = request.POST.get('navigation_system', 'off')
        parking_sensors = request.POST.get('parking_sensors', 'off')
        power_assisted_steering = request.POST.get('power_assisted_steering',
                                                   'off')
        sunroof = request.POST.get('sunroof', 'off')
        ABS = request.POST.get('ABS', 'off')
        ESP = request.POST.get('ESP', 'off')
        four_wheel_drive = request.POST.get('four_wheel_drive', 'off')
        immobilizer = request.POST.get('immobilizer', 'off')
        particulate = request.POST.get('particulate', 'off')
        xenon_headlights = request.POST.get('xenon_headlights', 'off')
        taxi = request.POST.get('taxi', 'off')
        disabled_accessible = request.POST.get('disabled_accessible', 'off')
        full_service_history = request.POST.get('full_service_history', 'off')
        photo_file_12 = request.POST.get('photo_file_1', 'off')
        print(photo_file_12)
        new_car = Car(car_model=CarModel(id=car_model2),
                      price=price2,
                      production=production2,
                      power=power2,
                      fuel_type=fuel_type2,
                      mileage=mileage2,
                      gearbox_type=gearbox_type2,
                      engine_size=engine_size2,
                      fuel_consumption=fuel_consumption2,
                      color=color2,
                      photo_file_1=photo_file_12
                      )
        if auxiliary_heating == 'on':
            new_car.auxiliary_heating=True
        if central_locking == 'on':
            new_car.central_locking=True
        if cruise_control == 'on':
            new_car.cruise_control=True
        if electric_heated_seats == 'on':
            new_car.electric_heated_seats=True
        if electric_windows == 'on':
            new_car.electric_windows=True
        if navigation_system == 'on':
            new_car.navigation_system=True
        if parking_sensors == 'on':
            new_car.parking_sensors=True
        if power_assisted_steering == 'on':
            new_car.power_assisted_steering=True
        if sunroof == 'on':
            new_car.sunroof=True
        if ABS == 'on':
            new_car.ABS=True
        if ESP == 'on':
            new_car.ESP=True
        if four_wheel_drive == 'on':
            new_car.four_wheel_drive=True
        if immobilizer == 'on':
            new_car.immobilizer=True
        if particulate == 'on':
            new_car.particulate=True
        if xenon_headlights == 'on':
            new_car.xenon_headlights=True
        if taxi == 'on':
            new_car.taxi=True
        if disabled_accessible == 'on':
            new_car.disabled_accessible=True
        if full_service_history == 'on':
            new_car.full_service_history=True
        new_car.save()
        return HttpResponseRedirect('/advertisement/added')
    return render(request,
                  'advertisement/add.html',
                  {'models':models,
                   'PRODUCTION':PRODUCTION,
                   'FUEL_TYPES_HTML':FUEL_TYPES_HTML,
                   'GEARBOX_TYPES_HTML':GEARBOX_TYPES_HTML,
                   }                  
                  )