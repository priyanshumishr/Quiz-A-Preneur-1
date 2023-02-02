from django.db import models
from django.contrib.auth import get_user_model

User= get_user_model

DIFF_CHOICES =(
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard'),
)


QUESTION_TYPE =(
    ('single_correct','single'),
    ('multi_correct', 'multi'),
    ('text_based','text'),
    
    
)

class registration_detail(models.Model):
    name = models.CharField(max_length=255)
    School = models.CharField(max_length=255,blank=False)
    standard = models.PositiveIntegerField()
    city_of_residence = models.CharField(max_length=255,blank=False)
    phone_number=models.PositiveIntegerField(null=True)
    mail_address=models.EmailField(max_length=255, default=False)
    
    def __str__(self):
        return self.name.username
