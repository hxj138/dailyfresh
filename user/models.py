from django.db import models
from db.base_model import BaseModel
# Create your models here.


class User(BaseModel):
    '''用户模型类'''
    username=models.CharField(max_length=20,verbose_name='用户名')
    password=models.CharField(max_length=20,verbose_name='密码')
    email=models.EmailField(verbose_name='邮箱')
    is_active=models.CharField(max_length=100,verbose_name='用户是否激活')


    class Meta:
        db_table='df_user'
        verbose_name='用户'
        verbose_name_plural=verbose_name


class Address(BaseModel):
     '''地址模型类'''
     user=models.ForeignKey('User',on_delete=models.CASCADE,verbose_name='所属账户')
     receiver=models.CharField(max_length=20,verbose_name='收件人')
     addr=models.CharField(max_length=256,verbose_name='收件地址')
     zip_code=models.CharField(max_length=6,null=True,verbose_name='邮政编码')
     phone=models.CharField(max_length=11,verbose_name='联系电话')
     is_default=models.BooleanField(default=False,verbose_name='是否默认')

     class Meta:
         db_table='df_adress'
         verbose_name='地址'
         verbose_name_plural=verbose_name