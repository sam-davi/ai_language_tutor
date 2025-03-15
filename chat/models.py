from django.db import models


class Actor(models.TextChoices):
    STUDENT = "Student"
    TUTOR = "Tutor"


class Language(models.TextChoices):
    ENGLISH = "English"
    FRENCH = "French"
    GERMAN = "German"
    SPANISH = "Spanish"


class Room(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    language = models.CharField(max_length=50, choices=Language.choices)

    class Meta:
        unique_together = ["owner", "language"]


class Message(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    actor = models.CharField(max_length=10, choices=Actor.choices)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
