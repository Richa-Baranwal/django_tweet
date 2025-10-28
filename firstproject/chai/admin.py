from django.contrib import admin
from .models import ChaiVarity, ChaiReview, ChaiStore, ChaiCert

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class CertAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')


# class ChaiStoreInline(admin.TabularInline):
#     model = ChaiStore
#     extra = 1

# class ChaiCertInline(admin.TabularInline):
#     model = ChaiCert
#     extra = 1

admin.site.register(ChaiVarity, ChaiVarityAdmin)
admin.site.register(ChaiReview)
admin.site.register(ChaiStore, StoreAdmin)
admin.site.register(ChaiCert, CertAdmin)
