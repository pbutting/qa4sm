# Generated by Django 2.1 on 2018-10-09 18:10

from django.db import migrations

def init_filters(apps, schema_editor):
    DataFilter = apps.get_model('validator', 'DataFilter')

    # Metop-A observations - filter on the sat_id flag where value of 3 bytes is metop a
    # Metop-B observations - filter on the sat_id flag where value of 4 bytes is metop b
    # No confidence flags raised - filter on conf_flag - not sure exactly yet, but looks like no value means all is ok
    # Soil not frozen (or state not known) - filter on variable ssf where values of 0 and 1 b mean unkown and frozen respectively

    filters = (
        {'id': 10, 'name': 'FIL_ASCAT_METOP_A', 'description': 'Metop-A observations', 'help_text': 'sat_id flag is metop-a'},
        {'id': 11, 'name': 'FIL_ASCAT_METOP_B', 'description': 'Metop-B observations', 'help_text': 'sat_id flag is metop-b'},
        {'id': 12, 'name': 'FIL_ASCAT_UNFROZEN_UNKNOWN', 'description': 'Soil not frozen (or state not known)', 'help_text': 'ssf flag is "unfrozen" or "unknown"'},
        {'id': 13, 'name': 'FIL_ASCAT_NO_CONF_FLAGS', 'description': 'No confidence flags raised', 'help_text': 'No confidence flags (indicating problems with the data) are set'},
        {'id': 14, 'name': 'FIL_ASCAT_NO_PROC_FLAGS', 'description': 'No processing flags raised', 'help_text': 'No processing flags (indicating data values are changed based on thresholds) are set'},
        )
    for f in filters:
        fil = DataFilter(**f)
        fil.save()

class Migration(migrations.Migration):

    dependencies = [
        ('validator', '0011_fill_progress_20181113_1618'),
    ]

    operations = [
        migrations.RunPython(init_filters),
    ]
