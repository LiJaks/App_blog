# Generated by Django 2.2 on 2022-07-14 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='upload_record/')),
            ],
        ),
        migrations.CreateModel(
            name='BlogRecordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=5000)),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'db_record',
            },
        ),
        migrations.CreateModel(
            name='BlogImgModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images_blogs/')),
                ('blog_record', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_blog.BlogRecordModel')),
            ],
            options={
                'db_table': 'db_img',
            },
        ),
    ]