
from django.forms import ModelForm
from .models import Event, Category, Participant

class EventForm(ModelForm):
    class Meta: model = Event; fields='__all__'

class CategoryForm(ModelForm):
    class Meta: model = Category; fields='__all__'

class ParticipantForm(ModelForm):
    class Meta: model = Participant; fields='__all__'
