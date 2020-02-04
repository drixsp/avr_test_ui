from django.db import models
from django.core.validators import validate_comma_separated_integer_list, MinValueValidator, MaxValueValidator


class LightModule(models.Model):
  module_name = models.CharField(max_length=50)
  module_ip = models.CharField(max_length=50)
  number_of_relays = models.PositiveIntegerField(validators=[MinValueValidator(2), MaxValueValidator(8)])
  number_of_relays_used = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(8)])  # LATER, MAX MUST BE SMALLER THAN NUMBER OF RELAYS
  setting_each_light = models.CharField(validators=[validate_comma_separated_integer_list], max_length=200)
    
  def __str__(self):
    return self.module_name

  def get_module_setting(self):
    settings = self.setting_each_light.split(',')
    return settings

  def number_of_relays_range(self):
    return range(self.number_of_relays)

  def number_of_relays_used_range(self):
    return range(self.number_of_relays_used)

# class OutletModule(models.Model):
  # number of outlets
  # setting for each outlet
  # module name
  # ip address of module's node

# class ACModule(models.Model):
  # number of ac units
  # mode of module (auto/manual)
  # setting for each unit
  # level setting of module
  # timer value - DurationField?
  # ip address of module's node

# class TempModule(models.Model):
  # number of temp sensors
  # module name
  # 4 ip addresses of each temp sensor's node
