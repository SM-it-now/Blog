from django import forms
from .models import Comment


# 댓글 작성 폼
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'content',
        )