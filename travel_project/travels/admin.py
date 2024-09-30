from django.contrib import admin

from travels.models import Travel, TravelImage


# Register your models here.
@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'location', 'cost', 'created_at')
    list_filter = ('user', 'location', 'created_at')
    search_fields = ('title', 'description', 'location', 'user__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    prepopulated_fields = {'slug': ('title',)}


@admin.register(TravelImage)
class TravelImageAdmin(admin.ModelAdmin):
    list_display = ('travel', 'image', 'caption')
    search_fields = ('caption',)
    list_filter = ('travel',)
