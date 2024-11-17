from django.contrib import admin

from Centr.models import MenuTrainingCent, more_detailed, card_info
from Centr.models import MenuAbout
from Centr.models import Teacher


# Register your models here.
admin.site.register(MenuTrainingCent)
admin.site.register(MenuAbout)
admin.site.register(Teacher)
admin.site.register(more_detailed)
admin.site.register(card_info)
