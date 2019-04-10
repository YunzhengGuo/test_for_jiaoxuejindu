from django.contrib import admin

# Register your models here.
# from .models import Question, Choice
from .models import Course, ClassRoom, shiyongqingkuang,class_table,major_table,jiaoxuejindu_table,xueqi_table,teacher_table,jiaoxue_task_book_table,ke_table,xueyuan_table
# actions_on_top=True
class CourseAdmin(admin.ModelAdmin):
    list_display=('course_name', 'course_id', 'course_for_major','course_times')

    list_editable=('course_name', 'course_id', 'course_for_major','course_times')
   
    list_filter=('course_id', 'course_name', 'course_times')
    search_fields=('course_name', 'course_id', 'course_for_major','course_times')
    list_display_links=None
    list_per_page=10
admin.site.register(Course, CourseAdmin)

class ClassRoomAdmin(admin.ModelAdmin):
    list_display=('classRoom_id', 'classRoom_name', 'rongliang','didian','leixing','shi_yong_qing_kuang'
    )

    list_editable=('classRoom_id', 'classRoom_name', 'rongliang','didian','leixing','shi_yong_qing_kuang'
    )
   
    list_filter=('classRoom_id', 'classRoom_name',)
    search_fields=('classRoom_id', 'classRoom_name', 'rongliang','didian','leixing','shi_yong_qing_kuang'
    )
    list_display_links=None
    list_per_page=10
admin.site.register(ClassRoom, ClassRoomAdmin)

class shiyongqingkuangAdmin(admin.ModelAdmin):
    list_display=('syqk_id', 'syqk_class', 'shiyongtime','shiyong_bool')

    list_editable=('syqk_id', 'syqk_class', 'shiyongtime','shiyong_bool')
   
    list_filter=('syqk_id', 'syqk_class',)
    search_fields=('syqk_id', 'syqk_class', 'shiyongtime','shiyong_bool')
    list_display_links=None
    list_per_page=10
admin.site.register(shiyongqingkuang, shiyongqingkuangAdmin)

class class_tableAdmin(admin.ModelAdmin):
    list_display=('class_id', 'class_name', 'people','year','hebanhao','zhuanyehao')

    list_editable=('class_id', 'class_name', 'people','year','hebanhao','zhuanyehao')
   
    list_filter=('class_id', 'class_name',)
    search_fields=('class_id', 'class_name', 'people','year','hebanhao','zhuanyehao')
    list_display_links=None
    list_per_page=10
admin.site.register(class_table, class_tableAdmin)

class major_tableAdmin(admin.ModelAdmin):
    list_display=('zhuanyehao_id', 'zhuanye_name', 'college','people','year','zhuanyehao','hebanhao')

    list_editable=('zhuanyehao_id', 'zhuanye_name', 'college','people','year','zhuanyehao','hebanhao')
   
    list_filter=('zhuanyehao_id', 'zhuanye_name', )
    search_fields=('zhuanyehao_id', 'zhuanye_name', 'college','people','year','zhuanyehao','hebanhao')
    list_display_links=None
    list_per_page=10
admin.site.register(major_table, major_tableAdmin)

class jiaoxuejindu_tableAdmin(admin.ModelAdmin):
    list_display=('zhuanye_jiaoxue_jindu_id', 'xuenian_xueqi_hao', 'course_name','xueshi_nums','start_end_weeks','weeks_times','zhuanyehao')

    list_editable=('zhuanye_jiaoxue_jindu_id', 'xuenian_xueqi_hao', 'course_name','xueshi_nums','start_end_weeks','weeks_times','zhuanyehao')
   
    list_filter=('zhuanye_jiaoxue_jindu_id', 'xuenian_xueqi_hao',)
    search_fields=('zhuanye_jiaoxue_jindu_id', 'xuenian_xueqi_hao', 'course_name','xueshi_nums','start_end_weeks','weeks_times','zhuanyehao')
    list_display_links=None
    list_per_page=10
admin.site.register(jiaoxuejindu_table, jiaoxuejindu_tableAdmin)

class xueqi_tableAdmin(admin.ModelAdmin):
    list_display=('xuenian_xueqi_hao', 'ruxue_xuenian', 'xueqi')

    list_editable=('xuenian_xueqi_hao', 'ruxue_xuenian', 'xueqi')
   
    list_filter=('xuenian_xueqi_hao', 'ruxue_xuenian',)
    search_fields=('xuenian_xueqi_hao', 'ruxue_xuenian', 'xueqi')
    list_display_links=None
    list_per_page=10
admin.site.register(xueqi_table, xueqi_tableAdmin)

class teacher_tableAdmin(admin.ModelAdmin):
    list_display=('teacher_hao', 'xueyuan', 'zhicheng','name')

    list_editable=('teacher_hao', 'xueyuan', 'zhicheng','name')
   
    # list_filter=('', '',)
    search_fields=('teacher_hao', 'xueyuan', 'zhicheng','name')
    list_display_links=None
    list_per_page=10
admin.site.register(teacher_table, teacher_tableAdmin)

class jiaoxue_task_book_tableAdmin(admin.ModelAdmin):
    list_display=('teacher_hao', 'xueyuan', 'jiaoyanshi','class_id','zhuanye_hao','heban_hao')

    list_editable=('teacher_hao', 'xueyuan', 'jiaoyanshi','class_id','zhuanye_hao','heban_hao')
   
    list_filter=('teacher_hao', 'xueyuan',)
    search_fields=('teacher_hao', 'xueyuan', 'jiaoyanshi','class_id','zhuanye_hao','heban_hao')
    list_display_links=None
    list_per_page=10
admin.site.register(jiaoxue_task_book_table, jiaoxue_task_book_tableAdmin)

class ke_tableAdmin(admin.ModelAdmin):
    list_display=('day_of_week', 'shiduan', 'heban_hao','kecheng','jiaoshi','teacher')

    list_editable=('day_of_week', 'shiduan', 'heban_hao','kecheng','jiaoshi','teacher')
   
    list_filter=('day_of_week', 'shiduan',)
    search_fields=('day_of_week', 'shiduan', 'heban_hao','kecheng','jiaoshi','teacher')
    list_display_links=None
    list_per_page=10
admin.site.register(ke_table, ke_tableAdmin)

class xueyuan_tableAdmin(admin.ModelAdmin):
    list_display=('xueyuan_hao', 'xueyuan_name', 'tel')

    list_editable=('xueyuan_hao', 'xueyuan_name', 'tel')
   
    list_filter=('xueyuan_hao', 'xueyuan_name',)
    search_fields=('xueyuan_hao', 'xueyuan_name', 'tel')
    list_display_links=None
    list_per_page=10
admin.site.register(xueyuan_table, xueyuan_tableAdmin)



# from .models import Question, Choice
# class QuestionAdmin(admin.ModelAdmin):
#     list_display=('question_text', 'author', 'pub_date')
#     list_editable=('question_text','author',)
#     list_filter=('question_text', 'author', 'pub_date')
#     search_fields=('question_text',)
#     list_display_links=None
#     list_per_page=10
# # 
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display=('question', 'choice_text',  'author')
#     list_editable=('choice_text', 'question')
#     list_filter=( 'choice_text',  'author')
#     search_fields=('choice_text', )
#     list_display_links=None
#     list_per_page=10

# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)