from openai import OpenAI
from django.conf import settings
from .models import Message, Actor, Room

client = OpenAI(
    base_url=settings.OPENROUTER_BASE_URL, api_key=settings.OPENROUTER_API_KEY
)


def get_completion(language, history=None, model="google/gemma-2-9b-it:free"):
    history = history or [
        {"role": "user", "content": f"Hello, please teach me {language}!"}
    ]
    messages = [
        {
            "role": "system",
            "content": f"""
                You are a friendly language tutor who is fluent in {language}.
                You are trying to teach the user how to learn {language} by adjusting your responses to the users current level of proficiency in {language}.
                If the user makes a mistake in {language}, you will correct them, explain what they did wrong and encourage them to continue learning {language}.
                If the user answers in English, you should provide them with {language} translations of what they said in English before you respond.
                You will help the user learn {language} by speaking with them in {language}.
                Limit your responses to a maximum of 100 words.
                """,
        },
        *history,
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return response.choices[0].message.content


def save_message(room: Room, actor: Actor, content: str):
    Message.objects.create(owner=room.owner, room=room, actor=actor, content=content)

    if actor == Actor.USER:
        history = room.messages.order_by("timestamp").values("actor", "content")
        save_message(room, Actor.ASSISTANT, get_completion(room.language, history))
