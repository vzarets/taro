from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Question, Card, Interpretation
import random

def index(request):
    return render(request, 'taro/index.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'taro/signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.user.is_authenticated:
        return redirect('page5')

    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                error = "Неверный логин или пароль"
    else:
        form = LoginForm()

    return render(request, 'taro/login.html', {'form': form, 'error': error})


def user_logout(request):
    logout(request)
    return redirect('login')


def page5_view(request):
    question_id = request.GET.get('question_id')
    question = get_object_or_404(Question, id=question_id)

    cards = Card.objects.filter(interpretations__question=question).distinct()

    if cards.exists():
        card = random.choice(cards)
        interpretation = Interpretation.objects.filter(card=card, question=question).first()
    else:
        card = None
        interpretation = None

    interpretation_text = interpretation.description if interpretation else "Интерпретация отсутствует"
    card_image_url = card.image.url if card else ""

    return render(request, 'taro/page5.html', {
        'question': question.text,
        'card': card,
        'interpretation': interpretation_text
    })


def faq_view(request):
    return render(request, 'taro/faq.html')

@login_required(login_url='/login/')
def raskl_view(request):
    return render(request, 'taro/raskl.html')
