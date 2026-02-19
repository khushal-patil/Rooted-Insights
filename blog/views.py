from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()

    return render(request, 'create_article.html', {'form': form})


def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            # 🔥 Check if user exists or not
            from django.contrib.auth.models import User

            if not User.objects.filter(username=username).exists():
                messages.error(request, "Account does not exist. Please register first.")
            else:
                messages.error(request, "Invalid password. Try again.")

    return render(request, "login.html")

def logout_view(request):
    # Implement logout logic here
    return redirect('login')
