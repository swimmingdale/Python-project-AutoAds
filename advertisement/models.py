from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

CAR_MAKES=(
    ("Acura", "Acura"),
    ("Aixam", "Aixam"),
    ("Alfa Romeo", "Alfa Romeo"),
    ("Aston Martin", "Aston Martin"),
    ("Audi", "Audi"),
    ("Austin", "Austin"),
    ("Bentley", "Bentley"),
    ("Berliner", "Berliner"),
    ("BMW", "BMW"),
    ("Borgward", "Borgward"),
    ("Bugatti", "Bugatti"),
    ("Buick", "Buick"),
    ("Cadillac", "Cadillac"),
    ("Chevrolet", "Chevrolet"),
    ("Chrysler", "Chrysler"),
    ("Citroen", "Citroen"),
    ("Corvette", "Corvette"),
    ("Dacia", "Dacia"),
    ("Daewoo", "Daewoo"),
    ("Daihatsu", "Daihatsu"),
    ("Daimler", "Daimler"),
    ("Datsun", "Datsun"),
    ("Dkw", "Dkw"),
    ("Dodge", "Dodge"),
    ("Eagle", "Eagle"),
    ("FSO", "FSO"),
    ("Ferrari", "Ferrari"),
    ("Fiat", "Fiat"),
    ("Ford", "Ford"),
    ("Geo", "Geo"),
    ("Great Wall", "Great wall"),
    ("Honda", "Honda"),
    ("Hyundai", "Hyundai"),
    ("Ifa", "Ifa"),
    ("Infiniti", "Infiniti"),
    ("Innocenti", "Innocenti"),
    ("Isuzu", "Isuzu"),
    ("Jaguar", "Jaguar"),
    ("Kia", "Kia"),
    ("Lada", "Lada"),
    ("Lamborghini", "Lamborghini"),
    ("Lancia", "Lancia"),
    ("Lexus", "Lexus"),
    ("Lifan", "Lifan"),
    ("Lincoln", "Lincoln"),
    ("Lotus", "Lotus"),
    ("Maserati", "Maserati"),
    ("Matra", "Matra"),
    ("Maybach", "Maybach"),
    ("Mazda", "Mazda"),
    ("McLaren", "McLaren"),
    ("Mercedes", "Mercedes"),
    ("Mercury", "Mercury"),
    ("Mg", "Mg"),
    ("Mini", "Mini"),
    ("Mitsubishi", "Mitsubishi"),
    ("Morgan", "Morgan"),
    ("Moskvich", "Moskvich"),
    ("Nissan", "Nissan"),
    ("Oldsmobile", "Oldsmobile"),
    ("Opel", "Opel"),
    ("Perodua", "Perodua"),
    ("Peugeot", "Peugeot"),
    ("Pgo", "Pgo"),
    ("Plymouth", "Plymouth"),
    ("Polonez", "Polonez"),
    ("Pontiac", "Pontiac"),
    ("Porsche", "Porsche"),
    ("Proton", "Proton"),
    ("Renault", "Renault"),
    ("Rolls-Royce", "Rolls-Royce"),
    ("Rover", "Rover"),
    ("Saab", "Saab"),
    ("Samand", "Samand"),
    ("Saturn", "Saturn"),
    ("Scion", "Scion"),
    ("Seat", "Seat"),
    ("Shatenet", "Shatenet"),
    ("Shuanghuan", "Shuanghuan"),
    ("Simca", "Simca"),
    ("Skoda", "Skoda"),
    ("Smart", "Smart"),
    ("Ssang yong", "Ssang yong"),
    ("Subaru", "Subaru"),
    ("Suzuki", "Suzuki"),
    ("Talbot", "Talbot"),
    ("Tata", "Tata"),
    ("Tavria", "Tavria"),
    ("Tazzari", "Tazzari"),
    ("Terberg", "Terberg"),
    ("Tesla", "Tesla"),
    ("Tofas", "Tofas"),
    ("Toyota", "Toyota"),
    ("Trabant", "Trabant"),
    ("Triumph", "Triumph"),
    ("VROMOS", "VROMOS"),
    ("Volga", "Volga"),
    ("Volvo", "Volvo"),
    ("Vw", "Vw"),
    ("Warszawa", "Warszawa"),
    ("Wartburg", "Wartburg"),
    ("Wiesmann", "Wiesmann"),
    ("Xinshun", "Xinshun"),
    ("Zastava", "Zastava"),
    ("Zaz", "Zaz")
          )
FUEL_TYPES = (
    ("Diesel", "Diesel"),
    ("Electric", "Electric"),
    ("LPG", "LPG"),
    ("LPG/Petrol", "LPG/Petrol"),
    ("Natural gas", "Natural gas"),
    ("Hybrid", "Hybrid"),
    ("Petrol", "Petrol"),
               )

GEARBOX_TYPES = (
    ("Manual", "Manual"),
    ("Automatic", "Automatic"),
    ("Semi-automatic", "Semi-automatic"),
    )

class CarBrand (models.Model):
    name = models.CharField(max_length=255, choices=CAR_MAKES)
    
    def __str__(self):
        return self.name

class CarModel (models.Model):
    make = models.ForeignKey(CarBrand)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.make.name + " " + self.name

class Car (models.Model):
    car_model = models.ForeignKey(CarModel)
    #id
    price = models.IntegerField(validators=[MinValueValidator(1)])
    production = models.IntegerField(validators=[MinValueValidator(1930),
                                                 MaxValueValidator(2013)])
    mileage = models.IntegerField(validators=[MinValueValidator(0),
                                              MaxValueValidator(3000000)])
    power = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(2000)])
    engine_size = models.IntegerField(validators=[MinValueValidator(1),
                                                  MaxValueValidator(10000)])
    fuel_type = models.CharField(max_length = 255, choices = FUEL_TYPES)
    fuel_consumption = models.FloatField(validators=[MinValueValidator(0.1),
                                                     MaxValueValidator(100)])
    gearbox_type = models.CharField(max_length = 255, choices = GEARBOX_TYPES)
    color = models.CharField(max_length = 255)
    photo_file_1 = models.FileField(upload_to = 'documents\images', blank=True)
    photo_file_2 = models.FileField(upload_to = 'documents\images', blank=True)
    photo_file_3 = models.FileField(upload_to = 'documents\images', blank=True)
    photo_file_4 = models.FileField(upload_to = 'documents\images', blank=True)
    photo_file_5 = models.FileField(upload_to = 'documents\images', blank=True)
    auxiliary_heating = models.BooleanField()
    central_locking = models.BooleanField()
    cruise_control = models.BooleanField()
    electric_heated_seats = models.BooleanField()
    electric_windows = models.BooleanField()
    navigation_system = models.BooleanField()
    parking_sensors = models.BooleanField()
    power_assisted_steering = models.BooleanField()
    sunroof = models.BooleanField()
    ABS = models.BooleanField()
    ESP = models.BooleanField()
    four_wheel_drive = models.BooleanField()
    immobilizer = models.BooleanField()
    particulate = models.BooleanField()
    xenon_headlights = models.BooleanField()
    taxi = models.BooleanField()
    disabled_accessible = models.BooleanField()
    full_service_history = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.car_model) + " " + str(self.price) + "lv."