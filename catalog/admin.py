from django.contrib import admin

# Register your models here.
from .models import Madicine,Category,Generic_name
from feedback.models import Feedback



#admin.site.register(Madicine)
admin.site.register(Category)
admin.site.register(Generic_name)


class ChoiceInline(admin.TabularInline):
    model = Feedback



class FeedbackAdmin(admin.ModelAdmin):

    inlines = [ChoiceInline]

admin.site.register(Madicine, FeedbackAdmin)