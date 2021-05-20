# Generated by Django 3.2.3 on 2021-05-16 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('district', models.CharField(choices=[('AL', 'ALAPPUZHA'), ('ER', 'ERNAKULAM'), ('ID', 'IDUKKI'), ('KN', 'KANNUR'), ('KS', 'KASARGOD'), ('KL', 'KOLLAM'), ('KT', 'KOTTAYAM'), ('KZ', 'KOZHIKODE'), ('MA', 'MALAPPURAM'), ('PL', 'PALAKKAD'), ('PT', 'PATHANAMTHITTA'), ('TV', 'TRIVANDRUM'), ('TS', 'THRISSUR'), ('WA', 'WAYANAD')], max_length=2)),
                ('phone', models.CharField(max_length=20)),
                ('sector', models.CharField(choices=[('GV', 'GOVERNMENT'), ('PR', 'PRIVATE')], max_length=2)),
                ('covid_beds', models.CharField(max_length=20)),
                ('normal_beds', models.CharField(max_length=20)),
                ('icu_beds', models.CharField(max_length=20)),
                ('ventilator', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('aadhar', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('district', models.CharField(choices=[('AL', 'ALAPPUZHA'), ('ER', 'ERNAKULAM'), ('ID', 'IDUKKI'), ('KN', 'KANNUR'), ('KS', 'KASARGOD'), ('KL', 'KOLLAM'), ('KT', 'KOTTAYAM'), ('KZ', 'KOZHIKODE'), ('MA', 'MALAPPURAM'), ('PL', 'PALAKKAD'), ('PT', 'PATHANAMTHITTA'), ('TV', 'TRIVANDRUM'), ('TS', 'THRISSUR'), ('WA', 'WAYANAD')], max_length=2)),
                ('category', models.CharField(choices=[('CV', 'COVID'), ('NC', 'NON-COVID')], max_length=2)),
                ('status', models.CharField(choices=[('WT', 'WAITING'), ('AD', 'ADMITTED'), ('DS', 'DISCHARGED')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='BedAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('C', 'COVID'), ('N', 'NORMAL'), ('I', 'ICU'), ('V', 'VENTILATOR')], max_length=2)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beds.hospital')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beds.patient')),
            ],
        ),
    ]
