# Generated by Django 2.2.1 on 2019-06-17 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_auto_20190617_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='id',
        ),
        migrations.AlterField(
            model_name='registration',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='login.User_detail'),
        ),
    ]
