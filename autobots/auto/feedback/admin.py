from django.contrib import admin
from .models import FeedBack, FeedBacks


class FeedBackAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(FeedBack)
admin.site.register(FeedBacks)