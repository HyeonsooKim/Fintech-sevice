from apps.account.models import Account
from rest_framework import serializers
from rest_framework.serializers import ValidationError

class AccountSerializer(serializers.ModelSerializer):
    total_assets = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)
    class Meta:
        model = Account
        fields = ('id', 'user', 'stock_firm', 'account_name', 'account_number', 'total_assets')


class AccountDetailSerializer(AccountSerializer):
    total_profit = serializers.SerializerMethodField()
    profit_percent = serializers.SerializerMethodField()
    
    class Meta:
        model = Account
        fields = ('id', 'user', 'stock_firm', 'account_name', 'account_number', 'total_profit', 'profit_percent', 'total_assets')

    def get_total_profits(self, obj):
        return obj.total_assets - obj.invest_principal

    def get_profits_ratio(self, obj):
        return ((obj.total_assets - obj.invest_principal) / obj.invest_principal) * 100