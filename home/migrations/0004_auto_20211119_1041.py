# Generated by Django 2.2 on 2021-11-19 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_auto_20211119_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regddd',
            name='job',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm', models.CharField(max_length=50)),
                ('ph', models.BigIntegerField(blank=True, null=True)),
                ('pro', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField()),
                ('children', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
