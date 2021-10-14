from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxLengthValidator
from django.db.models.constraints import UniqueConstraint

from core.models import Board, Caste, Person, Standard
from core.validators import validate_aadhaar

class SignUpForm(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name=forms.CharField()
    aadhaar_no=forms.CharField(validators=[validate_aadhaar])
    email=forms.EmailField()
    caste=forms.ModelChoiceField(queryset=Caste.objects.all(),initial=0)
    board=forms.ModelChoiceField(queryset=Board.objects.all(),initial=0)
    previous_std=forms.ModelChoiceField(queryset=Standard.objects.all(),initial=0)
    percentage=forms.DecimalField()
    

    class Meta(UserCreationForm.Meta):
        model = Person
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email','aadhaar_no','caste','board','previous_std','percentage',)

