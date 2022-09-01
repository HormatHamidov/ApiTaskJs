# Generated by Django 4.0.5 on 2022-08-29 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='bank_account',
            field=models.CharField(max_length=10, null=True, verbose_name='Bank hesabı'),
        ),
        migrations.AlterField(
            model_name='task',
            name='city',
            field=models.TextField(null=True, verbose_name='Şəhər'),
        ),
        migrations.AlterField(
            model_name='task',
            name='country',
            field=models.TextField(null=True, verbose_name='Ölkə'),
        ),
        migrations.AlterField(
            model_name='task',
            name='datetime',
            field=models.DateTimeField(null=True, verbose_name='Təklifin qüvvədə olduğu müddət'),
        ),
        migrations.AlterField(
            model_name='task',
            name='delivery_condition',
            field=models.TextField(choices=[('exw', 'EXW'), ('fca', 'FCA'), ('fob', 'FOB'), ('cif', 'CIF')], default='fca', max_length=4, null=True, verbose_name='Çatdırılma şərti'),
        ),
        migrations.AlterField(
            model_name='task',
            name='delivery_cost',
            field=models.CharField(max_length=10, null=True, verbose_name='Çatdırılma xərci'),
        ),
        migrations.AlterField(
            model_name='task',
            name='delivery_date',
            field=models.DateTimeField(null=True, verbose_name='Çatdırılma tarixi'),
        ),
        migrations.AlterField(
            model_name='task',
            name='discount',
            field=models.CharField(choices=[('var', 'VAR'), ('yoxdur', 'YOXDUR')], default='var', max_length=10, null=True, verbose_name='Endirim'),
        ),
        migrations.AlterField(
            model_name='task',
            name='edv_degree',
            field=models.CharField(max_length=10, null=True, verbose_name='ƏDV drərəcəsi'),
        ),
        migrations.AlterField(
            model_name='task',
            name='edv_price',
            field=models.CharField(max_length=10, null=True, verbose_name='ƏDV məbləği'),
        ),
        migrations.AlterField(
            model_name='task',
            name='location',
            field=models.TextField(null=True, verbose_name='Ünvan'),
        ),
        migrations.AlterField(
            model_name='task',
            name='miqdar',
            field=models.CharField(max_length=10, null=True, verbose_name='Miqdar'),
        ),
        migrations.AlterField(
            model_name='task',
            name='payment_terms',
            field=models.TextField(choices=[('öncədən ödəniş', 'ÖNCƏDƏN ÖDƏNİŞ'), ('konsiqnasiya', 'KONSİQNASİYA')], default='konsiqnasiya', max_length=14, null=True, verbose_name='Ödəniş şərti'),
        ),
        migrations.AlterField(
            model_name='task',
            name='price',
            field=models.CharField(max_length=10, null=True, verbose_name='Vahidin qiyməti'),
        ),
        migrations.AlterField(
            model_name='task',
            name='request_number',
            field=models.CharField(max_length=10, null=True, verbose_name='Sorğu nömrəsi'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type_transport',
            field=models.CharField(choices=[('avtomobil', 'AVTOMOBİL'), ('dəmir yolu', 'DƏMİR YOLU'), ('dəniz', 'DƏNİZ'), ('hava', 'HAVA')], default='avtomobil', max_length=10, null=True, verbose_name='Çatdırılma xərci'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user_id',
            field=models.CharField(max_length=10, null=True, verbose_name='Müştəri İD'),
        ),
        migrations.AlterField(
            model_name='task',
            name='valyuta',
            field=models.CharField(choices=[('azn', 'AZN'), ('usd', 'USD'), ('eur', 'EUR'), ('try', 'TRY'), ('rub', 'RUB')], default='azn', max_length=10, null=True, verbose_name='Valyuta'),
        ),
        migrations.AlterField(
            model_name='task',
            name='zipcode',
            field=models.CharField(max_length=10, null=True, verbose_name='Zip kod'),
        ),
    ]
