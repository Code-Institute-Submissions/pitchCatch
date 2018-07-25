from models import Pitch, Pitcher, Catcher
from wtforms_alchemy import ModelForm


"""
Pitcher Form
"""
class PitcherForm(ModelForm):
    class Meta:
        model = Pitcher


"""
Pitch Form
"""
class PitchForm(ModelForm):
    class Meta:
        model = Pitch
        include = ['pitcher_id']
        

"""
Catcher Form
"""
class CatcherForm(ModelForm):
    class Meta:
        model = Catcher
