from rest_framework import serializers
from .models import ReferralCode, Referral


class ReferralCodeSerializer(serializers.ModelSerializer):
    referrer_email = serializers.SerializerMethodField()

    def get_referrer_email(self, instance):
        return instance.user.email

    class Meta:
        model = ReferralCode
        fields = ['referrer_email', 'code', 'expiration_date']


class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ['referrer', 'referred']
