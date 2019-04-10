import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from markdown import markdown
# Create your models here.


class Course(models.Model):
    """课程表"""

    course_name = models.CharField("课程名",max_length=20)
    course_id = models.CharField('课程号',max_length=6)
    course_for_major  = models.CharField('专业课程',max_length=20)
    course_times  = models.CharField('课时',max_length=6)

    def __str__(self):
        return self.course_name
    
    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = '课程表'
        
class ClassRoom(models.Model):
    """教室表"""

    classRoom_id =  models.CharField("教室号",max_length=6)
    classRoom_name = models.CharField("教室名",max_length=20)
    rongliang = models.CharField("容量 ",max_length=8)
    didian  = models.CharField("地点",max_length=8)
    leixing  = models.CharField("类型",max_length=10)
    shi_yong_qing_kuang  = models.CharField("使用情况",max_length=6)
 

    def __str__(self):
        return self.classRoom_name
    
    class Meta:
        verbose_name = '教室信息 '
        verbose_name_plural = '教室表'

class shiyongqingkuang(models.Model):
    """使用情况表
    """
    syqk_id =  models.CharField("使用情况号",max_length=6)
    syqk_class = models.CharField("使用班级",max_length=8)
    shiyongtime = models.CharField("使用",max_length=8)
    shiyong_bool  = models.CharField("使用与否",max_length=4)

    def __str__(self):
        return self.syqk_id
    
    class Meta:
        verbose_name = '使用情况信息'
        verbose_name_plural = '使用情况表'

class class_table(models.Model):
    """班级表
    """
    class_id =  models.CharField('班级号',max_length=6)
    class_name = models.CharField('班级名称',max_length=8)
    people = models.CharField('班级人数',max_length=8)
    year  = models.CharField('入学年份',max_length=6)
    hebanhao  = models.CharField('合班号',max_length=6)
    zhuanyehao  = models.CharField('专业号',max_length=6)


    def __str__(self):
        return self.class_name
    
    class Meta:
        verbose_name = '班级信息'
        verbose_name_plural = '班级表'

class major_table(models.Model):
    """专业表
    """
    zhuanyehao_id =  models.CharField('专业号',max_length=6)
    zhuanye_name = models.CharField('专业名称',max_length=28)
    college = models.CharField("学院",max_length=20)
    people = models.CharField('人数',max_length=8)
    year  = models.CharField('入学年份',max_length=6)
    hebanhao  = models.CharField('合班号',max_length=6)
    zhuanyehao  = models.CharField('专业号',max_length=6)


    def __str__(self):
        return self.zhuanye_name
    
    class Meta:
        verbose_name = '专业信息 '
        verbose_name_plural = '专业表'

class jiaoxuejindu_table(models.Model):
    """教学进度表
    """
    zhuanye_jiaoxue_jindu_id =  models.CharField('专业教学进度号',max_length=6)
    xuenian_xueqi_hao = models.CharField('学年学期号',max_length=28)
    course_name = models.CharField("课程名",max_length=20)
    xueshi_nums = models.CharField("学时数",max_length=20)
    start_end_weeks = models.CharField("起始周",max_length=20)
    weeks_times =  models.CharField("周学时",max_length=4)
    zhuanyehao  = models.CharField('专业号',max_length=6)

    def __str__(self):
        return self.xuenian_xueqi_hao
    
    class Meta:
        verbose_name = '教学进度信息'
        verbose_name_plural = '教学进度表'

class xueqi_table(models.Model):
    """学期表
    """
    
    xuenian_xueqi_hao = models.CharField('学年学期号',max_length=28)
    ruxue_xuenian = models.CharField('入学学年',max_length=28)
    xueqi = models.CharField('学期',max_length=28)
    
    def __str__(self):
        return self.xuenian_xueqi_hao
    
    class Meta:
        verbose_name = '学年学期信息'
        verbose_name_plural = '学年学期表'

class teacher_table(models.Model):
    """学期表
    """
    
    teacher_hao = models.CharField('教师号',max_length=6)
    xueyuan = models.CharField('学院',max_length=28)
    zhicheng = models.CharField('职称',max_length=28)
    name = models.CharField('姓名',max_length=28)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '学期信息'
        verbose_name_plural = '学期表'

class jiaoxue_task_book_table(models.Model):
    """教学任务书
    """
    
    teacher_hao = models.CharField('教师号',max_length=6)
    xueyuan = models.CharField('学院',max_length=28)
    jiaoyanshi = models.CharField('教研室', max_length=10)
    class_id = models.CharField('班级号',max_length=10)
    zhuanye_hao = models.CharField('专业号',max_length=10)
    heban_hao = models.CharField('合班',max_length=6)
    
    def __str__(self):
        return self.teacher_hao
    
    class Meta:
        verbose_name = '教学任务书信息'
        verbose_name_plural = '教学任务书'

class ke_table(models.Model):
    """课表
    """
    
    day_of_week = models.CharField('教师号',max_length=6)
    shiduan = models.CharField("时段",max_length=4)
    heban_hao = models.CharField('合班',max_length=6)
    kecheng = models.CharField('课程',max_length=6)
    jiaoshi = models.CharField('教室',max_length=6)
    teacher = models.CharField("教师",max_length=10)
    class Meta:
        verbose_name = '课表信息'
        verbose_name_plural = '课表'

class xueyuan_table(models.Model):
    """学院表
    """
    xueyuan_hao = models.CharField("学院号",max_length=6)
    xueyuan_name = models.CharField("学院名",max_length=20)
    tel = models.CharField("电话",max_length=12)
    class Meta:
        verbose_name = '学院信息'
        verbose_name_plural = '学院表'
    
class Question(models.Model):
    question_text = models.CharField('问题',max_length=200)
    pub_date = models.DateTimeField('发布时间',auto_now_add=True)
    # author = models.CharField(max_length=50, default="gyz")
    author = models.ForeignKey(User, default=1 , on_delete=models.CASCADE,verbose_name='作者')
    picture = models.FileField('图片内容',blank=True,null=True)   
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=2)

    class Meta:
        verbose_name = '回复'
        verbose_name_plural = '问题'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,verbose_name='问题')
    # choice_text = models.CharField(max_length=200)
    choice_text = models.TextField('回复',max_length=2000)
    # author = models.CharField(max_length=50, default='gyz')
    author = models.ForeignKey(User, default=1 , on_delete=models.CASCADE,verbose_name='作者')
    picture = models.FileField(blank=True,null=True)    
    def get_choice_text_md(self):
        return mark_safe(markdown(self.choice_text))

    def __str__(self):
        return self.choice_text
    
    class Meta:
        # verbose_name = '回复'
        verbose_name_plural = '回复'