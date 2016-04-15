from django.contrib import admin
from project.models import ProjectClassifyFirst, ProjectClassifySecond, Project
from pagedown.widgets import AdminPagedownWidget
from django.db import models

@admin.register(ProjectClassifyFirst)
class ProjectClassifyFirstAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectClassifySecond)
class ProjectClassifySecondAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
