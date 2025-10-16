from rest_framework import serializersfrom rest_framework import serializers

from .models import User, Team, Activity, Workout, Leaderboardfrom .models import User, Team, Activity, Workout, Leaderboard



class TeamSerializer(serializers.ModelSerializer):class TeamSerializer(serializers.ModelSerializer):

    class Meta:    class Meta:

        model = Team        model = Team

        fields = ['id', 'name']        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):class UserSerializer(serializers.ModelSerializer):

    team = TeamSerializer(read_only=True)    team = TeamSerializer(read_only=True)

    class Meta:    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True, required=False)

        model = User    class Meta:

        fields = ['id', 'username', 'email', 'team']        model = User

        fields = ['id', 'username', 'email', 'team', 'team_id']

class ActivitySerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)class ActivitySerializer(serializers.ModelSerializer):

    class Meta:    user = UserSerializer(read_only=True)

        model = Activity    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

        fields = ['id', 'user', 'type', 'duration', 'calories']    class Meta:

        model = Activity

class WorkoutSerializer(serializers.ModelSerializer):        fields = ['id', 'user', 'user_id', 'type', 'duration', 'calories']

    user = UserSerializer(read_only=True)

    class Meta:class WorkoutSerializer(serializers.ModelSerializer):

        model = Workout    user = UserSerializer(read_only=True)

        fields = ['id', 'user', 'name', 'description', 'duration']    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

    class Meta:

class LeaderboardSerializer(serializers.ModelSerializer):        model = Workout

    user = UserSerializer(read_only=True)        fields = ['id', 'user', 'user_id', 'name', 'description', 'duration']

    class Meta:

        model = Leaderboardclass LeaderboardSerializer(serializers.ModelSerializer):

        fields = ['id', 'user', 'score']    user = UserSerializer(read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_id', 'score']
