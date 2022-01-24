from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout

import gamebutton

class PlanszaRzad(GridLayout):
    number = NumericProperty()

    def __init__(self, **kwargs):
        super(PlanszaRzad, self).__init__(**kwargs)