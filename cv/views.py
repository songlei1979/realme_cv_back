import os
from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from docx import Document
from io import BytesIO
from .models import TempIDModel, PersonalStatement, KeySkill, Education, WorkExperience, WorkTask, Achievement, Interest

@api_view(['GET'])
def get_all_info_by_temp_id(request, temp_id):
    try:
        # Fetch the TempIDModel instance
        temp_id_instance = TempIDModel.objects.get(temp_id=temp_id)

        # Fetch related data
        personal_statement = PersonalStatement.objects.filter(temp_id=temp_id_instance).first()
        key_skills = KeySkill.objects.filter(temp_id=temp_id_instance)
        educations = Education.objects.filter(temp_id=temp_id_instance)
        work_experiences = WorkExperience.objects.filter(temp_id=temp_id_instance)
        interests = Interest.objects.filter(temp_id=temp_id_instance)

        # Fetch WorkTasks and Achievements based on related WorkExperience
        work_experience_ids = work_experiences.values_list('id', flat=True)
        work_tasks = WorkTask.objects.filter(work_experience__id__in=work_experience_ids)
        achievements = Achievement.objects.filter(work_experience__id__in=work_experience_ids)

        # Load the Word template document
        template_path = os.path.join(settings.BASE_DIR, 'documents', str(temp_id) + '.docx')  # Ensure this file exists
        doc = Document()
        doc.save(template_path)
        if not os.path.exists(template_path):
            return Response({'error': f'Template file not found at {template_path}'}, status=status.HTTP_404_NOT_FOUND)

        doc = Document(template_path)

        # Modify the document by adding the required information
        doc.add_heading('Name', level=1)  # Adding Name as a heading
        doc.add_paragraph('[Student Name]')  # Replace with dynamic student name


        # Add Personal Statement
        if personal_statement:
            doc.add_heading('Personal Statement', level=1)
            doc.add_paragraph(personal_statement.content)

        # Add Key Skills
        if key_skills.exists():
            doc.add_heading('Key Skills', level=1)
            for skill in key_skills:
                doc.add_paragraph(skill.content, style='ListBullet')

        # Add Education
        if educations.exists():
            doc.add_heading('Education', level=1)
            for education in educations:
                doc.add_paragraph(f"{education.programme_title} ({education.year_start} - {education.year_complete})")
                doc.add_paragraph(f"Institution: {education.institution}, {education.location}")
                if education.courses_and_projects:
                    doc.add_paragraph(f"Courses/Projects: {education.courses_and_projects}")

        # Add Work Experience
        if work_experiences.exists():
            doc.add_heading('Work Experience', level=1)
            for experience in work_experiences:
                doc.add_paragraph(f"{experience.job_title} ({experience.year_start} - {experience.year_complete})")
                doc.add_paragraph(f"Organisation: {experience.organisation}, {experience.location}")

                # Add Work Tasks
                related_tasks = work_tasks.filter(work_experience=experience)
                if related_tasks.exists():
                    doc.add_heading('Tasks', level=2)
                    for task in related_tasks:
                        doc.add_paragraph(task.content, style='ListBullet')

                # Add Achievements
                related_achievements = achievements.filter(work_experience=experience)
                if related_achievements.exists():
                    doc.add_heading('Achievements', level=2)
                    for achievement in related_achievements:
                        doc.add_paragraph(achievement.content, style='ListBullet')

        # Add Interests
        if interests.exists():
            doc.add_heading('Interests', level=1)
            for interest in interests:
                doc.add_paragraph(interest.content)

        doc.add_heading('Reference', level=1)  # Adding Reference as a heading
        doc.add_paragraph('[Reference Details]')  # Replace with dynamic reference

        # Define the save path for the new document
        save_path = os.path.join(settings.BASE_DIR, 'documents', f"{temp_id}.docx")
        print(f"Attempting to save document at: {save_path}")  # Debugging output

        # Save the document to disk
        try:
            doc.save(save_path)
            print(f"Document successfully saved at: {save_path}")
        except Exception as e:
            print(f"Error saving document: {e}")
            return Response({'error': f"Error saving document: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Check if the document was saved successfully
        if not os.path.exists(save_path):
            return Response({'error': 'Document was not saved as expected.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Save document to BytesIO for response
        byte_io = BytesIO()
        doc.save(byte_io)
        byte_io.seek(0)

        # Create a response with the document
        response = HttpResponse(byte_io,
                                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename="{temp_id}.docx"'
        return response

    except TempIDModel.DoesNotExist:
        return Response({'error': 'TempID not found'}, status=status.HTTP_404_NOT_FOUND)
