# Generated by Django 2.0.3 on 2018-03-21 18:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_category_slug_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='slug_field',
            new_name='slug_field_post',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='slug_field',
            new_name='slug_field_category',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='img',
            field=models.ImageField(default='a', upload_to='BlogImages/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
