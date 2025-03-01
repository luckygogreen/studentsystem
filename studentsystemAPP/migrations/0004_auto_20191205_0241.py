# Generated by Django 2.2.7 on 2019-12-05 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsystemAPP', '0003_auto_20191204_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('url_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='role',
            name='menus',
            field=models.ManyToManyField(blank=True, to='studentsystemAPP.Menu'),
        ),
    ]
