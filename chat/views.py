from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Room, Actor, Language
from .chat import save_message, get_completion


@login_required
def index(request):
    languages = Language.choices
    return render(request, "chat/index.html", {"languages": languages})


@login_required
def room(request, language):
    if language not in Language:
        return redirect("index")

    context = {
        "language": language,
    }

    return render(
        request,
        "chat/room.html",
        context,
    )
