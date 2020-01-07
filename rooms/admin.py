from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    
    """ Item admin Defination """

    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room admin Defination """


    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")}
        ), 
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")}
        ),
         (
            "Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}
        ),
        (
            "More About the Space",
            
            {"fields": ("amenities", "facilites", "house_rules"), 'classes': ('collapse'),}
        ),
        (
            "Last Details", 
            {"fields": ("host",)}
        )
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )


    list_filter = (
        "instant_book",
        "host__superhost",
        "city",
        "room_type",
        "amenities",
        "facilites",
        "house_rules",
        "country",
    )

    search_fields = ("=city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilites",
        "house_rules"
    )


    def count_amenities(self, obj):
        print(obj.amenities.all())
        return "hello"
    
    count_amenities.short_description = "Hello there"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo model Defination """

    pass

