# Generated by Django 3.0.7 on 2020-09-05 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='police',
            name='district',
        ),
        migrations.RemoveField(
            model_name='police',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='police',
            name='state',
        ),
        migrations.AddField(
            model_name='police',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='police',
            name='police',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
