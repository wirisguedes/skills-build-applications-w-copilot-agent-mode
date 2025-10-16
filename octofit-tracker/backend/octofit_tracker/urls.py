

import os
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.http import JsonResponse

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)

def api_root_with_env(request):
    codespace_name = os.environ.get('CODESPACE_NAME', '')
    base_url = f"https://{codespace_name}-8000.app.github.dev" if codespace_name else "http://localhost:8000"
    return JsonResponse({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activities': f'{base_url}/api/activities/',
        'workouts': f'{base_url}/api/workouts/',
        'leaderboard': f'{base_url}/api/leaderboard/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root_with_env, name='api-root'),
]
