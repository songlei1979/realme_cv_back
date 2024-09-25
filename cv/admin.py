# admin.py
from django.contrib import admin
from .models import (
    TempIDModel, PersonalStatement, KeySkill, Education,
    WorkExperience, WorkTask, Achievement, Interest
)


@admin.register(TempIDModel)
class TempIDModelAdmin(admin.ModelAdmin):
    list_display = ['temp_id', 'created_at', 'updated_at']
    search_fields = ['temp_id']


@admin.register(PersonalStatement)
class PersonalStatementAdmin(admin.ModelAdmin):
    list_display = ['temp_id', 'content', 'created_at', 'updated_at']
    search_fields = ['temp_id__temp_id']


@admin.register(KeySkill)
class KeySkillAdmin(admin.ModelAdmin):
    list_display = ['temp_id', 'content', 'created_at', 'updated_at']
    search_fields = ['temp_id__temp_id']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['temp_id', 'programme_title', 'institution', 'year_start', 'year_complete']
    search_fields = ['temp_id__temp_id', 'programme_title', 'institution']


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['temp_id', 'job_title', 'organisation', 'year_start', 'year_complete']
    search_fields = ['temp_id__temp_id', 'job_title', 'organisation']


@admin.register(WorkTask)
class WorkTaskAdmin(admin.ModelAdmin):
    list_display = ['work_experience', 'content', 'created_at', 'updated_at']
    search_fields = ['work_experience__temp_id']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['work_experience', 'content', 'created_at', 'updated_at']
    search_fields = ['work_experience__temp_id']


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['temp_id', 'content', 'created_at', 'updated_at']
    search_fields = ['temp_id__temp_id']
