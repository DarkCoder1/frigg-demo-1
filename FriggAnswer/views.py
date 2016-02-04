#/usr/bin/python
# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from backend.MongoFeedback import MongoFeedback
import json

from .forms import FriggForm, UploadForm, FeedbackForm
from .models import answer, answer_file
from messages import intro_message

feedback = MongoFeedback()

def question_view(request):
    feed = FeedbackForm()
    ans = intro_message()
    form = FriggForm()
    context={"form": form, "intro": ans, "feedback": feed}
    return render_to_response("FriggTemplates/index.html", context ,RequestContext(request), RequestContext(request))

def ajax_answer(request):
    print 'vim até aqui'
    if request.method == 'POST':
        form = FriggForm(request.POST)
        #print 'segundo ponto de teste'
        if form.is_valid():
            quest = request.POST['question']
        ans = answer(quest)
        context={"answer": ans}
        return HttpResponse(
            json.dumps(context),
            content_type="application/json")

def custom_404(request):
    return render(request, 'FriggTemplates/404.html', {}, status=404)

def upload_view(request):
    ans = "Pode carregar o arquivo"
    if request.method == 'POST':
        up_form = UploadForm(request.POST, request.FILES)
        ques_form = FriggForm(request.POST)
        if up_form.is_valid() and ques_form.is_valid:
    	    text = request.FILES['file']
            ques = request.POST['question']
	    ans = answer_file(ques, text)
	    context={"up_form": up_form, "question_form":ques_form, "subtest": ans}
	    return render(request, "FriggTemplates/upload.html", context)
	    return HttpResponse("/FriggResponse/")
    #acontece de qualquer forma...
    up_form = UploadForm()
    ques = FriggForm()
    context={"up_form": up_form, "question_form":ques, "subtest": ans}
    return render_to_response("FriggTemplates/upload.html", context ,RequestContext(request), RequestContext(request))