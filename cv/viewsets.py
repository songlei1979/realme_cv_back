# views.py
from rest_framework import viewsets
from .models import (
    TempIDModel, PersonalStatement, KeySkill, Education,
    WorkExperience, WorkTask, Achievement, Interest
)
from .serializers import (
    TempIDModelSerializer, PersonalStatementSerializer, KeySkillSerializer,
    EducationSerializer, WorkExperienceSerializer, WorkTaskSerializer,
    AchievementSerializer, InterestSerializer
)


class TempIDModelViewSet(viewsets.ModelViewSet):
    queryset = TempIDModel.objects.all()
    serializer_class = TempIDModelSerializer


class PersonalStatementViewSet(viewsets.ModelViewSet):
    queryset = PersonalStatement.objects.all()
    serializer_class = PersonalStatementSerializer


class KeySkillViewSet(viewsets.ModelViewSet):
    queryset = KeySkill.objects.all()
    serializer_class = KeySkillSerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class WorkTaskViewSet(viewsets.ModelViewSet):
    queryset = WorkTask.objects.all()
    serializer_class = WorkTaskSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
