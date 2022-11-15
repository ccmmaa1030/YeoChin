# Generated by Django 3.2.13 on 2022-11-15 00:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('grade', models.CharField(max_length=10)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('address', models.TextField()),
                ('facilities', models.TextField()),
                ('image', models.TextField()),
                ('detail_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.detailregion')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.region')),
            ],
        ),
        migrations.CreateModel(
            name='HotelReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
