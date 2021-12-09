from django.db import models


# create a class of college classes with certain attributes
class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    courseNumber = models.IntegerField()
    instructorName = models.CharField(max_length=60, default="", blank=True)
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title
