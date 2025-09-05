from django.contrib import admin
from . import models


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level")
    list_editable = ("level",)
    search_fields = ("name",)


@admin.register(models.ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "featured", "created")
    list_filter = ("featured", "category")
    search_fields = ("title", "subtitle", "description")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("skills",)


@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "start_date", "end_date")
    search_fields = ("role", "company")


@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "start_date", "end_date")
    search_fields = ("degree", "institution")


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "description")


@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author", "role", "created")
    search_fields = ("author", "role", "content")


@admin.register(models.SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("platform", "url", "order")
    list_editable = ("order",)
    search_fields = ("platform",)


@admin.register(models.ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "is_read", "created")
    list_filter = ("is_read",)
    search_fields = ("name", "email", "subject", "message")

# Register your models here.
