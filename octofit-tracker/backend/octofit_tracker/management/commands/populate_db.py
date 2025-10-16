from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Limpa dados existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Cria times
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Cria usuários super-heróis
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='123', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='123', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='123', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='123', team=dc),
        ]

        # Cria atividades
        for user in users:
            Activity.objects.create(user=user, type='run', duration=30, calories=200)
            Activity.objects.create(user=user, type='bike', duration=60, calories=400)

        # Cria workouts
        for user in users:
            Workout.objects.create(user=user, name='Full Body', description='Treino completo', duration=45)

        # Cria leaderboard
        Leaderboard.objects.create(user=users[0], score=1000)
        Leaderboard.objects.create(user=users[1], score=900)
        Leaderboard.objects.create(user=users[2], score=950)
        Leaderboard.objects.create(user=users[3], score=920)

        self.stdout.write(self.style.SUCCESS('Banco populado com dados de super-heróis!'))
