# Generated by Django 4.2.2 on 2023-06-13 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active?')),
                ('site_description', models.TextField(blank=True, max_length=255, null=True, verbose_name='Site description')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site_config', to='sites.site', verbose_name='Site')),
            ],
            options={
                'verbose_name': 'Site Config',
                'verbose_name_plural': 'Site Config',
            },
        ),
    ]
