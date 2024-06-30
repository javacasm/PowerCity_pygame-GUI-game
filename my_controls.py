from pygame_gui.elements import UIStatusBar,UIWindow, UIHorizontalSlider, UILabel, UITextEntryLine, UIDropDownMenu, UIImage,UIScreenSpaceHealthBar

from pygame import Rect, image

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
    
class UIDetailWindow(UIWindow):
    def __init__(self, rect, ui_manager):
        super().__init__(rect, ui_manager,
                         window_display_title='Everything Container',
                         object_id='#everything_window',
                         resizable=True)

        self.test_slider = UIHorizontalSlider(Rect((int(self.rect.width / 2),
                                                           int(self.rect.height * 0.70)),
                                                          (240, 25)),
                                              50.0,
                                              (0.0, 100.0),
                                              self.ui_manager,
                                              container=self,
                                              click_increment=5)

        self.slider_label = UILabel(Rect((int(self.rect.width / 2) + 250,
                                                 int(self.rect.height * 0.70)),
                                                (28, 25)),
                                    str(int(self.test_slider.get_current_value())),
                                    self.ui_manager,
                                    container=self)
        
        self.test_text_entry = UITextEntryLine(Rect((int(self.rect.width / 2),
                                                            int(self.rect.height * 0.50)),
                                                           (200, -1)),
                                               self.ui_manager,
                                               container=self)
        self.test_text_entry.set_forbidden_characters('numbers')
        
        lista_items = [ f'Item {i}' for i in range(31)]
        current_resolution_string = lista_items[0]        
        self.test_drop_down_menu = UIDropDownMenu(lista_items,
                                                  current_resolution_string,
                                                  Rect((int(self.rect.width / 2),
                                                               int(self.rect.height * 0.3)),
                                                              (200, 25)),
                                                  self.ui_manager,
                                                  container=self)
        
        self.health_bar = UIScreenSpaceHealthBar(Rect((int(self.rect.width / 9),
                                                              int(self.rect.height * 0.7)),
                                                             (200, 30)),
                                                 self.ui_manager,
                                                 container=self)

        
        loaded_test_image = image.load('pygame_gui_examples/data/images/splat.bmp').convert_alpha()

        self.test_image = UIImage(Rect((int(self.rect.width / 9),
                                               int(self.rect.height * 0.3)),
                                              loaded_test_image.get_rect().size),
                                  loaded_test_image, self.ui_manager,
                                  container=self)
        
    def update(self, time_delta):
        super().update(time_delta)

        if self.alive() and self.test_slider.has_moved_recently:
            self.slider_label.set_text(str(int(self.test_slider.get_current_value())))
