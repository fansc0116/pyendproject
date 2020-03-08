# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAdmin(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=500, blank=True, null=True)
    t_pwd = models.CharField(max_length=500, blank=True, null=True)
    t_flag = models.CharField(max_length=500, blank=True, null=True)
    column_5 = models.CharField(db_column='Column_5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_6 = models.CharField(db_column='Column_6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_7 = models.CharField(db_column='Column_7', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_admin'


class TArtide(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_pic = models.CharField(max_length=500, blank=True, null=True)
    t_title = models.CharField(max_length=500, blank=True, null=True)
    t_time = models.CharField(max_length=500, blank=True, null=True)
    t_content = models.CharField(max_length=500, blank=True, null=True)
    t_category = models.CharField(max_length=500, blank=True, null=True)
    t_tid = models.CharField(max_length=500, blank=True, null=True)
    t_contentpic = models.CharField(max_length=500, blank=True, null=True)
    column_9 = models.CharField(db_column='Column_9', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_10 = models.CharField(db_column='Column_10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_11 = models.CharField(db_column='Column_11', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_artide'


# 轮播图
class TSlideshow(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_url = models.ImageField(upload_to='img')
    t_title = models.CharField(max_length=500, blank=True, null=True)
    t_flag = models.CharField(max_length=500, blank=True, null=True)
    t_createtime = models.CharField(max_length=500, blank=True, null=True)
    column_6 = models.CharField(db_column='Column_6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_7 = models.CharField(db_column='Column_7', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_slideshow'


class TTeacher(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_pic = models.CharField(max_length=500, blank=True, null=True)
    t_name = models.CharField(max_length=500, blank=True, null=True)
    t_flag = models.CharField(max_length=500, blank=True, null=True)
    column_5 = models.CharField(db_column='Column_5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_6 = models.CharField(db_column='Column_6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_7 = models.CharField(db_column='Column_7', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_teacher'


# 用户
class TUser(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=500, blank=True, null=True)
    t_tel = models.CharField(max_length=500, blank=True, null=True)
    t_pwd = models.CharField(max_length=500, blank=True, null=True)
    t_salt = models.CharField(max_length=500, blank=True, null=True)
    t_add = models.CharField(max_length=500, blank=True, null=True)
    t_pic = models.ImageField(upload_to='img')
    t_nota = models.CharField(max_length=500, blank=True, null=True)
    t_sex = models.CharField(max_length=500, blank=True, null=True)
    t_flag = models.CharField(max_length=500, blank=True, null=True)
    t_add1 = models.CharField(max_length=500, blank=True, null=True)
    column_12 = models.CharField(db_column='Column_12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_13 = models.CharField(db_column='Column_13', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_user'


class TVoice(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_title = models.CharField(max_length=500, blank=True, null=True)
    t_url = models.CharField(max_length=500, blank=True, null=True)
    t_duration = models.CharField(max_length=500, blank=True, null=True)
    t_vlid = models.CharField(max_length=500, blank=True, null=True)
    t_size = models.CharField(max_length=500, blank=True, null=True)
    column_9 = models.CharField(db_column='Column_9', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_10 = models.CharField(db_column='Column_10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_11 = models.CharField(db_column='Column_11', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_voice'


class TVoicelist(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_pic = models.CharField(max_length=500, blank=True, null=True)
    t_title = models.CharField(max_length=500, blank=True, null=True)
    t_grade = models.CharField(max_length=500, blank=True, null=True)
    t_time = models.CharField(max_length=500, blank=True, null=True)
    t_author = models.CharField(max_length=500, blank=True, null=True)
    t_announcer = models.CharField(max_length=500, blank=True, null=True)
    t_count = models.CharField(max_length=500, blank=True, null=True)
    t_content = models.CharField(max_length=500, blank=True, null=True)
    column_10 = models.CharField(db_column='Column_10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_11 = models.CharField(db_column='Column_11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_12 = models.CharField(db_column='Column_12', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_voicelist'


class TWork(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_title = models.CharField(max_length=500, blank=True, null=True)
    t_time = models.CharField(max_length=500, blank=True, null=True)
    t_count = models.CharField(max_length=500, blank=True, null=True)
    t_wlid = models.CharField(max_length=500, blank=True, null=True)
    column_6 = models.CharField(db_column='Column_6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_7 = models.CharField(db_column='Column_7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_8 = models.CharField(db_column='Column_8', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_work'


class TWorklist(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_title = models.CharField(max_length=500, blank=True, null=True)
    t_category = models.CharField(max_length=500, blank=True, null=True)
    t_uid = models.CharField(max_length=500, blank=True, null=True)
    column_6 = models.CharField(db_column='Column_6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_7 = models.CharField(db_column='Column_7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_8 = models.CharField(db_column='Column_8', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_worklist'
