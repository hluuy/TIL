from django.contrib import admin
from libraries.models import Book, Review, User
# Register your models here.

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(User)