from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.TextField()
    review = models.TextField()

    def __str__(self):
        return self.title

def get_default_movie():
    return Movie.objects.get_or_create(title = 'LOTR', price = 0)[0].id

class CartItem(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE, default = get_default_movie)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.quantity) + str(self.movie)