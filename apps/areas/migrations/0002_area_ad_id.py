from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='ad_id',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
