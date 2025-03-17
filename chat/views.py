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
    chat_room, created = Room.objects.get_or_create(
        owner=request.user, language=language
    )
    if created:
        save_message(chat_room, Actor.ASSISTANT, get_completion(language))

    messages = chat_room.messages.order_by("timestamp").all()

    context = {
        "language": language,
        "messages": messages,
    }

    return render(
        request,
        "chat/room.html",
        context,
    )
