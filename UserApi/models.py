import random
import string

from django.db import models


# Create your models here.

class UserDetail(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)
    user_type = models.BooleanField(default=False)
    password = models.CharField(max_length=100, null=False)

    def as_json(self):
        return dict(
            name=self.name,
            email=self.email,
            user_type=self.user_type,
            password=self.password)


class CodeDetail(models.Model):
    code = models.CharField(max_length=14, null=False, unique=True)
    count = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default="unused", null=False)

    def as_json(self):
        return dict(
            code=self.code,
            count=self.count,
            status=self.status)

    @staticmethod
    def generate_uniq_code():
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(14))


