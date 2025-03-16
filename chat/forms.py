from django import forms


class MessageForm(forms.Form):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "placeholder": "Your message...",
                "class": "w-full p-4 bg-white border-2 rounded-xl",
            }
        ),
    )
