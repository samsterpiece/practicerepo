from django.conf import settings
from django.db import models
from django.utils import timezone

#Class- Defining a project
#Post - Name of model (start class name with uppercase
#models.Model - Post is django model , save in database
class Post(models.Model): #defines our model(is an object)
    #defined properties
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=200) #text
    text=models.TextField() #text with no limit
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
