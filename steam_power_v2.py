
import pygame

from pygame_gui import UIManager, UI_BUTTON_PRESSED, UI_HORIZONTAL_SLIDER_MOVED
from pygame_gui.elements import UILabel, UIScreenSpaceHealthBar
from power_plant_v2 import PowerPlant_v2
from pygame import Vector2, Rect
from config import *


v = 0.4

print(f'{__name__} v{v}')

pygame.init()

pygame.display.set_caption('Power plants')

window_surface = pygame.display.set_mode(SIZE)
manager = UIManager(SIZE, THEME_FILE)

background = pygame.Surface(SIZE)
background.fill(manager.ui_theme.get_colour('dark_bg'))


plantas = []
for data in plantas_data:
    planta = PowerPlant_v2(data[0], manager, data[1], Vector2(data[2],data[3]),data[4],data[5])
    plantas.append(planta)

def get_power_percentage():
    return 50

full_power_label = UILabel(Rect((100,80),(50, 25)),'Power',manager)

full_power_bar = UIScreenSpaceHealthBar(Rect((100, 100), (200, 30)),manager)
    
city_label = UILabel(Rect((20,20),(100, 25)),'Granada',manager)

progress = 0
time_acc = 0
clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        manager.process_events(event)

        if event.type == UI_BUTTON_PRESSED:
            bFound = False            
            for planta in plantas:
                if event.ui_element == planta.info_button :
                    bFound = True                    
                    planta.create_message_window()
                    break
                if event.ui_element == planta.more_control_button:
                    bFound = True
                    planta.create_more_control_window()
                    
            if bFound == False:
                print(f'button not found {event.ui_element}')
                
        elif event.type == UI_HORIZONTAL_SLIDER_MOVED:
            bFound = False
            for planta in plantas:
                if event.ui_element == planta.slider_bar:
                    planta.slider_label.text = str(int(planta.slider_bar.get_current_value()))
                    bFound = True
                    break
            if bFound == False:
                print('slider not found')                


    manager.update(time_delta)
    for planta in plantas:
        planta.update(time_delta)
        
    time_acc += time_delta

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
pygame.quit()