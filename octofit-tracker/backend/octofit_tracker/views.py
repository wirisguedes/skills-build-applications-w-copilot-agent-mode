from rest_framework import viewsets, permissionsfrom rest_framework import viewsets, routers

from rest_framework.decorators import api_viewfrom rest_framework.decorators import api_view

from rest_framework.response import Responsefrom rest_framework.response import Response

from .models import User, Team, Activity, Workout, Leaderboardfrom .models import User, Team, Activity, Workout, Leaderboard

from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializerfrom .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer



class UserViewSet(viewsets.ModelViewSet):class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()    queryset = User.objects.all()

    serializer_class = UserSerializer    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TeamViewSet(viewsets.ModelViewSet):

class TeamViewSet(viewsets.ModelViewSet):    queryset = Team.objects.all()

    queryset = Team.objects.all()    serializer_class = TeamSerializer

    serializer_class = TeamSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]class ActivityViewSet(viewsets.ModelViewSet):

    queryset = Activity.objects.all()

class ActivityViewSet(viewsets.ModelViewSet):    serializer_class = ActivitySerializer

    queryset = Activity.objects.all()

    serializer_class = ActivitySerializerclass WorkoutViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]    queryset = Workout.objects.all()

    serializer_class = WorkoutSerializer

class WorkoutViewSet(viewsets.ModelViewSet):

    queryset = Workout.objects.all()class LeaderboardViewSet(viewsets.ModelViewSet):

    serializer_class = WorkoutSerializer    queryset = Leaderboard.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]    serializer_class = LeaderboardSerializer



class LeaderboardViewSet(viewsets.ModelViewSet):@api_view(['GET'])

    queryset = Leaderboard.objects.all().order_by('-score')def api_root(request, format=None):

    serializer_class = LeaderboardSerializer    return Response({

    permission_classes = [permissions.AllowAny]        'users': '/users/',

        'teams': '/teams/',

@api_view(['GET'])        'activities': '/activities/',

def api_root(request, format=None):        'workouts': '/workouts/',

    return Response({        'leaderboard': '/leaderboard/',

        'users': '/api/users/',    })

        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'workouts': '/api/workouts/',
        'leaderboard': '/api/leaderboard/',
    })
