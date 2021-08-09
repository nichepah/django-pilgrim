from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'dump your thoughts here!'}
            ), 
        max_length=4000,
        help_text="max_length is 4k"
        )
    email = forms.EmailField()


    class Meta:
        model = Topic
        fields = ['subject', 'message', 'email']