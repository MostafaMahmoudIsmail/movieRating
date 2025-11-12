from django.db import models

class Movie(models.Model):
    movieId = models.IntegerField(primary_key=True, db_column='movieid') 
    title = models.CharField(max_length=255)
    genres = models.TextField()

    class Meta:
        db_table = 'movies'
        managed = False


class Link(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, db_column='movieid', primary_key=True)
    imdbId = models.IntegerField(db_column='imdbid')
    tmdbId = models.IntegerField(db_column='tmdbid')

    class Meta:
        db_table = 'links'
        managed = False


class Rating(models.Model):
    userId = models.IntegerField(db_column='userid')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, db_column='movieid',null=True, blank=True )
    rating = models.DecimalField(max_digits=2, decimal_places=1, db_index=True)
    timestamp = models.BigIntegerField()

    class Meta:
        db_table = 'ratings'
        managed = True
        unique_together = ('userId', 'movie')


class Tag(models.Model):
    userId = models.IntegerField(db_column='userid')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, db_column='movieid')
    tag = models.CharField(max_length=255)
    timestamp = models.BigIntegerField()

    class Meta:
        db_table = 'tags'
        managed = False
        unique_together = ('userId', 'movie', 'tag')


