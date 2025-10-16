from django.contrib import adminfrom django.contrib import admin

from .models import User, Team, Activity, Workout, Leaderboardfrom .models import User, Team, Activity, Workout, Leaderboard



@admin.register(User)admin.site.register(User)

class UserAdmin(admin.ModelAdmin):admin.site.register(Team)

    list_display = ('username', 'email', 'team')admin.site.register(Activity)

    search_fields = ('username', 'email')admin.site.register(Workout)

admin.site.register(Leaderboard)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'duration', 'calories')
    search_fields = ('user__username', 'type')

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'duration')
    search_fields = ('user__username', 'name')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'score')
    search_fields = ('user__username',)
