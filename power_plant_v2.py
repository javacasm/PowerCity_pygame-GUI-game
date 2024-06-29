# power_plant

from pygame import Rect, Vector2, image

from pygame_gui.core import ObjectID
from pygame_gui.elements import UILabel, UIImage, UIStatusBar, UIHorizontalSlider, UIButton, UIScreenSpaceHealthBar
from pygame_gui.windows import UIMessageWindow 
from config import *
from random import randint
from utiles import *
from my_controls import UIPowerBar, UIHealthBar

v = 0.5

print(f'{__name__} v{v}')

class PowerPlant_v2:
    def __init__(self, name, manager,image_file, position, max_power,tool_tip):
        self.ui_manager = manager
        self.name = name
        self.position = position
        imagen_original = image.load(IMAGE_DIR+image_file)
        self.image = escala_imagen(imagen_original,SIZE_IMAGEN)
        self.tooltip = tool_tip
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

        self.health_capacity = 100
        self.current_health = 100

        self.max_power = max_power
        self.current_power = 0
        
        self.add_controls()

    def get_power(self):
        return randint(0,self.max_power)

    def get_health(self):
        return randint(0,100)

    def add_controls(self):

        '''
        TODO:
        A partir de la posición del elemento, añadimos:
            label con el nombre
            statusBar arriba con el % de  estado y label con valor 
            imagen de la planta
            V2 botón info para mostrar más detalles
            statusBar abajo la  producción y label con el valor
            slideBar abajo la potencia máxima y label con el valor
        Al hacer click
        '''
        
        margen = 10
        ancho_barra = self.image.get_rect().width 
        alto_barra = 25
        base_barras = 0
        espacio_barras = 20
        self.power_plant_label = UILabel(Rect(self.position,(150,25)), self.name, self.ui_manager)
        
        x_button = self.position.x+ancho_barra-25
        self.info_button = UIButton(Rect((x_button,self.position.y),(25,25)),
                                    '?',
                                    self.ui_manager,
                                    tool_tip_text=self.tooltip,
                                    object_id='#hover_me_button')

        self.more_control_button = UIButton(Rect((x_button-25,self.position.y),(25,25)),
                                    '+',
                                    self.ui_manager,
                                    tool_tip_text=self.tooltip,
                                    object_id='#hover_me_button')

        
        health_bar_y = self.position.y + 25
                
        self.health_bar = UIHealthBar(Rect((self.position.x,self.position.y+espacio_barras), (ancho_barra, alto_barra)),
                                                 self.ui_manager,self.get_health)
        image_y = health_bar_y + alto_barra
        self.imageUI = UIImage(Rect((self.position.x,image_y), (self.image.width,self.image.height)),
                                  self.image, self.ui_manager)
        
        power_bar_y = image_y + self.image.get_height()

        #self.power_bar = UIScreenSpaceHealthBar(Rect((self.position.x, power_bar_y), (ancho_barra, alto_barra)),
        #                                         self.ui_manager,
        #                                         sprite_to_monitor = self)
        self.power_bar = UIPowerBar(Rect((self.position.x, power_bar_y), (ancho_barra, alto_barra)),
                                                 self.ui_manager,
                                                 self.get_power,self.max_power)
        
        slider_bar_y = power_bar_y + alto_barra
        
        self.slider_bar = UIHorizontalSlider(Rect((self.position.x,slider_bar_y),(ancho_barra, 25)),
                              50.0, (0.0, 100.0),
                              self.ui_manager,
                              None,
                              click_increment=5)
        self.slider_label = UILabel(Rect((self.position.x + ancho_barra ,slider_bar_y),(100, 25)),
                                    str(int(self.slider_bar.get_current_value())),
                                    self.ui_manager)
        


    def update(self, time_delta_secs: float) -> None:
        # print('Update')
        self.rect.topleft = (int(self.position.x), int(self.position.y))
        self.current_health = randint(0,self.health_capacity)
        self.current_power = randint(0,self.max_power)
        
    def create_more_control_window(self):
        print('TODO: more controls window')

    def create_message_window(self):
        self.message_window = UIMessageWindow(
            rect=Rect(self.position,
                             (300, 250)),
            window_title='Test Message Window',
            html_message='<font color=normal_text>'
                         'This is a <a href="test">test</a> message to see if '
                         'this box <a href=actually_link>actually</a> works. '
                         '<br>'
                         'In <i>bibendum</i> orci et velit</b> gravida lacinia.<br><br>'
                         'In hac a habitasse to platea dictumst.<br>'
                         '<font color=#4CD656 size=4>Vivamus I interdum mollis lacus nec '
                         'porttitor. <br>Morbi '
                         'accumsan, lectus at '
                         'tincidunt to dictum, neque <font color=#879AF6>erat tristique '
                         'blob</font>, '
                         'sed a tempus for <b>nunc</b> dolor in nibh.<br>'
                         'Suspendisse in viverra dui <i>fringilla dolor laoreet</i>, sit amet '
                         'on pharetra a ante'
                         ' sollicitudin.</font>'
                         '<br><br>'
                         'In <i>bibendum</i> orci et velit</b> gravida lacinia.<br><br><br> '
                         'In hac a habitasse to platea dictumst.<br>'
                         ' <font color=#4CD656 size=4>Vivamus I interdum mollis lacus nec '
                         'porttitor.<br> Morbi'
                         ' accumsan, lectus at'
                         ' tincidunt to dictum, neque <font color=#879AF6>erat tristique '
                         'erat</font>,'
                         ' sed a tempus for <b>nunc</b> dolor in nibh.<br>'
                         ' Suspendisse in viverra dui <i>fringilla dolor laoreet</i>, sit amet '
                         'on pharetra a ante'
                         ' sollicitudin.</font>'
                         '<br><br>'
                         'In <i>bibendum</i> orci et velit</b> gravida lacinia.<br><br><br> '
                         'In hac a habitasse to platea dictumst.<br>'
                         ' <font color=#4CD656 size=4>Vivamus I interdum mollis lacus nec '
                         'porttitor.<br> Morbi'
                         ' accumsan, lectus at'
                         ' tincidunt to dictum, neque <font color=#879AF6>erat tristique '
                         'erat</font>,'
                         ' sed a tempus for <b>nunc</b> dolor in nibh.<br>'
                         ' Suspendisse in viverra dui <i>fringilla dolor laoreet</i>, '
                         'sit amet on pharetra a ante'
                         ' sollicitudin.</font>'
                         '</font>',
            manager=self.ui_manager)
