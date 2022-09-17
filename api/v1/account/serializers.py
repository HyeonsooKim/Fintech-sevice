from apps.account.models import AccountAsset, Stock, AccountStock, TransactionHistory
from rest_framework import serializers
from rest_framework.serializers import ValidationError

class AccountAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountAsset
        fields = "__all__"
        # read_only_fields = []

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"

class AccountStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountStock
        fields = "__all__"

class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = "__all__"