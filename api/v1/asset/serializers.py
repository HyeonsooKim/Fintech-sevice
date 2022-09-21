from rest_framework import serializers
from apps.asset.models import AssetInfo


class AssetInfoSerializer(serializers.ModelSerializer):
    """ 투자 정보 조회 시리얼라이저 """
    class Meta:
        model = AssetInfo
        fields = ('stock_name', 'asset_group', 'isin')


