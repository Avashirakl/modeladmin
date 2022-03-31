from django.contrib import admin
from posts.models import Post, Grade


class PostA(admin.ModelAdmin):
    list_display = ['uuid', 'name', 'created_at', 'created_by','description', 'status']
    list_display_links = ['uuid', 'name',]
    search_fields = ['name', ]
    list_filter = ['status', ]
    list_editable = ['status', ]
    list_per_page = 2
    list_max_show_all = 100

admin.site.register(Post, PostA)
admin.site.register(Grade)
