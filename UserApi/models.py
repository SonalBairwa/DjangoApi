import random, string


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

    def __str__(self):
        return self.email


class CodeDetail(models.Model):
    code = models.CharField(max_length=14, null=False, unique=True)
    count = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default="unused", null=False)

    def as_json(self):
        return dict(
            code=self.code,
            count=self.count,
            status=self.status)

    def __str__(self):
        return self.code

    @staticmethod
    def generate_uniq_code():

        x = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        return x
        #return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(14))


