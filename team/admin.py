from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role')