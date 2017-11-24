# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CheckoutOrder(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    date_time = models.CharField(max_length=255, blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    user = models.ForeignKey('UserAccount', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.date_time

    class Meta:
        managed = False
        db_table = 'checkout_order'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True 
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Item(models.Model):
    itemid = models.BigAutoField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    option_value = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    order = models.ForeignKey(CheckoutOrder, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        if self.city is None: 
            return self.country
        else:
            return self.country + " " + self.city
    class Meta:
        managed = True 
        db_table = 'item'


class PasswordResetToken(models.Model):
    id = models.BigAutoField(primary_key=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('UserAccount', on_delete=models.CASCADE)
    def __str__(self):
        return self.token
    class Meta:
        managed = True 
        db_table = 'password_reset_token'


class Role(models.Model):
    role_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        managed = True 
        db_table = 'role'


class SpringSession(models.Model):
    session_id = models.CharField(db_column='SESSION_ID', primary_key=True, max_length=36)  # Field name made lowercase.
    creation_time = models.BigIntegerField(db_column='CREATION_TIME')  # Field name made lowercase.
    last_access_time = models.BigIntegerField(db_column='LAST_ACCESS_TIME')  # Field name made lowercase.
    max_inactive_interval = models.IntegerField(db_column='MAX_INACTIVE_INTERVAL')  # Field name made lowercase.
    principal_name = models.CharField(db_column='PRINCIPAL_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.session_id
    class Meta:
        managed = True 
        db_table = 'spring_session'


class SpringSessionAttributes(models.Model):
    session = models.ForeignKey(SpringSession, db_column='SESSION_ID', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    attribute_name = models.CharField(db_column='ATTRIBUTE_NAME', max_length=200)  # Field name made lowercase.
    attribute_bytes = models.TextField(db_column='ATTRIBUTE_BYTES', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.attribute_name
    class Meta:
        managed = True 
        db_table = 'spring_session_attributes'
        unique_together = (('session', 'attribute_name'),)


class UserAccount(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    contact_no = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.user_name
    class Meta:
        managed = True 
        db_table = 'user_account'


class UserRole(models.Model):
    user = models.ForeignKey(UserAccount, primary_key=True, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        managed = True 
        db_table = 'user_role'
        unique_together = (('user', 'role'),)
