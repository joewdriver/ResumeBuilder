from django.contrib import admin

# Register your models here.

from django.contrib import admin
from resumes.models import *


class EdHistoryInLine(admin.StackedInline):
    model = EdHistory
    extra = 2


class ResumeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['statement']}),
        (None, {'fields': ['low_salary']}),
        (None, {'fields': ['high_salary']}),
        (None, {'fields': ['applicant']}),
    ]
    inlines = [EdHistoryInLine]


admin.site.register(Applicant)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(School)
admin.site.register(Skills)
admin.site.register(JobHistory)
# admin.site.register(EdHistory)
admin.site.register(References)