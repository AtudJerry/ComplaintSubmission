from django.forms import ModelForm
from complainsubmissionapp.models import Student

class Studentform(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
