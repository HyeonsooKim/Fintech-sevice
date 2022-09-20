# Generated by Django 4.1 on 2022-09-21 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_account_delete_accountasset_delete_accountstock_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=20, verbose_name='종목명')),
                ('isin', models.CharField(max_length=20, verbose_name='ISIN')),
                ('asset_group', models.CharField(choices=[('미국 주식', '미국 주식'), ('미국섹터 주식', '미국섹터 주식'), ('선진국 주식', '선진국 주식'), ('신흥국 주식', '신흥국 주식'), ('전세계 주식', '전세계 주식'), ('부동산 / 원자재', '부동산 / 원자재'), ('채권 / 현금', '채권 / 현금')], max_length=20, verbose_name='자산그룹')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='보유수량')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='현재가')),
                ('account', models.ForeignKey(db_column='account_id', on_delete=django.db.models.deletion.CASCADE, related_name='asset', to='account.account')),
                ('info', models.ForeignKey(db_column='asset_info', on_delete=django.db.models.deletion.DO_NOTHING, related_name='info', to='asset.assetinfo')),
            ],
        ),
    ]
