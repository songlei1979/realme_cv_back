# # serializers.py
# from rest_framework import serializers
# from .models import (
#     TempIDModel, PersonalStatement, KeySkill, Education,
#     WorkExperience, WorkTask, Achievement, Interest
# )


# class TempIDModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TempIDModel
#         fields = ['id', 'temp_id', 'created_at', 'updated_at']


# class PersonalStatementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PersonalStatement
#         fields = ['id', 'temp_id', 'content', 'created_at', 'updated_at']


# class KeySkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = KeySkill
#         fields = ['id', 'temp_id', 'content', 'created_at', 'updated_at']


# class EducationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Education
#         fields = [
#             'id', 'temp_id', 'programme_title', 'institution',
#             'location', 'courses_and_projects', 'year_start',
#             'year_complete', 'created_at', 'updated_at'
#         ]


# class WorkExperienceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WorkExperience
#         fields = [
#             'id', 'temp_id', 'job_title', 'organisation',
#             'location', 'year_start', 'year_complete',
#             'created_at', 'updated_at'
#         ]


# class WorkTaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WorkTask
#         fields = ['id', 'work_experience', 'content', 'created_at', 'updated_at']


# class AchievementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Achievement
#         fields = ['id', 'work_experience', 'content', 'created_at', 'updated_at']


# class InterestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Interest
#         fields = ['id', 'temp_id', 'content', 'created_at', 'updated_at']


from rest_framework import serializers
from .models import (
    TempIDModel, PersonalStatement, KeySkill, Education,
    WorkExperience, Interest
)


class TempIDModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempIDModel
        fields = ['id', 'temp_id', 'created_at', 'updated_at']


class PersonalStatementSerializer(serializers.Serializer):
    statementQ1 = serializers.CharField(max_length=500)
    statementQ2 = serializers.CharField(max_length=500)


class KeySkillSerializer(serializers.Serializer):
    skillsQ1 = serializers.CharField(max_length=500)
    skillsQ2 = serializers.CharField(max_length=500)


class EducationSerializer(serializers.Serializer):
    major = serializers.CharField(max_length=100)
    school = serializers.CharField(max_length=200)
    startTime = serializers.CharField(max_length=100)
    endTime = serializers.CharField(max_length=100)
    achievements = serializers.CharField(max_length=1000, required=False)


class WorkExperienceSerializer(serializers.Serializer):
    job_title = serializers.CharField(max_length=100)
    organisation = serializers.CharField(max_length=200)
    startTime = serializers.CharField(max_length=100)
    endTime = serializers.CharField(max_length=100)
    tasks = serializers.CharField(max_length=1000)
    achievements = serializers.CharField(max_length=1000, required=False)


class InterestSerializer(serializers.Serializer):
    interestQ1 = serializers.CharField(max_length=500)
    interestQ2 = serializers.CharField(max_length=500)


class CompleteSubmissionSerializer(serializers.Serializer):
    temp_id = serializers.UUIDField()
    personal_statement = PersonalStatementSerializer()
    key_skills = KeySkillSerializer()
    educations = EducationSerializer(many=True)
    work_experiences = WorkExperienceSerializer(many=True)
    interests = InterestSerializer()