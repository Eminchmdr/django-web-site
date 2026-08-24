from django.contrib import admin
from .models import Blog, Category
from django.utils.safestring import mark_safe


class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'is_active', 'is_home',
                    'slug', 'selected_category')
    list_editable = ('is_active', 'is_home')
    search_fields = ('title', 'description')
    readonly_fields = ('slug',)
    list_filter = ('is_active', 'is_home', 'categories')

    def selected_category(self, obj):
        html = ""
        for category in obj.categories.all():
            html += f"<li>{category.name}</li>"
        return mark_safe(f"<ul>{html}</ul>")


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
