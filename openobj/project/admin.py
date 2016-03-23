from django.contrib import admin

# Register your models here.
from project.models import ProjectClassifyFirst, ProjectClassifySecond, Project


@admin.register(ProjectClassifyFirst)
class ProjectClassifyFirstAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectClassifySecond)
class ProjectClassifySecondAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass