from django import forms
from .models import Course, ClassRoom, shiyongqingkuang,class_table,major_table,jiaoxuejindu_table,xueqi_table,teacher_table,jiaoxue_task_book_table,ke_table,xueyuan_table
from django import forms
from .models import Choice, Question


class ChoiceForm(forms.ModelForm):
    choice_text = forms.CharField(
        
        label="你的答案",
        max_length =2000,
        
        help_text= "最大长度为2000",
        widget=forms.Textarea(
            attrs={
                'placeholder':'请说出的答案',
                "rows":8,
                'class' : 'form-control'
                
            }
        )
        )
   
    class Meta:
        model = Choice
        fields = ['choice_text','picture']

class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(
        
        label="问题",
        max_length =200,
        
        help_text= "最大长度为200",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入想问的话题',
                'class' : 'form-control'
                
            }
        )
        )
   
    class Meta:
        model = Question
        fields = ['question_text','picture']
class CourseForm(forms.ModelForm):
    course_name=forms.CharField(
         label="课程表",
        max_length =20,
        help_text= "最大长度为20",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    course_id=forms.CharField(
         label="课程id",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    course_for_major=forms.CharField(
         label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    course_times=forms.CharField(
         label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    class Meta:
        model = Question
        fields = ['question_text','picture']
class ClassRoomForm(forms.ModelForm):
    classRoom_id=forms.CharField(
        #  label="课程表",
        max_length =20,
        help_text= "最大长度为20",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    classRoom_name=forms.CharField(
        #  label="课程id",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    rongliang=forms.CharField(
         label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    didian=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    leixing=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    shi_yong_qing_kuang=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    class Meta:
        model = ClassRoom
        fields = ['classRoom_id', 'classRoom_name', 'rongliang','didian','leixing','shi_yong_qing_kuang']
class shiyongqingkuangForm(forms.ModelForm):
    syqk_id=forms.CharField(
        #  label="课程表",
        max_length =20,
        help_text= "最大长度为20",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    syqk_class=forms.CharField(
        #  label="课程id",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    shiyongtime=forms.CharField(
         label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    shiyong_bool=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    class Meta:
        model = shiyongqingkuang
        fields = ['syqk_id', 'syqk_class', 'shiyongtime','shiyong_bool']
class class_tableForm(forms.ModelForm):
    class_id=forms.CharField(
        #  label="课程表",
        max_length =20,
        help_text= "最大长度为20",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    class_name=forms.CharField(
        #  label="课程id",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    year=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    hebanhao=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    zhuanyehao=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    class Meta:
        model = class_table
        fields = ['class_id', 'class_name', 'people','year','hebanhao','zhuanyehao']
class major_tableForm(forms.ModelForm):
    zhuanyehao_id=forms.CharField(
        #  label="课程表",
        max_length =20,
        help_text= "最大长度为20",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    zhuanye_name=forms.CharField(
        #  label="课程id",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    college=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    people=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    year=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    hebanhao=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    zhuanyehao=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    class Meta:
        model = major_table
        fields = ['zhuanyehao_id', 'zhuanye_name', 'college','people','year','zhuanyehao','hebanhao']
class jiaoxuejindu_tableForm(forms.ModelForm):
    zhuanye_jiaoxue_jindu_id=forms.CharField(
        #  label="课程表",
        max_length =20,
        help_text= "最大长度为20",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    xuenian_xueqi_hao=forms.CharField(
        #  label="课程id",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    course_name=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    xueshi_nums=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    start_end_weeks=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    weeks_times=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    zhuanyehao=forms.CharField(
        #  label="课时",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    class Meta:
        model = jiaoxuejindu_table
        fields = ['zhuanye_jiaoxue_jindu_id', 'xuenian_xueqi_hao', 'course_name','xueshi_nums','start_end_weeks','weeks_times','zhuanyehao']

class xueqi_tableForm(forms.ModelForm):
    xuenian_xueqi_hao=forms.CharField(
        #  label="课程表",
        max_length =20,
        help_text= "最大长度为20",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    ruxue_xuenian=forms.CharField(
        #  label="课程id",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    xueqi=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
   
    class Meta:
        model = xueqi_table
        fields = ['xuenian_xueqi_hao', 'ruxue_xuenian', 'xueqi']

class teacher_tableForm(forms.ModelForm):
    teacher_hao=forms.CharField(
        #  label="课程表",
        max_length =20,
        help_text= "最大长度为20",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    xueyuan=forms.CharField(
        #  label="课程id",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    zhicheng=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    name=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
   
    class Meta:
        model = teacher_table
        fields = ['teacher_hao', 'xueyuan', 'zhicheng','name']
class jiaoxue_task_book_tableForm(forms.ModelForm):
    teacher_hao=forms.CharField(
        #  label="课程表",
        max_length =20,
        help_text= "最大长度为20",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    xueyuan=forms.CharField(
        #  label="课程id",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    jiaoyanshi=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    class_id=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    zhuanye_hao=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    heban_hao=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    class Meta:
        model = jiaoxue_task_book_table
        fields = ['teacher_hao', 'xueyuan', 'jiaoyanshi','class_id','zhuanye_hao','heban_hao']
class ke_tableForm(forms.ModelForm):
    day_of_week=forms.CharField(
        #  label="课程表",
        max_length =20,
        help_text= "最大长度为20",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    shiduan=forms.CharField(
        #  label="课程id",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    heban_hao=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    kecheng=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    jiaoshi=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    teacher=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    class Meta:
        model = ke_table
        fields = ['day_of_week', 'shiduan', 'heban_hao','kecheng','jiaoshi','teacher']
class xueyuan_tableForm(forms.ModelForm):
    xueyuan_hao=forms.CharField(
        #  label="课程表",
        max_length =20,
        help_text= "最大长度为20",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    xueyuan_name=forms.CharField(
        #  label="课程id",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    tel=forms.CharField(
        #  label="专业课程",
        max_length =20,
        help_text= "最大长度为6",
        widget=forms.TextInput(
            attrs={
                'placeholder':'请输入',
                'class' : 'form-control'  
            }
        )
    )
    class Meta:
        model = xueyuan_table
        fields = ['xueyuan_hao','xueyuan_name','tel']




















































































































