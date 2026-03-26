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
		def full_url(path):
			# Remove scheme/host if present in path
			if path.startswith('http://') or path.startswith('https://'):
				idx = path.find('/', 8)
				if idx != -1:
					path = path[idx:]
				else:
					path = '/'
			return base_url + path
	else:
		def full_url(path):
			return request.build_absolute_uri(path)

	return Response({
		'users': full_url(reverse('user-list')), 
		'teams': full_url(reverse('team-list')),
		'activities': full_url(reverse('activity-list')),
		'leaderboard': full_url(reverse('leaderboard-list')),
		'workouts': full_url(reverse('workout-list')),
	})

