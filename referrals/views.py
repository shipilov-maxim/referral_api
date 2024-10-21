from django.utils import timezone
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from .models import ReferralCode, Referral
from .permissions import IsOwner
from .serializers import ReferralCodeSerializer, ReferralSerializer


class CreateReferralCodeView(generics.CreateAPIView):
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralCodeSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        if ReferralCode.objects.filter(user=self.request.user, expiration_date__gt=timezone.now()).first():
            raise ValidationError('У вас есть активный реферальный код')
        serializer.save(user=self.request.user)


class ReferralCodeListView(ListAPIView):
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralCodeSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ['referrer_email', ]


class GetReferralCodeView(generics.RetrieveAPIView):
    serializer_class = ReferralCodeSerializer
    queryset = ReferralCode.objects.all()


class DeleteReferralCodeView(generics.DestroyAPIView):
    queryset = ReferralCode.objects.all()
    permission_classes = (IsOwner,)


class CreateReferralView(generics.CreateAPIView):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer


class GetReferralsView(generics.ListAPIView):
    serializer_class = ReferralSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Referral.objects.filter(referrer_id=user_id)
