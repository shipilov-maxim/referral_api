from django.urls import path
from .apps import ReferralsConfig
from .views import CreateReferralCodeView, DeleteReferralCodeView, CreateReferralView, GetReferralsView, \
    GetReferralCodeView, ReferralCodeListView

app_name = ReferralsConfig.name

urlpatterns = [
    path('code/create/', CreateReferralCodeView.as_view(), name='create_code'),
    path('code/<int:pk>/', GetReferralCodeView.as_view(), name='get_code'),
    path('code/', ReferralCodeListView.as_view(), name='get_code_filter'),
    path('code/<int:pk>/delete/', DeleteReferralCodeView.as_view(), name='delete_code'),
    path('referral/create/', CreateReferralView.as_view(), name='create_referral'),
    path('referral/<int:user_id>/', GetReferralsView.as_view(), name='get_referrals'),
]
