from django.contrib import admin
# chapter 9
from rango.models import UserProfile
# Register your models here.

# chapter 5
from rango.models import Category, Page
class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
admin.site.register(Page, PageAdmin)

# chapter 6
# Add in this class to customise the Admin Interface 
class CategoryAdmin(admin.ModelAdmin): 
	prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)

# chapter 9
admin.site.register(UserProfile)

