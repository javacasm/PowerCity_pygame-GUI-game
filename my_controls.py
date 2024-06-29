from pygame_gui.elements import UIStatusBar

v = 0.11

print(f'{__name__} v{v}')

class UIPowerBar(UIStatusBar):
    def __init__(self, rect, manager, percent_method,max_value):
        self.power_max_value = max_value
        super().__init__(rect,manager,percent_method = percent_method,object_id='#power_bar')
               

    def status_text(self):
        value = self.percent_method()
        str_text = f'Power: {int(value)}/{int(self.power_max_value)} W'
        return str_text


class UIHealthBar(UIStatusBar):
    def __init__(self, rect, manager, percent_method):
        super().__init__(rect,manager,percent_method = percent_method,object_id='#health_bar')
             

    def status_text(self):
        value = self.percent_method()
        str_text = f'Status: {int(value)}/{100} %'
        return str_text