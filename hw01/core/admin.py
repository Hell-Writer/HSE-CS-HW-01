from django.contrib import admin
from .models import Article, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('text','title','name')
    empty_value_display = '-пусто-'


admin.site.register(Article)
admin.site.register(Contact, ContactAdmin)

