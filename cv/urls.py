# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import get_all_info_by_temp_id
from .viewsets import (
    TempIDModelViewSet, PersonalStatementViewSet, KeySkillViewSet,
    EducationViewSet, WorkExperienceViewSet, WorkTaskViewSet,
    AchievementViewSet, InterestViewSet
)

# Initialize the DefaultRouter
router = DefaultRouter()
router.register(r'temp-ids', TempIDModelViewSet)
router.register(r'personal-statements', PersonalStatementViewSet)
router.register(r'key-skills', KeySkillViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'work-experiences', WorkExperienceViewSet)
router.register(r'work-tasks', WorkTaskViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'interests', InterestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('info/<uuid:temp_id>/', get_all_info_by_temp_id, name='get_all_info_by_temp_id'),
]
