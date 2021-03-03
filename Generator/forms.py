from django import forms

class questionFormResponse(forms.Form):
    question_text = forms.CharField(label='Questiontext', max_length=200)
    answer = forms.CharField(label='Answer', max_length=1)
    marks = forms.IntegerField(label='Marks')
    difficulty_level = forms.CharField(label='Difficultylevel',max_length=1)