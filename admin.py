from django.contrib import admin

from movie_app.models import CineProfessional, Movie, MovieReview

# Register your models here.

admin.site. register(CineProfessional)
admin. site. register(Movie)
admin.site.register(MovieReview)