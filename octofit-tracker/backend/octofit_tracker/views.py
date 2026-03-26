from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
	queryset = Leaderboard.objects.all()
	serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
	queryset = Workout.objects.all()
	serializer_class = WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
	import os
	codespace_name = os.environ.get('CODESPACE_NAME')
	if codespace_name:
		base_url = f"https://{codespace_name}-8000.app.github.dev"
	else:
		base_url = request.build_absolute_uri('/')[:-1]

	return Response({
		'users': base_url + reverse('user-list', request=request, format=format),
		'teams': base_url + reverse('team-list', request=request, format=format),
		'activities': base_url + reverse('activity-list', request=request, format=format),
		'leaderboard': base_url + reverse('leaderboard-list', request=request, format=format),
		'workouts': base_url + reverse('workout-list', request=request, format=format),
	})

