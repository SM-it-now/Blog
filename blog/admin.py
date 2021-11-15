from django.contrib import admin
from .models import Post, Category, Tag, Comment

# Register your models here.

# Post모델의 각 객체를 display하고, 그것을 admin 페이지에 보이도록 표시.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at')

# category모델을 admin에 출력.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# admin 페이지에 출력.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
