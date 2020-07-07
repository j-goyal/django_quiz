from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from quiz.models import Contact, Question
from datetime import datetime

# Create your views here.

def home(request):
    return render(request, 'home.html')


def quiz(request):
    return render(request, 'quiz.html')


def create_quiz(request):
    if request.method=="POST":
        question = request.POST.get('ques')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        cor_option = request.POST.get('cor_option')

        if cor_option =='Select Option':
            messages.warning(request, "Warning! Please select a correct option for your question.")
            return redirect('/create_quiz/')


        obj = Question(ques=question,option1=option1, option2=option2, option3=option3, option4=option4, cor_option=cor_option)
        obj.save()

        messages.success(request, "Success! Question Added Successfully.")

        questions = Question.objects.all()  # query set
        context = {'questions':questions}   # passing model into template
        return render(request, 'create_quiz.html', context)



    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request,'create_quiz.html',context)



def solve(request, ques_id):
    question = Question.objects.get(pk=ques_id)

    if request.method=="POST":
        answer = request.POST.get('ques')
        if answer == question.cor_option:
            messages.success(request, "Yeeey! Right answer. Check out other questions")
            return redirect('create_quiz')
        else:
            messages.warning(request, "Oops! Wrong answer. TRY again!")

    
    context = {'question':question}
    return render(request,'solve.html', context)


def delete(request, ques_id):
    question = Question.objects.get(pk=ques_id)
    question.delete()
    messages.success(request, "Successfully deleted question")
    return redirect('create_quiz')



def make_quiz(request):
    questions = Question.objects.all()

    if len(questions) <= 2:
        messages.warning(request,"Please add atleast 3 questions to make quiz")
        return redirect('/create_quiz/')
    

    li=[]
    cor_ans = []
    for i in questions:
        li.append(str(i.id))
        cor_ans.append(str(i.cor_option))

    if request.method == "POST":
        res = [] 
        count = 0
        for i in li:
            res.append(request.POST.get(i))

        for j in range(0,len(res)):
            if cor_ans[j] == res[j]:
                count += 1

        if res.count(None)==len(res):
            messages.warning(request,'Warning! Please select option for atleast one question.')
            return redirect('/make_quiz/')

        messages.success(request,"Your score: %d/%d " %(count, len(res))) # always remember to do this
        return redirect('/make_quiz/')

        #context = {'questions':questions,'title':'Your Score - ', 'outof':'/', 'total':len(res), 'score':count, 'flag':True}
        #return render(request,'make_quiz.html',context)


    context = {'questions':questions}
    return render(request, 'make_quiz.html', context)




def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')

        if len(name)<2 or len(email)<6 or len(phone)<10 or len(content)<4:
            messages.warning(request, "Warning! Please fill the form correctly")
        
        else:
            contact = Contact(name=name, phone=phone, email=email, content=content, timestamp=datetime.today())  # create obj of Contact class
            contact.save()
            messages.success(request, "Hurreey! Your form has been Successfully Submitted")



    return render(request, 'contact.html')


def quiz1(request):
    if request.method=='POST':
        flag=1
        original_solutions= ['ans12','ans22','ans32']

        ans1 = request.POST.get('q1')
        ans2 = request.POST.get('q2')
        ans3 = request.POST.get('q3')

        res = []
        res.append(ans1)
        res.append(ans2)
        res.append(ans3)

        if res.count(None)==len(res):
            flag=0
            messages.warning(request,'Warning! Please select option for atleast one question.')
            return redirect('/quiz1')
                
        c=0
        for i in res:
            if i in original_solutions:
                c=c+1

        #context = {'total':len(res), 'score':c, 'flag':flag}
        messages.info(request, {'title':'You score:', 'total':len(res), 'score':c, 'flag':flag})
        #return render(request,'quiz1.html', context)


    return render(request,'quiz1.html')