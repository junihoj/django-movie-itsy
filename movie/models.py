from django.db import models

class Movie(models.Model):
    STATUS_CHOICES = (
        ('coming_up', 'Coming Up'),
        ('starting', 'Starting'),
        ('running', 'Running'),
        ('finished', 'Finished'),
    )

    name = models.CharField(max_length=100)
    protagonists = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='posters/')
    trailer = models.FileField(upload_to='trailers/')
    start_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='coming_up')
    ranking = models.IntegerField(default=0)  # Initial ranking
    
    def __str__(self):
        return self.name