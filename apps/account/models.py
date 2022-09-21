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

    def __str__(self):
        return self.account_number

    def total_assets(self):
        return sum([asset.price * asset.quantity for asset in self.assets.all()])

    def total_profits(self):
        return self.total_assets() - self.invest_principal

    def earnings_rate(self):
        return self.total_profits() / self.invest_principal * 100


class AccountAsset(TimeStampedModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_column='account_id', related_name='assets')
    info = models.ForeignKey(AssetInfo, on_delete=models.DO_NOTHING, db_column='asset_info', related_name='info')
    quantity = models.IntegerField(verbose_name="보유수량")
    price = models.DecimalField(verbose_name='현재가', max_digits=20, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['account', 'info'], name='unique_account_asset')
        ]

    def evaluated_price(self):
        return self.price * self.quantity


class TransactionInfo(TimeStampedModel):
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='transaction')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='transaction')
    price = models.DecimalField(max_digits=16, decimal_places=2, validators=[MinValueValidator(0)])


class Transaction(models.Model):
    tr_info = models.OneToOneField(TransactionInfo, on_delete=models.CASCADE, primary_key=True)
    is_transferred = models.BooleanField(verbose_name='거래 여부', default=False)