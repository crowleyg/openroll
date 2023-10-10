from random import randint
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


# Window Configuration
Window.size = (400, 600)

# Load the kv file
Builder.load_file('openroll.kv')

class OpenRollLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.active_dice = {
            'd4': 0, 'd6': 0, 'd8': 0, 'd10': 0,
            'd12': 0, 'd20': 0, 'd100': 0}
    
    def add_die(self, die):
        self.active_dice[die] += 1
        self.ids.dice_display.text = self.active_roll()

    def remove_die(self, die):
        if self.active_dice[die] > 0:
            self.active_dice[die] -= 1
            self.ids.dice_display.text = self.active_roll()

    def active_roll(self):
        display_output = 'Rolling: '
        for die, count in self.active_dice.items():
            if count > 0:
                if display_output != 'Rolling: ':
                    display_output += ' + '
                display_output += f'{count}{die}'
        return display_output

    def roll_dice(self):
        display_output = self.active_roll()
        total = 0
        for die, count in self.active_dice.items():
            if count > 0:
                display_output += f'\n{die}: ('
                for i in range(count):
                    roll_result = randint(1, int(die[1:]))
                    if i > 0:
                        display_output += ' + '
                    display_output += f'{roll_result}'
                    total += roll_result
                display_output += ')'
        self.ids.dice_display.text = display_output

        if total > 0:
            self.ids.result_display.text = str(total)

    
    def clear_dice(self):
        self.active_dice = {
            'd4': 0, 'd6': 0, 'd8': 0, 'd10': 0,
            'd12': 0, 'd20': 0, 'd100': 0}
        self.ids.dice_display.text = 'Rolling: '
        self.ids.result_display.text = ''

class OpenRollApp(App):
    def build(self):
        return OpenRollLayout()
    
if __name__ == '__main__':
    OpenRollApp().run()