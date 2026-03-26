from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	class Meta:
		model = User
		fields = ['id', 'name', 'email', 'team']
	def get_id(self, obj):
		return str(obj.id)

class TeamSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	class Meta:
		model = Team
		fields = ['id', 'name', 'members']
	def get_id(self, obj):
		return str(obj.id)

class ActivitySerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	class Meta:
		model = Activity
		fields = ['id', 'user', 'activity', 'duration']
	def get_id(self, obj):
		return str(obj.id)

class LeaderboardSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	class Meta:
		model = Leaderboard
		fields = ['id', 'team', 'points']
	def get_id(self, obj):
		return str(obj.id)

class WorkoutSerializer(serializers.ModelSerializer):
	id = serializers.SerializerMethodField()
	class Meta:
		model = Workout
		fields = ['id', 'name', 'suggested_for']
	def get_id(self, obj):
		return str(obj.id)
