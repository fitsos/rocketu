# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from orm_app.models import Poll, PollAnswer, Comment
from orm_app.forms import PollAnswerForm, PollQuestionForm
from forms import SignupForm, User
# from django.views.decorators.cache import cache_page
from django.core.cache import cache
import requests

def money(requests):
    # url = "http://www.cnet.com/"
    url = "http://bootcamp-rocketu.rhcloud.com/exercises/moviepicker/assets/data/movies.json"
    data = requests.get(url)
    # cache.set(url, data, 300)
    # cached_data = cache.GET(url)
    render(requests, 'money.html', data)
    #return HttpResponse(data)

def money(requests):
    # url = "http://www.cnet.com/"
    url = "http://bootcamp-rocketu.rhcloud.com/exercises/moviepicker/assets/data/movies.json"
    data = requests.get(url)
    # cache.set(url, data, 300)
    # cached_data = cache.GET(url)
    render(requests, 'money.html', data)
    #return HttpResponse(data)



def poll(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    data = {
        "poll": poll
    }
    return render(request, "poll.html",data)

def poll_results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    data = {
        "poll": poll,
        "results":True,
    }
    return render(request, "poll.html",data)

def add_poll_answer(request):
    data = {}
    if request.method == "POST":
        my_form = PollAnswerForm(request.POST)
        if my_form.is_valid():
            poll = my_form.cleaned_data["poll"]
            new_answer = my_form.cleaned_data["answer"]

            answer = PollAnswer(poll=poll, answer=new_answer)
            answer.save()

            data["message"] = "Answer saved."
    else:
        my_form = PollQuestionForm['']

    data["poll_form"] = my_form
    return render(request, "my_form.html", data)

def add_poll_question(request):
    data = {}
    if request.method == "POST":
        fq = PollQuestionForm(request.POST)
        if fq.is_valid():
            new_question = fq.cleaned_data["question"]
            answer = PollQuestion(poll=question, question=new_question)
            answer.save()

            data["message"] = "Answer saved."
    else:
        fq = PollQuestionForm()

    data["poll_form"] = fq
    return render(request, "fq.html", data)

def latest_poll(request):
    data = {"latest": Poll.objects.latest("pk")}
    return render(
        request,
        "admin/latest_poll.html",
        data
    )

def my_form_view(request):
    data = {}
    render(request, 'my_form.html', data)

# @cache_page(900)
# def test(request):
#     data = {}
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#                 form.cleaned_data["username"],
#                 form.cleaned_data["email"],
#                 form.cleaned_data["password"],
#             )
#             response = HttpResponse("Good job, you submited")
#             return response
#     else:
#         form = SignupForm()
#
#     data["form"] = form
#     return render(request, "test.html", data)




