from django.apps import apps
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.db import connection
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def assign_permission_to_peerlogic_staff_group(sender, **kwargs):
    group, created = Group.objects.get_or_create(name="staff")
    with connection.cursor() as cursor:
        cursor.execute("SELECT app, name FROM django_migrations ORDER BY applied DESC")
        migrations = cursor.fetchall()

    for app_config in apps.get_app_configs():
        for model in app_config.get_models():
            content_type = ContentType.objects.get_for_model(model)

            model_name = model.__name__.lower()
            is_new_model = any(model_name in migration[1].lower() for migration in migrations)

            if is_new_model:
                permissions = Permission.objects.filter(content_type=content_type)
                group.permissions.add(*permissions)
