from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, contact_no, name, password=None):
        if not contact_no:
            raise ValueError('must have user phone number')
        if not name:
            raise ValueError('must have user name')
        user = self.model(
            contact_no=contact_no,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, contact_no, name, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(contact_no, name, password, **extra_fields)


class User(AbstractBaseUser):
    contact_no = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=100,
                            null=False, blank=False)

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'contact_no'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = [ 'name']

    def __str__(self):
        return self.contact_no

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
