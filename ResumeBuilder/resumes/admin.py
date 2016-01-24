from django.contrib import admin

# Register your models here.

from django.contrib import admin
from resumes.models import *


class EdHistoryInLine(admin.StackedInline):
    model = EdHistory
    extra = 1


class JobHistoryInLine(admin.StackedInline):
    model = JobHistory
    extra = 1


class ReferencesInLine(admin.StackedInline):
    model = References
    extra = 1


class SkillsInLine(admin.StackedInline):
    model = Skills
    extra = 1


# this is where we derive the structure for the resume creation form
class ResumeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['statement']}),
        (None, {'fields': ['low_salary']}),
        (None, {'fields': ['high_salary']}),
        (None, {'fields': ['applicant']}),
    ]
    inlines = [EdHistoryInLine, JobHistoryInLine, SkillsInLine, ReferencesInLine]


admin.site.register(Applicant)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(School)