from django.contrib import admin
from . import models

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    pass

@admin.register(models.Conversations)
class ConversationsAdmin(admin.ModelAdmin):

    pass