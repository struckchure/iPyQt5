'''
    Contains base widgets for other existing widgets,
    in terms of generic properties
'''

from iConfigurations import iConfig
from iConfigurations import iButtonConfig


'''
    Button Base
'''

class ButtonBase:
    padding = iConfig.generics['padding']
    margin = iConfig.generics['margin']
    border = iConfig.generics['border']
    borderRadius = iConfig.generics['borderRadius']
    color = iConfig.generics['color']
    backgroundColor = iConfig.generics['backgroundColor']
    width = iButtonConfig.generics['width']
    height = iButtonConfig.generics['height']
