# main_app/models.py
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class Feedback(models.Model):
    APP_CHOICES = [
        ("biodiversity", "Biodiversity"),
        ("land", "Land"),
        ("map", "Map"),
        ("forestry", "Forestry"),
    ]

    app_name = models.CharField(max_length=50, choices=APP_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.app_name}] {self.message[:30]}"

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"




# PROXY MODELS para mahiwalay sa admin
class BiodiversityFeedback(Feedback):
    class Meta:
        proxy = True
        verbose_name = "Biodiversity Feedback"
        verbose_name_plural = "Biodiversity Feedback"



class LandFeedback(Feedback):
    class Meta:
        proxy = True
        verbose_name = "Land Feedback"
        verbose_name_plural = "Land Feedback"

class MapFeedback(Feedback):
    class Meta:
        proxy = True
        verbose_name = "Map Feedback"
        verbose_name_plural = "Map Feedback"

class ForestryFeedback(Feedback):
    class Meta:
        proxy = True
        verbose_name = "Forestry Feedback"
        verbose_name_plural = "Forestry Feedback"


