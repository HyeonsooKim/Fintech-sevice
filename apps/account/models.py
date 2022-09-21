from django.db import models
from django.core.validators import MinValueValidator

from apps.asset.models import AssetInfo
from apps.common.models import TimeStampedModel
from apps.user.models import User

# Create your models here.
class Account(TimeStampedModel):
    STOCK_FIRMS = (
        ('디셈버증권', '디셈버증권'),
        ('베스트투자', '베스트투자'),
        ('핀트투자증권', '핀트투자증권'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', related_name='account')
    account_name = models.CharField(max_length=20, verbose_name="계좌명")
    account_number = models.CharField(max_length=20, verbose_name="계좌번호")
    invest_principal = models.DecimalField(verbose_name="투자원금", max_digits=20, decimal_places=2)
    stock_firm = models.CharField(verbose_name='증권사', max_length=20, choices=STOCK_FIRMS)


class AccountAsset(TimeStampedModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_column='account_id', related_name='asset')
    info = models.ForeignKey(AssetInfo, on_delete=models.DO_NOTHING, db_column='asset_info', related_name='info')
    quantity = models.IntegerField(verbose_name="보유수량")
    price = models.DecimalField(verbose_name='현재가', max_digits=20, decimal_places=2)
