# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PayPalIPN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business', models.CharField(blank=True, help_text=b'Email where the money was sent.', max_length=127)),
                ('charset', models.CharField(blank=True, max_length=32)),
                ('custom', models.CharField(blank=True, max_length=255)),
                ('notify_version', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('parent_txn_id', models.CharField(blank=True, max_length=19, verbose_name=b'Parent Transaction ID')),
                ('receiver_email', models.EmailField(blank=True, max_length=127)),
                ('receiver_id', models.CharField(blank=True, max_length=127)),
                ('residence_country', models.CharField(blank=True, max_length=2)),
                ('test_ipn', models.BooleanField(default=False)),
                ('txn_id', models.CharField(blank=True, db_index=True, help_text=b'PayPal transaction ID.', max_length=19, verbose_name=b'Transaction ID')),
                ('txn_type', models.CharField(blank=True, help_text=b'PayPal transaction type.', max_length=128, verbose_name=b'Transaction Type')),
                ('verify_sign', models.CharField(blank=True, max_length=255)),
                ('address_country', models.CharField(blank=True, max_length=64)),
                ('address_city', models.CharField(blank=True, max_length=40)),
                ('address_country_code', models.CharField(blank=True, help_text=b'ISO 3166', max_length=64)),
                ('address_name', models.CharField(blank=True, max_length=128)),
                ('address_state', models.CharField(blank=True, max_length=40)),
                ('address_status', models.CharField(blank=True, max_length=11)),
                ('address_street', models.CharField(blank=True, max_length=200)),
                ('address_zip', models.CharField(blank=True, max_length=20)),
                ('contact_phone', models.CharField(blank=True, max_length=20)),
                ('first_name', models.CharField(blank=True, max_length=64)),
                ('last_name', models.CharField(blank=True, max_length=64)),
                ('payer_business_name', models.CharField(blank=True, max_length=127)),
                ('payer_email', models.CharField(blank=True, max_length=127)),
                ('payer_id', models.CharField(blank=True, max_length=13)),
                ('auth_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('auth_exp', models.CharField(blank=True, max_length=28)),
                ('auth_id', models.CharField(blank=True, max_length=19)),
                ('auth_status', models.CharField(blank=True, max_length=9)),
                ('exchange_rate', models.DecimalField(blank=True, decimal_places=16, default=0, max_digits=64, null=True)),
                ('invoice', models.CharField(blank=True, max_length=127)),
                ('item_name', models.CharField(blank=True, max_length=127)),
                ('item_number', models.CharField(blank=True, max_length=127)),
                ('mc_currency', models.CharField(blank=True, default=b'USD', max_length=32)),
                ('mc_fee', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('mc_gross', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('mc_handling', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('mc_shipping', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('memo', models.CharField(blank=True, max_length=255)),
                ('num_cart_items', models.IntegerField(blank=True, default=0, null=True)),
                ('option_name1', models.CharField(blank=True, max_length=64)),
                ('option_name2', models.CharField(blank=True, max_length=64)),
                ('payer_status', models.CharField(blank=True, max_length=10)),
                ('payment_date', models.DateTimeField(blank=True, help_text=b'HH:MM:SS DD Mmm YY, YYYY PST', null=True)),
                ('payment_gross', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=17)),
                ('payment_type', models.CharField(blank=True, max_length=7)),
                ('pending_reason', models.CharField(blank=True, max_length=14)),
                ('protection_eligibility', models.CharField(blank=True, max_length=32)),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('reason_code', models.CharField(blank=True, max_length=15)),
                ('remaining_settle', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('settle_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('settle_currency', models.CharField(blank=True, max_length=32)),
                ('shipping', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('shipping_method', models.CharField(blank=True, max_length=255)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('transaction_entity', models.CharField(blank=True, max_length=7)),
                ('auction_buyer_id', models.CharField(blank=True, max_length=64)),
                ('auction_closing_date', models.DateTimeField(blank=True, help_text=b'HH:MM:SS DD Mmm YY, YYYY PST', null=True)),
                ('auction_multi_item', models.IntegerField(blank=True, default=0, null=True)),
                ('for_auction', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('amount_per_cycle', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('initial_payment_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('next_payment_date', models.DateTimeField(blank=True, help_text=b'HH:MM:SS DD Mmm YY, YYYY PST', null=True)),
                ('outstanding_balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('payment_cycle', models.CharField(blank=True, max_length=32)),
                ('period_type', models.CharField(blank=True, max_length=32)),
                ('product_name', models.CharField(blank=True, max_length=128)),
                ('product_type', models.CharField(blank=True, max_length=128)),
                ('profile_status', models.CharField(blank=True, max_length=32)),
                ('recurring_payment_id', models.CharField(blank=True, max_length=128)),
                ('rp_invoice_id', models.CharField(blank=True, max_length=127)),
                ('time_created', models.DateTimeField(blank=True, help_text=b'HH:MM:SS DD Mmm YY, YYYY PST', null=True)),
                ('amount1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('amount2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('amount3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('mc_amount1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('mc_amount2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('mc_amount3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('password', models.CharField(blank=True, max_length=24)),
                ('period1', models.CharField(blank=True, max_length=32)),
                ('period2', models.CharField(blank=True, max_length=32)),
                ('period3', models.CharField(blank=True, max_length=32)),
                ('reattempt', models.CharField(blank=True, max_length=1)),
                ('recur_times', models.IntegerField(blank=True, default=0, null=True)),
                ('recurring', models.CharField(blank=True, max_length=1)),
                ('retry_at', models.DateTimeField(blank=True, help_text=b'HH:MM:SS DD Mmm YY, YYYY PST', null=True)),
                ('subscr_date', models.DateTimeField(blank=True, help_text=b'HH:MM:SS DD Mmm YY, YYYY PST', null=True)),
                ('subscr_effective', models.DateTimeField(blank=True, help_text=b'HH:MM:SS DD Mmm YY, YYYY PST', null=True)),
                ('subscr_id', models.CharField(blank=True, max_length=19)),
                ('username', models.CharField(blank=True, max_length=64)),
                ('case_creation_date', models.DateTimeField(blank=True, help_text=b'HH:MM:SS DD Mmm YY, YYYY PST', null=True)),
                ('case_id', models.CharField(blank=True, max_length=14)),
                ('case_type', models.CharField(blank=True, max_length=24)),
                ('receipt_id', models.CharField(blank=True, max_length=64)),
                ('currency_code', models.CharField(blank=True, default=b'USD', max_length=32)),
                ('handling_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=64, null=True)),
                ('transaction_subject', models.CharField(blank=True, max_length=255)),
                ('ipaddress', models.GenericIPAddressField(blank=True, null=True)),
                ('flag', models.BooleanField(default=False)),
                ('flag_code', models.CharField(blank=True, max_length=16)),
                ('flag_info', models.TextField(blank=True)),
                ('query', models.TextField(blank=True)),
                ('response', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('from_view', models.CharField(blank=True, max_length=6, null=True)),
            ],
            options={
                'db_table': 'paypal_ipn',
                'verbose_name': 'PayPal IPN',
            },
        ),
    ]
