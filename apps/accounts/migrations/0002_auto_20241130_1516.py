from django.db import migrations

def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    # Create roles
    Group.objects.get_or_create(name="Managers")
    Group.objects.get_or_create(name="Employees")
    Group.objects.get_or_create(name="Customers")

class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
