from django.contrib import admin
from sqlalchemy.testing.pickleable import Order
from .models import Blog, Gallery, Index

admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(Index)


