from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from hasker.apps.hasker_main.models import *
from hasker.apps.hasker_main import global_settings
from hasker.apps.hasker_main import forms
import re

import logging


# Create your vplaceiews here.


@require_http_methods(['GET'])
def index(request):
    trending = HaskerQuestion.objects.order_by('-votes')[:global_settings.QUESTION_MAX_TRENDING]

    sorting = request.GET.get('sorting', 'last')
    if sorting == 'last':
        questions = HaskerQuestion.objects.order_by('-date')
    elif sorting == 'hot':
        questions = HaskerQuestion.objects.order_by('-votes')
    else:
        return HttpResponseNotFound()

    page = request.GET.get('page', 1)
    paginator = Paginator(questions, global_settings.QUESTION_PAGE_NUM)
    try:
        questions_page = paginator.page(page)
    except EmptyPage:
        questions_page = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        questions_page = paginator.page(1)

    context = {
        'questions': questions_page,
        'trending': trending,
        'sorting': sorting
    }

    return render(request, 'index.html', context)


def question_detailed(request, question_id):
    question = get_object_or_404(HaskerQuestion, id=question_id)
    return render(request, 'question.html', {'question': question})


@require_http_methods(['GET'])
def search(request):
    form = forms.SearchForm(request.GET)

    if form.is_valid():
        phrase = request.GET.get('phrase', '')

        questions = HaskerQuestion.objects.all()
        if re.match(r'(\s*)#(\w+)', phrase):
            phrase = re.findall(r'\w+', phrase)

            logging.warning(phrase)
            questions = questions.filter(tags__tag__in=phrase)
        else:
            phrase = re.split(r'\s', phrase)
            for word in phrase:
                questions = questions.filter(Q(title__icontains=word) | Q(text__icontains=word))
        questions.order_by('-votes', '-date')

        page = request.GET.get('page', '1')
        paginator = Paginator(questions, global_settings.QUESTION_PAGE_NUM)
        try:
            questions_page = paginator.page(page)
        except EmptyPage:
            questions_page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            questions_page = paginator.page(1)

        trending = HaskerQuestion.objects.order_by('-votes')[:global_settings.QUESTION_MAX_TRENDING]
        context = {
            'questions': questions_page,
            'trending': trending
        }

        return render(request, 'search.html', context)
    else:
        return HttpResponseRedirect('/')


@csrf_protect
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.POST:
        user_form = forms.LoginForm(request.POST)

        if user_form.is_valid():
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            user_login = auth.authenticate(username=username, password=password)

            logging.warning(user_login is not None)
            if user_login is not None:
                if user_login.is_active:
                    auth.login(request, user_login)
                    return HttpResponseRedirect('/')
            else:
                return HttpResponse('did not find user')
        else:
            return HttpResponseRedirect('/login')
    else:
        return render(request, 'login.html', {})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


@csrf_protect
@require_http_methods(['GET', 'POST'])
def register(request):
    context = {}

    if request.POST:
        user_form = forms.RegistrationForm(request.POST)
        if user_form.is_valid():
            user = User.objects.create_user(
                request.POST.get('username'),
                request.POST.get('email'),
                request.POST.get('password'),
            )
            user.save()
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/register')
    else:
        return render(request, 'register.html', context)


@csrf_protect
@require_http_methods(['GET', 'POST'])
def asking(request):
    if request.POST:
        question_form = forms.AskingForm(request.POST)
        logging.warning(question_form.is_valid())
        if question_form.is_valid():
            title = request.POST.get('title')
            text = request.POST.get('text')
            tags = []

            logging.warning(title)
            logging.warning(text)
            logging.warning(title and text)
            if title and text:  # run by tags
                tags_all = HaskerTag.objects.all()
                for tag in tags_all:
                    if tag.tag in request.POST.keys():
                        tags.append(tag)

                logging.warning(tags)
            else:
                pass
                # TODO error handler
        return HttpResponseRedirect('/')
    else:
        available_tags = HaskerTag.objects.all()
        context = {
            'tags': available_tags,
        }
        return render(request, 'asking.html', context)








