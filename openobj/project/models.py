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
    EASY = 1
    MID = 2
    HARD = 3
    DIFF_TYPE = (
        (EASY, '初级'),
        (MID, '中级'),
        (HARD, '高级'),
    )

    OPEN = 'open'
    CLOSE = 'close'
    CODE_PATTER = (
        (OPEN, '开源'),
        (CLOSE, '闭源'),
    )

    GITHUB = 'github'
    OSCHINA = 'oschina'
    CODING = 'coding'
    PERSONAL = 'personal'
    REPOSITORY_OTHER = 'other'
    REPOSITORY = (
        (GITHUB, 'Github'),
        (OSCHINA, '开源中国'),
        (CODING, 'Coding'),
        (PERSONAL, '个人仓库'),
        (REPOSITORY_OTHER, '其他'),
    )
    guid = models.AutoField(primary_key=True)
    owner_user = models.ForeignKey(UserAccount, verbose_name="拥有者")
    title = models.CharField(max_length=128, verbose_name="标题")
    description = models.TextField(verbose_name="描述")
    classify = models.ManyToManyField(ProjectClassifySecond, verbose_name="类别")
    creation_time = models.DateTimeField(default=now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=now, verbose_name="更新时间", blank=True, null=True)
    difficulty = models.IntegerField(choices=DIFF_TYPE, default=EASY, verbose_name="难度")
    code_pattern = models.CharField(max_length=32, choices=CODE_PATTER, default=OPEN, verbose_name="代码形式")
    repository = models.CharField(max_length=32, choices=REPOSITORY, default=GITHUB, verbose_name="托管方式")
    read_num = models.IntegerField(default=0, verbose_name="浏览数")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "project"
        verbose_name = "项目表"
