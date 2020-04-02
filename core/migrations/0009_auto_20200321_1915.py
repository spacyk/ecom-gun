# Generated by Django 2.2.8 on 2020-03-21 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_auto_20200310_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_option',
            field=models.CharField(choices=[('S', 'Stripe'), ('P', 'PayPal')], max_length=2, null=True),
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.BillingAddress'),
        ),
    ]
