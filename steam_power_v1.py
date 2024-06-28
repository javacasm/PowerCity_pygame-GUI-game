import pygame
from pygame import Rect
import pygame_gui
from pygame_gui.core import ObjectID
from pygame_gui.elements import UILabel, UIImage, UIStatusBar, UIHorizontalSlider, UIButton

IMAGE_DIR = 'assets/graphics/'

class PowerPlant(pygame.sprite.Sprite):
    def __init__(self, *groups: pygame.sprite.AbstractGroup):
        super().__init__(*groups)

        self.max_health = 100
        self.current_health = 100

        self.max_mana = 100
        self.current_mana = 50

        self.max_stamina = 100.0
        self.current_stamina = 10.0

        self.speed = 100.0
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.stam_recharge_tick = 0.05
        self.stam_recharge_acc = 0.0


    def add_status_bars(self):
        margen = 10
        ancho_barra = self.image.get_rect().width + 2 * margen
        alto_barra = 10
        base_barras = 0
        espacio_barras = 20
        self.health_bar = UIStatusBar(Rect((0, base_barras), (ancho_barra, alto_barra)),
                          manager,
                          sprite=self,
                          follow_sprite = True,
                          percent_method=self.get_health_percentage,
                          object_id=ObjectID(
                                 '#health_bar', '@player_status_bars'))
        self.mana_bar = UIStatusBar(Rect((0, base_barras + (alto_barra + espacio_barras)), (ancho_barra, alto_barra)),
                          manager,
                          sprite=self,
                          follow_sprite = True,                                    
                          percent_method=self.get_mana_percentage,
                          object_id=ObjectID(
                                 '#mana_bar', '@player_status_bars'))
        self.stamina_bar = UIStatusBar(Rect((0, base_barras + 2 * (alto_barra + espacio_barras)), (ancho_barra, alto_barra)),
                          manager,
                          sprite=self,
                          follow_sprite = True,                                       
                          percent_method=self.get_stamina_percentage,
                          object_id=ObjectID(
                              '#stamina_bar', '@player_status_bars'))
                                            



    def set_control_power_bar(self,power_bar):
        self.power_bar = power_bar

    def set_image_file(self,image_file):        
        self.image = pygame.image.load(IMAGE_DIR+image_file)
        self.rect = self.image.get_rect()
#        self.rect.topleft = (200, 300)
        self.add_status_bars()


    def get_health_percentage(self) -> float:
        return self.current_health/self.max_health

    def get_mana_percentage(self) -> float:
        return self.current_mana/self.max_mana

    def get_stamina_percentage(self) -> float:
        return self.current_stamina/self.max_stamina

    def update(self, time_delta_secs: float) -> None:
        '''
        if self.moving_left:
            self.position.x -= self.speed * time_delta_secs
            self.current_stamina -= 0.4
        if self.moving_right:
            self.position.x += self.speed * time_delta_secs
            self.current_stamina -= 0.4
        if self.moving_up:
            self.position.y -= self.speed * time_delta_secs
            self.current_stamina -= 0.4
        if self.moving_down:
            self.position.y += self.speed * time_delta_secs
            self.current_stamina -= 0.4

        self.current_stamina = max(self.current_stamina, 0)

        if self.current_stamina < self.max_stamina:
            self.stam_recharge_acc += time_delta_secs
            if self.stam_recharge_acc >= self.stam_recharge_tick:
                self.current_stamina += 1
                self.stam_recharge_acc = 0.0

        self.current_stamina = min(self.current_stamina, self.max_stamina)
        '''
        self.rect.topleft = (int(self.position.x), int(self.position.y))


pygame.init()

ANCHO = 800
ALTO = 600

SIZE = (ANCHO, ALTO)

pygame.display.set_caption('Power plants')
window_surface = pygame.display.set_mode(SIZE)
manager = pygame_gui.UIManager(SIZE, 'pygame_gui_examples/data/themes/status_bar_theme.json')

background = pygame.Surface(SIZE)
background.fill(manager.ui_theme.get_colour('withe_bg'))

sprite_list = pygame.sprite.Group()

nuclear_plant = PowerPlant(sprite_list)
nuclear_plant.set_image_file('nuclear.png')
nuclear_plant.position = pygame.Vector2(100.0, 300.0)

grid_plant = PowerPlant(sprite_list)
grid_plant.set_image_file('grid.png')
grid_plant.position = pygame.Vector2(600.0, 200.0)

coal_plant = PowerPlant(sprite_list)
coal_plant.set_image_file('coal.png')
coal_plant.position = pygame.Vector2(350.0, 400.0)

progress_bar = UIStatusBar(Rect((100, 100), (200, 30)),
                                               manager,
                                               None,
                                               object_id=ObjectID('#progress_bar', '@UIStatusBar'))

power_bar = UIHorizontalSlider(Rect((50,60),(200, 25)),
                                      50.0,
                                      (0.0, 100.0),
                                      manager,
                                      None,
                                      click_increment=5)

power_bar_label = UILabel(Rect((50,80),(200,25)), str(int(power_bar.get_current_value())),manager)

city_label = UILabel(Rect((20,20),(100, 25)),'Granada',manager)



'''
test_image = UIImage(Rect((int(self.rect.width / 9),
                                               int(self.rect.height * 0.3)),
                                              loaded_test_image.get_rect().size),
                                  loaded_test_image, self.ui_manager,
                                  container=self)
'''
test_button = UIButton(pygame.Rect((50,150),(120, 40)),
                                    'Hola',
                                    manager,
                                    tool_tip_text="<font face=noto_sans color=normal_text size=2>"
                                                  "<b><u>Test Tool Tip</u></b>"
                                                  "<br><br>"
                                                  "A little <i>test</i> of the "
                                                  "<font color=#FFFFFF><b>tool tip</b></font>"
                                                  " functionality."
                                                  "<br><br>"
                                                  "Unleash the Kraken!"
                                                  "</font>",
                                    object_id='#hover_me_button')

nuclear_plant.set_control_power_bar(power_bar)


progress = 0
time_acc = 0
clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                nuclear_plant.moving_left = True
            if event.key == pygame.K_RIGHT:
                nuclear_plant.moving_right = True
            if event.key == pygame.K_UP:
                nuclear_plant.moving_up = True
            if event.key == pygame.K_DOWN:
                nuclear_plant.moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                nuclear_plant.moving_left = False
            if event.key == pygame.K_RIGHT:
                nuclear_plant.moving_right = False
            if event.key == pygame.K_UP:
                nuclear_plant.moving_up = False
            if event.key == pygame.K_DOWN:
                nuclear_plant.moving_down = False

        manager.process_events(event)

    sprite_list.update(time_delta)
    manager.update(time_delta)

    time_acc += time_delta
    progress = (time_acc/10.0)
    if progress > 1.0:
        time_acc = 0.0
    progress_bar.percent_full = progress

    window_surface.blit(background, (0, 0))
    sprite_list.draw(window_surface)
    manager.draw_ui(window_surface)

    pygame.display.update()
pygame.quit()
