from django.core.management import BaseCommand

from users.models import Employee


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = Employee.objects.create(
            email="admin@admin.admin",
            telegram_id="@PyAG04",
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )

        user.set_password("123qwe456rty")
        user.save()