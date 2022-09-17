from django.db import models

# Create your models here.
class AccountAsset(models.Model):
    user = models.CharField(max_length=20, verbose_name="고객이름")
    account_name = models.CharField(max_length=20, verbose_name="계좌명")
    stock_firm = models.CharField(max_length=20, verbose_name="증권사")
    account_number = models.CharField(max_length=20, verbose_name="계좌번호")
    total_asset = models.IntegerField(verbose_name="계좌 총 자산")
    invest_principal = models.CharField(max_length=20, verbose_name="투자원금")
    total_profit = models.IntegerField(verbose_name="총 수익금")
    percent_profit = models.IntegerField(verbose_name="수익률")
    isin = models.CharField(max_length=20, verbose_name="ISIN")


class Stock(models.Model):
    stock_name = models.CharField(max_length=20, verbose_name="종목명")
    isin = models.CharField(max_length=20, verbose_name="ISIN")
    asset_group = models.CharField(max_length=20, verbose_name="자산그룹")
    current_stock_price = models.PositiveIntegerField(verbose_name="현재가")

class AccountStock(models.Model):
    account_number = models.CharField(max_length=20, verbose_name="계좌번호")
    stock_name = models.CharField(max_length=20, verbose_name="종목명")
    stock_quantity = models.IntegerField(verbose_name="보유수량")
    market_value = models.IntegerField(verbose_name="평가금액")

class TransactionHistory(models.Model):
    account_number = models.CharField(max_length=20, verbose_name="계좌번호")
    user = models.CharField(max_length=20, verbose_name="고객이름")
    amount_value = models.IntegerField(verbose_name="거래금액")