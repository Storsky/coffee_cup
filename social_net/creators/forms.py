from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    'placeholder': 'Share something...',
                                    'class': 'input is-link',
                                }
                            ),
                            label='',                            
                            )
    yt_link = forms.URLField(required=True,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    'placeholder': 'Youtube link',
                                    'class': 'input is-link',
                                }
                            ),
                            label='',                            
                            )

    description = forms.CharField(required=True,
                            widget=forms.widgets.Textarea(
                                attrs={
                                    'placeholder': 'Why is it so cool?',
                                    'class': 'textarea is-link',
                                }
                            ),
                            label='',                            
                            )

    class Meta:
        model = Post
        exclude = ('owner', 'likes_counter', 'video_id',)