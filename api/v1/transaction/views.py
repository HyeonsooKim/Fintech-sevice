from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.shortcuts import get_object_or_404
from .serializers import TransactionSerializer, TransactionCheckSerializer
from apps.transaction.models import Transaction, TransactionInfo

class TransactionViewSet(CreateModelMixin,
                         GenericViewSet):
    """ 거래 내역 생성 Viewset """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionCheckViewSet(CreateModelMixin,
                              GenericViewSet):
    """ 거래 내역 유효성 검증 Viewset """

    queryset = TransactionInfo.objects.all()
    serializer_class = TransactionCheckSerializer