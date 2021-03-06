from django import forms
from .models import Topic
from django import forms
from .models import Post


class NewTopicForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Tittle in here bro!'}
    ))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Write some stuff here!!!...'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Write your reply here!!!...'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )
    class Meta:
        model = Post
        fields = ['message', ]
