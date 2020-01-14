import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail

# Create your models here.

class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )


    LANGUAGE_ENGLISH = "en"
    LANGUAGE_TIBETAN = "tb"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_TIBETAN, "Tibetan"),
    )


    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10,blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    langauge = models.CharField(choices=LANGUAGE_CHOICES, max_length=2,blank=True,default=LANGUAGE_TIBETAN)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True,default=CURRENCY_KRW)
    superhost = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)


    def verify_email(self):
        if self.email_confirmed is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            send_mail(
                "Verify Airbnb Account", 
                "Verify Account! what is your secret: {secret}", 
                settings.EMAIL_FROM, 
                [self.email],
                fail_silently=False,
            )
        return 




