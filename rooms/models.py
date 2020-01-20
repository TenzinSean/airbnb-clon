from django.db import models
from django.utils import timezone
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
from cal import Calendar

class AbstractItem(core_models.TimeStampModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType abstract """

    class Meta:
        verbose_name_plural = "Room Type"
        ordering = ['created']


class Amenity(AbstractItem):
    """ Amenity object defination """
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model defination """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """ House rule model defination """

    class Meta:
        verbose_name_plural = "House Rules"


class Photo(core_models.TimeStampModel):

    """ Photo of model Defination """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)


    def __str__(self):
        return self.caption


# Create your models here.

class Room(core_models.TimeStampModel):

    """ Room models Definiation """
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=40)
    guests = models.IntegerField(help_text="How many people will be staying?")
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, related_name="rooms", on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    facilites = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)



    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={'pk': self.pk})


    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return all_ratings / len(all_reviews)
        return 0


    def first_photo(self):
        try:
            photo, = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos
    
    def get_calendars(self):
        now = timezone.now()
        this_year = now.year
        this_month = now.month
        next_month = this_month + 1
        if this_month == 12:
            next_month = 1
        this_month_cal = Calendar(this_year, this_month)
        next_month_cal = Calendar(this_year, next_month)
        return [this_month_cal, next_month_cal]
