from django.db import models
from django.utils.timezone import now
from usercenter.models import UserAccount


class ProjectClassifyFirst(models.Model):
    guid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, verbose_name="一级分类名称")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "project_classify_first"
        verbose_name = "项目一级分类表"


class ProjectClassifySecond(models.Model):
    guid = models.AutoField(primary_key=True)
    classify_first = models.ForeignKey(ProjectClassifyFirst, verbose_name="一级分类名称")
    name = models.CharField(max_length=128, verbose_name="二级分类名称")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "project_classify_second"
        verbose_name = "项目二级分类表"


class Project(models.Model):
    guid = models.AutoField(primary_key=True)
    owner_user = models.ForeignKey(UserAccount, verbose_name="拥有者")
    title = models.CharField(max_length=128, verbose_name="标题")
    description = models.TextField(verbose_name="描述")
    classify = models.ManyToManyField(ProjectClassifySecond, verbose_name="类别")
    creation_time = models.DateTimeField(default=now, verbose_name="创建时间")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "project"
        verbose_name = "项目表"
