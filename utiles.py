# utiles

from pygame import transform, image

def escala_imagenes(array_iconos, new_size):
    array_iconos_escalados = []
    for icono in array_iconos:
        icono_resize = escala_imagen(icono, new_size)
        array_iconos_escalados.append(icono_resize)
    return array_iconos_escalados

def escala_imagen(imagen, new_size):
    imagen_escalada = transform.scale(imagen, (new_size, new_size))
    return imagen_escalada