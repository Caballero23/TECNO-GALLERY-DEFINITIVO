from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from  .models import Carac_moviles,Fundas, Protector

# Register your models here.





admin.site.register(Carac_moviles)

admin.site.register(Fundas)
admin.site.register(Protector)