# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import generate_temp_id, submit_all_info
from . import views
from .views import generate_word


# from .views import get_all_info_by_temp_id
from .viewsets import (
    TempIDModelViewSet, PersonalStatementViewSet, KeySkillViewSet,
    EducationViewSet, WorkExperienceViewSet, InterestViewSet
)

# Initialize the DefaultRouter
router = DefaultRouter()
router.register(r'temp-ids', TempIDModelViewSet)
router.register(r'personal-statements', PersonalStatementViewSet)
router.register(r'key-skills', KeySkillViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'work-experiences', WorkExperienceViewSet)
# router.register(r'work-tasks', WorkTaskViewSet)
# router.register(r'achievements', AchievementViewSet)
router.register(r'interests', InterestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', submit_all_info, name='submit_all_info_test'),
    # path('info/<uuid:temp_id>/', get_all_info_by_temp_id, name='get_all_info_by_temp_id'),
    # path('submit-info/', submit_all_info, name='submit_all_info'),  # 新增的路由
    # path('generate-temp-id/', generate_temp_id, name='generate_temp_id'),
    path('predict/', views.predict_category, name='predict_category'),
    path('generate-word/', views.generate_word, name='generate_word'),
]
