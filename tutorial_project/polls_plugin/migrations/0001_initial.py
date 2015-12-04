# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='cms.CMSPlugin', primary_key=True)),
                ('poll', models.ForeignKey(to='polls.Poll')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
