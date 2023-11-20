import factory


class Location(factory.django.DjangoModelFactory):
    name = factory.Faker("city")
    latitude = factory.Faker("latitude")
    longitude = factory.Faker("longitude")

    class Meta:
        model = "locations.Location"
