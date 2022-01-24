from kivy import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

import plansza
from gamebutton import GameButton

class Statki(GridLayout):
    def __init__(self, **kwargs):
        super(Statki, self).__init__(**kwargs)
        self.ids['opponent'].disabled = True

        for c1 in self.children:
            for c2 in c1.children:
                for c3 in c2.children:
                    for c4 in c3.children:
                        if isinstance(c4, GameButton):
                            c4.sendMessage = self.sendMessage

    def startButtonClick(self):
        self.ids['player'].disabled = True
        self.ids['opponent'].disabled = False
        self.ids['rozpocznijGameButton'].disabled=True
        self.ids['graId'].disabled=True
        print("Click")

    def onMessage(self, message):
        x = message['x']
        y = message['y']
        if self.isShip(x, y):
            self.ids['opponent'].ids[y].ids[x].hit()
        else:
            self.ids['opponent'].ids[y].ids[x].miss()

    def sendMessage(self, message):
        print(message)
        self.onMessage(message)

    def isShip(self, x, y):
        return self.ids['player'].ids[y].ids[x].isShip

class StatkiApp(App):
    def build(self):
        return Statki()

if __name__ == '__main__':
    Config.read('config.ini')
    StatkiApp().run()
