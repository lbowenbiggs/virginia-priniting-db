from django.contrib import admin

from .models import Biography, NewspaperHistory, NewspaperCitation, ImprintRecord

# Register your models here.
admin.site.register(Biography)
admin.site.register(NewspaperCitation)
admin.site.register(NewspaperHistory)
admin.site.register(ImprintRecord)