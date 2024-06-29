#config

v = 0.4

print(f'{__name__} v{v}')

ANCHO_VENTANA = 1200
ALTO_VENTANA = 800

SIZE = (ANCHO_VENTANA, ALTO_VENTANA)

SIZE_IMAGEN = 200

THEME_FILE = 'power_city_theme.json'

IMAGE_DIR = 'assets/graphics/'

plantas_data = [ ['Nuclear','nuclear.png',100.0, 200.0,100,"<font face=noto_sans color=normal_text size=2>"
                                                  "<b><u>Test Tool Tip</u></b>"
                                                  "<br><br>"
                                                  "A little <i>test</i> of the "
                                                  "<font color=#FFFFFF><b>tool tip</b></font>"
                                                  " functionality."
                                                  "<br><br>"
                                                  "Unleash the Kraken!"
                                                  "</font>"],
            ['Red eléctrica','grid.png',750.0, 100.0,1500,'Tooltip <b>Red eléctrica</b>'],
            ['Carbón','coal.png',550.0, 500.0,50,'Tooltip Carbón'],
            ['Transformador','transformer.png',900,400,1500,'Tooltip Transformador']     ]
