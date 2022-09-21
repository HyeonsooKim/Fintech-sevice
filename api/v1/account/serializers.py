import decimal
from apps.account.models import Account, AccountAsset
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    total_assets = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)
    class Meta:
        model = Account
        fields = (
            'id',
            'account_name',
            'stock_firm',
            'account_number',
            'total_assets',
            'invest_principal',
            'total_profits',
            'earnings_rate',
            'created_at',
            'updated_at',
        )


class AccountAssetSerializer(serializers.ModelSerializer):
    # info = AssetInfoSerializer(read_only=True)
    # total = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)
    asset_name = serializers.CharField(read_only=True, source='asset.asset_name')
    class Meta:
        model = AccountAsset
        # fields = ('info', 'total')
        fields = (
            'id',
            'info',
            'asset_name',
            'price',
            'quantity',
            'created_at',
            'updated_at',
            'evaluated_price',
        )
