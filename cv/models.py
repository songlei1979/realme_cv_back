from django.db import models
import uuid


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TempIDModel(BaseModel):
    temp_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return str(self.temp_id)


class PersonalStatement(BaseModel):
    temp_id = models.OneToOneField(TempIDModel, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.temp_id)


class KeySkill(BaseModel):
    temp_id = models.ForeignKey(TempIDModel, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.temp_id)


class Education(BaseModel):
    temp_id = models.ForeignKey(TempIDModel, on_delete=models.CASCADE)
    programme_title = models.TextField()
    institution = models.TextField()
    location = models.TextField()
    courses_and_projects = models.TextField(null=True, blank=True)
    year_start = models.DateField()
    year_complete = models.DateField()

    def __str__(self):
        return str(self.temp_id)

class WorkExperience(BaseModel):
    temp_id = models.ForeignKey(TempIDModel, on_delete=models.CASCADE)
    job_title = models.TextField()
    organisation = models.TextField()
    location = models.TextField()
    year_start = models.DateField()
    year_complete = models.DateField()

    def __str__(self):
        return str(self.job_title)

class WorkTask(BaseModel):
    work_experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.work_experience)

class Achievement(BaseModel):
    work_experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.work_experience)

class Interest(BaseModel):
    temp_id = models.ForeignKey(TempIDModel, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.temp_id)