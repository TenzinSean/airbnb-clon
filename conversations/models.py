from django.db import models
from core import models as core_models


class Conversations(core_models.TimeStampModel):

    participants = models.ManyToManyField("users.User", related_name="conversations", blank=True)


    def __str__(self):
        # usernames = []
        # for user in self.participants.all():
        #     usernames.append(user.username)
        # return ", ".join(usernames)
        return str(self.created)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Message"


    def count_participate(self):
        return self.participants.count()
    
    count_participate.short_description = "Number of Participate"

    
class Message(core_models.TimeStampModel):
    message = models.TextField()
    user = models.ForeignKey("users.User", related_name="messages", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversations", related_name="messages", on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user} says: {self.message}'