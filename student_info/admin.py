from django.contrib import admin
from django.utils.html import format_html
from .models import Student


# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'dob',
        'email',
        'tel',
        'gender',
        'country',
        'image_preview',
        'message',
    )

    search_fields = ('id', 'email', 'tel', 'gender', 'country')
    list_filter = ('gender', 'country')
    ordering = ('id',)

    def image_preview(self, obj):
        if obj.profile_pic:
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" width="50" height="50" /></a>',
                obj.profile_pic.url,
                obj.profile_pic.url
            )
        return "No Image"

    image_preview.short_description = "Profile Pic"