# Generated by Django 3.2.13 on 2022-11-16 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0002_alter_qna_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='qna',
            table='qna_board',
        ),
        migrations.AlterModelTable(
            name='tag',
            table='qna_tag',
        ),
    ]