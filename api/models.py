from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name+' '+self.surname


class Actor(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name+' '+self.surname


class Theatre(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    website = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name


class Show(models.Model):
    name = models.CharField(max_length=50)
    annotation = models.TextField(max_length=1000)
    language = models.CharField(max_length=20, null=True)
    duration = models.TimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    season = models.CharField(max_length=9, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    #actors = models.ManyToManyField(Actor, null=True, blank=True)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, null=True)
    premiere = models.BooleanField(default=False)
    ticket_url = models.CharField(max_length=50, null=True, blank=True,)
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.name
