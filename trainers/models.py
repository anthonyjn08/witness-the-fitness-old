from django.db import models


class Trainers(models.Model):
    trainer_name = model.OneToOneField(null=False, blank=False)
    trainer_email = models.EmailField(max_length=254, null=False, blank=False)
    trainer_phone_number = models.CharField(max_length=20, null=True, blank=True)
    trainer_bio = model.TextField(null=False)

    def __str__(self):
        return self.trainer_name
