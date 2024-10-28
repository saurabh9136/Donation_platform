from django.contrib import admin
from .models import User, NGO, Donation

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','get_full_name', 'email', 'mobile_number', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'country_region')
    search_fields = ('first_name', 'last_name', 'email', 'mobile_number')
    date_hierarchy = 'created_at'

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_full_name.short_description = 'Full Name'

class NGOAdmin(admin.ModelAdmin):
    list_display = ('ngo_id','ngo_name', 'email', 'contact_person', 'status', 'created_at')
    search_fields = ('ngo_name',)

class DonationAdmin(admin.ModelAdmin):
    list_display = ('get_user_full_name', 'get_ngo_name', 'amount', 'get_ngo_mobile_number', 'status', 'donation_date')
    

    def get_user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_user_full_name.short_description = 'User Name'

    def get_ngo_mobile_number(self, obj):
        return obj.ngo.mobile_number
    get_ngo_mobile_number.short_description = 'NGO Contact'

    def get_ngo_name(self, obj):
        return obj.ngo.ngo_name
    get_ngo_name.short_description = 'NGO Name'


admin.site.register(User, UserAdmin)
admin.site.register(NGO, NGOAdmin)
admin.site.register(Donation, DonationAdmin)
