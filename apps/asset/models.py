from django.db import models

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

    def __str__(self):
        return self.stock_name