from django.db import models
from django.core.validators import RegexValidator
import uuid


class Message(models.Model):
    id = models.CharField(max_length=36,
                          primary_key=True,
                          blank=True,
                          default=uuid.uuid4)
    conversationId = models.CharField(max_length=36,
                          validators=[
                              RegexValidator(
                                regex='^.{36}$',
                                message='conversationId length has to be 36',
                                code='nomatch')
                          ],)
    timestamp = models.DateTimeField(auto_now_add=True)
    from_bot = models.CharField(max_length=36, db_column='from',
                                validators=[
                                    RegexValidator(
                                        regex='^.{36}$',
                                        message='from length has to be 36',
                                        code='nomatch')
                                ],)
    to = models.CharField(max_length=36, 
                          validators=[
                              RegexValidator(
                                regex='^.{36}$',
                                message='to length has to be 36',
                                code='nomatch')
                          ],)
    text = models.TextField()
    