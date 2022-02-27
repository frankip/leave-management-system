import datetime
from django import forms
from .models import Leave

class LeaveForm(forms.ModelForm):
    description = forms.CharField(label="Reason", max_length="100", widget=forms.Textarea, required=False)
    start_date  = forms.DateField(label="Start Date", initial=datetime.date.today, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date  = forms.DateField(label="End Date", widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Leave
        fields = ('employee', 'type', 'description', 'status', 'start_date', 'end_date',)
