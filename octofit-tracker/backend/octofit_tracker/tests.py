from django.test import TestCasefrom django.test import TestCase

from django.urls import reversefrom .models import User, Team, Activity, Workout, Leaderboard

from rest_framework.test import APIClient

from rest_framework import statusclass ModelSmokeTest(TestCase):

from .models import User, Team, Activity, Workout, Leaderboard    def test_team_create(self):

        team = Team.objects.create(name='Test Team')

class UserModelTest(TestCase):        self.assertEqual(str(team), 'Test Team')

    def test_create_user(self):

        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')    def test_user_create(self):

        self.assertEqual(user.username, 'testuser')        team = Team.objects.create(name='Test Team')

        self.assertEqual(user.email, 'test@example.com')        user = User.objects.create_user(username='test', email='test@test.com', password='123', team=team)

        self.assertEqual(user.email, 'test@test.com')

class TeamModelTest(TestCase):

    def test_create_team(self):    def test_activity_create(self):

        team = Team.objects.create(name='Team A')        team = Team.objects.create(name='Test Team')

        self.assertEqual(team.name, 'Team A')        user = User.objects.create_user(username='test', email='test@test.com', password='123', team=team)

        activity = Activity.objects.create(user=user, type='run', duration=10, calories=100)

class ActivityModelTest(TestCase):        self.assertEqual(activity.type, 'run')

    def test_create_activity(self):

        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='testpass')    def test_workout_create(self):

        activity = Activity.objects.create(user=user, type='run', duration=30, calories=200)        team = Team.objects.create(name='Test Team')

        self.assertEqual(activity.type, 'run')        user = User.objects.create_user(username='test', email='test@test.com', password='123', team=team)

        self.assertEqual(activity.duration, 30)        workout = Workout.objects.create(user=user, name='W1', description='desc', duration=20)

        self.assertEqual(activity.calories, 200)        self.assertEqual(workout.name, 'W1')



class WorkoutModelTest(TestCase):    def test_leaderboard_create(self):

    def test_create_workout(self):        team = Team.objects.create(name='Test Team')

        user = User.objects.create_user(username='testuser3', email='test3@example.com', password='testpass')        user = User.objects.create_user(username='test', email='test@test.com', password='123', team=team)

        workout = Workout.objects.create(user=user, name='Cardio', description='Cardio session', duration=45)        lb = Leaderboard.objects.create(user=user, score=100)

        self.assertEqual(workout.name, 'Cardio')        self.assertEqual(lb.score, 100)

        self.assertEqual(workout.duration, 45)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create_user(username='testuser4', email='test4@example.com', password='testpass')
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class APIRootTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('workouts', response.data)
        self.assertIn('leaderboard', response.data)
