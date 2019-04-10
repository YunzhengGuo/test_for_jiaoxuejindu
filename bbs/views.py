from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator

from .models import Course, ClassRoom, shiyongqingkuang,class_table,major_table,jiaoxuejindu_table,xueqi_table,teacher_table,jiaoxue_task_book_table,ke_table,xueyuan_table


from .forms import CourseForm,ClassRoomForm,shiyongqingkuangForm,class_tableForm,major_tableForm,jiaoxuejindu_tableForm,xueqi_tableForm,teacher_tableForm,jiaoxue_task_book_tableForm,ke_tableForm,xueyuan_tableForm

from .models import Question, Choice
from .forms import ChoiceForm,QuestionForm
# Create your views here
#FBV function based view
#CBV class based view

# Create your views here
#FBV function based view
#CBV class based view
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    query = request.GET.get('q')
    # print(query)
    if query:
        latest_question_list= latest_question_list.filter(
            Q(question_text__icontains=query)|
            Q(author__username__icontains=query)
        ).distinct()#区分查询的结果
    template = loader.get_template('bbs/index.html')
    form  = QuestionForm()
    context = {
        'latest_question_list':latest_question_list,
        'current_user':{'user':request.user,'is_login':request.user.is_authenticated },
        'form':form,

    }
    return HttpResponse(template.render(context, request))
class QuestionListView(ListView):
    model = Question
    context_object_name = 'latest_question_list'

    template_name = 'bbs/index.html'
    paginate_by=10
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['current_user'] = {'user':self.request.user, 'is_login':self.request.user.is_authenticated}
        context['form'] = QuestionForm()       
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        print(f'queryset:{queryset}')
        query = self.request.GET.get('q')
        print(query)
        if query:
            return queryset.filter(
                Q(question_text__icontains=query)
                |
                Q(author__username__icontains=query)
            ).distinct().order_by('-pub_date')

        return queryset.order_by('-pub_date')



@method_decorator(login_required, name='dispatch')
class TopicUpdateView(UpdateView):
    model = Question
    template_name = 'bbs/detail.html'
    def post(self, request, *args, **kwargs):
        pk = request.POST.get('pk')
        if pk:
            question = get_object_or_404(Question,pk=pk)
            # print('get question by pk :' , pk, question)
            question.question_text = request.POST['question_text']
            question.save()
            return HttpResponseRedirect(reverse('bbs:detail', args=(pk,)))
     

class TopicCreateView(CreateView):
    model = Question
    template_name = 'bbs/index.html'
    fields = ('question_text','picture')
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        question = form.save(commit=False)
        question.author = self.request.user
        question.save()
        return redirect('bbs:index')



def detail(request,question_id):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('bbs/index.html')
    form = ChoiceForm()
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'latest_question_list':latest_question_list,
        'question':question,
        'current_user':{'user':request.user,'is_login':request.user.is_authenticated },
        'form':form,

    }
        # question = Question.objects.get(pk=question_id)
   
    return render(request, 'bbs/detail.html', context)

@login_required
def topic(request):
   
    if request.method == 'POST': 
        #判断pk存在的情况下只更新数据
        pk = request.POST.get('pk')
        if pk:
            question = get_object_or_404(Question, pk=pk)
            print(f'get question by pk :{pk},{question}')
            question.question_text = request.POST['question_text']
            question.save()  
            return HttpResponseRedirect(reverse('bbs:detail',args=(pk,)))  
        form = QuestionForm(request.POST, request.FILES or None)
        print('form',form,request.FILES)
        # 判断合法 并保存
        if form.is_valid():
            question = form.save(commit=False)
            # print('question',question, type(question))
            question.author = request.user
            # question.question = question
            # question.picture = request.FILES['picture']
            question.save()
    return HttpResponseRedirect(reverse('bbs:index'))



def replay(request, question_id):
    # return HttpResponse("You're voting on question %s."%question_id)
    question = get_object_or_404(Question, pk=question_id)
    # print(question)
    try:
        if request.method == 'POST':    
            form = ChoiceForm(request.POST, request.FILES or None)
            print('form',form,request.FILES)
            if form.is_valid():
                reply1 = form.save(commit=False)
                print('reply1',reply1, type(reply1))
                reply1.author = request.user
                reply1.question = question
                # reply1.picture = request.FILES['picture']
                reply1.save()

        else:
            return render(request, 'bbs/detail.html',{'question':question,'error_message':'没有数据！'})
        # selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # print(request.POST['choice'])
    except (KeyError):
        return render(request, 'bbs/detail.html', {
            "question":question,
        "error_message":"传值错误", 
        })
    else:
        # selected_choice.votes += 1
        # selected_choice.save()

        return HttpResponseRedirect(reverse('bbs:detail', args=(question.id,)))


@login_required
def my_page(request):
    latest_question_list = Question.objects.order_by('-pub_date').filter(author=request.user)

    form = QuestionForm()
    context = {
        'latest_question_list':latest_question_list,
        'current_user':{'user':request.user, 'is_login':request.user.is_authenticated},
        'form': form
    }
    return render(request, 'bbs/my_page.html', context)