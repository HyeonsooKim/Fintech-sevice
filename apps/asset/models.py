from django.db import models
from apps.account.models import Account

class AssetInfo(models.Model):
    GROUPS = (
        ('미국 주식', '미국 주식'),
        ('미국섹터 주식', '미국섹터 주식'),
        ('선진국 주식', '선진국 주식'),
        ('신흥국 주식', '신흥국 주식'),
        ('전세계 주식', '전세계 주식'),
        ('부동산 / 원자재', '부동산 / 원자재'),
        ('채권 / 현금', '채권 / 현금'),
    )
    stock_name = models.CharField(max_length=20, verbose_name="종목명")
    isin = models.CharField(max_length=20, verbose_name="ISIN")
    asset_group = models.CharField(max_length=20, verbose_name="자산그룹", choices=GROUPS)

class Asset(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_column='account_id', related_name='asset')
    info = models.ForeignKey(AssetInfo, on_delete=models.DO_NOTHING, db_column='asset_info', related_name='info')
    quantity = models.IntegerField(verbose_name="보유수량")
    price = models.DecimalField(verbose_name='현재가', max_digits=20, decimal_places=2)