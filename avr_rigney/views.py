from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import LightModule
from .forms import LightModuleForm, ACModuleForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework import viewsets
from .serializers import LightSerializer
from django.http import JsonResponse
from rest_framework.generics import ListAPIView

class LightView(viewsets.ModelViewSet):
  queryset = LightModule.objects.all()
  serializer_class = LightSerializer

# class LightView(ListAPIView):
#   queryset = LightModule.objects.all()
#   serializer_class = LightSerializer

def get_lights(request):
  lights = LightModule.objects.all().values('id','module_name','module_ip','number_of_relays','number_of_relays_used','setting_each_light')
  lights_list = list(lights)
  return JsonResponse(lights_list, safe=False)

@login_required(login_url='/login/')
def dashboard(request):
  light_modules = LightModule.objects.all()
  # ranges = LightModule.objects
  context = {
    'light_modules': light_modules,
  }
  return render(request, 'avr_rigney/dashboard.html', context)

@login_required(login_url='/login/')
def presetsPage(request):
  return render(request, 'avr_rigney/presets-page.html')

def userCheck(user):
  return user.username=='admin'

@login_required(login_url='/login/')
@user_passes_test(userCheck, login_url='/dashboard/', redirect_field_name=None)
def settingsPage(request):
  if request.method == 'POST':  # if data has already been inputted
    module_type = request.POST.get('type-selection')  # checks what module was added
    if module_type == 'light_module':
      form = LightModuleForm(request.POST)  # request post data from light module form
    else:
      form = ACModuleForm(request.POST)     # request post data from ac module form

    if form.is_valid():
      module_name = form.cleaned_data['module_name']
      module_ip = form.cleaned_data['module_ip']
      relays = form.cleaned_data['number_of_relays']
      relays_used = form.cleaned_data['number_of_relays_used']
      setting_for_each = form.cleaned_data['setting_each_light']
      new_light_module = LightModule(
        module_name=module_name,
        module_ip=module_ip,
        number_of_relays=relays,
        number_of_relays_used=relays_used,
        setting_each_light=setting_for_each
      )
      new_light_module.save()
      return HttpResponseRedirect(reverse('avr_rigney:settingsPage'))
  else:   # no data yet, this will load a blank light module form
    light_form = LightModuleForm()
    ac_form = ACModuleForm()
    context = {
      'light_form': light_form,
      'ac_form': ac_form
    } 

  return render(request, 'avr_rigney/settings-page.html', context)