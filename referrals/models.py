from datetime import timedelta
from django.db import models
from django.utils import timezone

from users.models import User


class ReferralCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, unique=True)
    expiration_date = models.DateTimeField(default=(timezone.now() + timedelta(days=7)))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Реферральный код'
        verbose_name_plural = 'Реферральные коды'
        ordering = ('pk',)


class Referral(models.Model):
    referrer = models.ForeignKey(User, related_name='referrals', on_delete=models.CASCADE)
    referred = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.referrer

    class Meta:
        verbose_name = 'Реферрал'
        verbose_name_plural = 'Реферралы'
        ordering = ('pk',)
