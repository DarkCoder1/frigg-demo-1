from django import forms

class FriggForm(forms.Form):
    question = forms.CharField(
        label='digite uma pergunta',
        max_length=55
    )

class UploadForm(forms.Form):
    file = forms.FileField(
        label="Escolha um arquivo",
        help_text="Max. 10kb"
    )

class FeedbackForm(forms.Form):
    opinion_text = forms.CharField(
        label='Conte-nos o que achou:',
        widget=forms.Textarea
    )
    feedback_text = forms.CharField(
        label='O que poderia ser melhor?',
        widget=forms.Textarea
    )
    CHOICES=[(1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5')]

    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())