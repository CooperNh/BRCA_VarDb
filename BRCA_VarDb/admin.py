from django.contrib import admin
from .models import Patient, Occurance, Investigation, Gene, Transcript, Variant

# Register your models here.

admin.site.register(Patient)
admin.site.register(Occurance)
admin.site.register(Investigation)
admin.site.register(Gene)
admin.site.register(Transcript)
admin.site.register(Variant)

