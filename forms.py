from models import Pitch, Pitcher, Catcher
from wtforms_alchemy import ModelForm


"""
Pitcher form
"""
class PitcherForm(ModelForm):
    class Meta:
        model = Pitcher


"""
PitchForm
"""
class PitchForm(ModelForm):
    class Meta:
        model = Pitch


"""
CatcherForm
"""
class CatcherForm(ModelForm):
    class Meta:
        model = Catcher