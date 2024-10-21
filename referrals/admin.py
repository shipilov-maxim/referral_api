from django.contrib import admin
from referrals.models import ReferralCode, Referral

admin.site.register(Referral)


@admin.register(ReferralCode)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'user',)
