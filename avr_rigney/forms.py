from django import forms
from django.core.validators import validate_comma_separated_integer_list, MinValueValidator, MaxValueValidator

class LightModuleForm(forms.Form):
  module_name = forms.CharField(max_length=50)
  module_ip = forms.CharField(max_length=50)
  relays_allowed = (
    (2, "2"),
    (4, "4"),
    (8, "8")
  )
  number_of_relays = forms.ChoiceField(choices=relays_allowed, widget=forms.RadioSelect())
  number_of_relays_used = forms.IntegerField(validators=[
    MinValueValidator(1),
    MaxValueValidator(8)
  ])  # LATER, MAX MUST BE SMALLER THAN NUMBER OF RELAYS
  setting_each_light = forms.CharField(validators=
    [validate_comma_separated_integer_list],
    max_length=200
  )

class ACModuleForm(forms.Form):
  module_name = forms.CharField(max_length=50)
  module_ip = forms.CharField(max_length=50)
  relays_allowed = (
    (2, "2"),
    (4, "4")
  )
  number_of_relays = forms.ChoiceField(choices=relays_allowed, widget=forms.RadioSelect())
  number_of_relays_used = forms.IntegerField(validators=[
    MinValueValidator(1),
    MaxValueValidator(8)
  ])  # LATER, MAX MUST BE SMALLER THAN NUMBER OF RELAYS
  setting_each_light = forms.CharField(validators=
    [validate_comma_separated_integer_list],
    max_length=200
  )