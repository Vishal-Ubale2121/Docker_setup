from django import forms
from core.models import Mood

class MoodForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MoodForm, self).__init__(*args, **kwargs)
        self.fields['time'].required = False


    class Meta:
        model = Mood
        fields = "__all__"