from django.db import models
from django.core.validators import MinValueValidator
from apps.common.models import TimeStampedModel
from apps.user.models import User
from apps.account.models import Account

class TransactionInfo(TimeStampedModel):
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='transaction')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='transaction')
    price = models.DecimalField(max_digits=16, decimal_places=2, validators=[MinValueValidator(0)])


class Transaction(models.Model):
    tr_info = models.OneToOneField(TransactionInfo, on_delete=models.CASCADE, primary_key=True)
    is_transferred = models.BooleanField(verbose_name='거래 여부', default=False)