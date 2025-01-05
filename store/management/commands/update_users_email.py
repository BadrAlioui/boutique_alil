from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Ajoute une adresse email par défaut pour les utilisateurs sans email'

    def handle(self, *args, **kwargs):
        users_without_email = User.objects.filter(email="")
        for user in users_without_email:
            user.email = f"user{user.id}@example.com"
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Email ajouté pour utilisateur {user.username}'))
