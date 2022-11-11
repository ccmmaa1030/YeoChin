from django import forms
from .models import Friend, Friend_Comment

class DateInput(forms.DateInput):
    input_type = 'date'

class FriendForm(forms.ModelForm):

    class Meta:
        model = Friend
        fields = ['title', 'content','start_at', 'end_at', 'image','thumbnail']
        widgets = {
            'start_at':DateInput(),
            'end_at':DateInput(),
            
        }
        labels = {
            'title': '제목',
            'content': '내용',
            'start_at': '시작날짜',
            'end_at': '마감날짜',
        }

class Friend_CommentForm(forms.ModelForm):

    class Meta:
        model = Friend_Comment
        fields = ['content']

