from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Bot(models.Model):
    id = models.CharField(max_length=36,
                          validators=[
                              RegexValidator(
                                regex='^.{36}$',
                                message='id length has to be 36',
                                code='nomatch')
                          ],
                          primary_key=True, null=False)
    name = models.CharField(max_length=255)