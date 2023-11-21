import pygame
import sys
import os

pygame.init()

dir_actual = os.path.dirname(__file__)

ancho, alto = pygame.display.Info().current_w, pygame.display.Info().current_h

# Crear Ventana
ventana = pygame.display.set_mode((ancho, alto))  
pygame.display.set_caption("Batalla Naval Aerea") 

# Cargar la imagen de fondo de la pantalla de inicio
ruta_imagen_fondo_inicio = os.path.join(dir_actual, "Imagenes", "fondo_inicio.jpg")
imagen_fondo_inicio = pygame.image.load(ruta_imagen_fondo_inicio).convert()
imagen_fondo_inicio = pygame.transform.scale(imagen_fondo_inicio, (ancho, alto))

# Cargar la imagen de fondo de la pantalla del juego
ruta_imagen_fondo_juego = os.path.join(dir_actual, "Imagenes", "fondo_juego.jpg")
imagen_fondo_juego = pygame.image.load(ruta_imagen_fondo_juego).convert()
imagen_fondo_juego = pygame.transform.scale(imagen_fondo_juego, (ancho, alto))

# Configurar la fuente para el título y los botones
fuente_titulo = os.path.join(dir_actual, "square_pixel7", "square_pixel-7.ttf")
fuente_subtext = os.path.join(dir_actual, "square_pixel7", "square_pixel-7.ttf")
fuente_atras = pygame.font.Font(fuente_titulo, 40)  # Nueva fuente para el botón "atrás"
fuente_titulo = pygame.font.Font(fuente_titulo, 125)
fuente_subtext = pygame.font.Font(fuente_subtext, 50)

# Crear textos para el menú
titulo_texto = fuente_titulo.render("BATALLA NAVAL AEREA", True, (255, 255, 255))
empezar_texto = fuente_subtext.render("Empezar a Jugar", True, (255, 255, 255))
salir_texto = fuente_subtext.render("Salir", True, (255, 255, 255))

# Crear texto para el botón "atrás"
atras_texto = fuente_atras.render("Volver", True, (255, 255, 255))

# Obtener los rectángulos de los textos para posicionarlos en la pantalla
rect_titulo = titulo_texto.get_rect(center=(ancho // 2, alto // 4))
rect_empezar = empezar_texto.get_rect(center=(ancho // 2, alto // 2))
rect_salir = salir_texto.get_rect(center=(ancho // 2, alto * 3 // 4))

# Nuevo rectángulo para el botón "atrás"
rect_atras = atras_texto.get_rect(topleft=(20, 20))

# Función para dibujar el texto con contorno grueso
def draw_text_with_outline(surface, font, text, pos, color, outline_color, thickness):
    for i in range(1, thickness + 1):
        offset = i
        surface.blit(font.render(text, True, outline_color), (pos[0] - offset, pos[1]))
        surface.blit(font.render(text, True, outline_color), (pos[0] + offset, pos[1]))
        surface.blit(font.render(text, True, outline_color), (pos[0], pos[1] - offset))
        surface.blit(font.render(text, True, outline_color), (pos[0], pos[1] + offset))
    surface.blit(font.render(text, True, color), pos)

# Bucle principal del juego
en_juego = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not en_juego and rect_empezar.collidepoint(event.pos):
                en_juego = True
            elif rect_salir.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            elif en_juego and rect_atras.collidepoint(event.pos):
                en_juego = False

    if en_juego:
        # Lógica del juego
        ventana.blit(imagen_fondo_juego, (0, 0))
        
        # Dibuja el botón "atrás"
        pygame.draw.rect(ventana, (0, 0, 0), rect_atras.inflate(20, 10), border_radius=10, width=0)  # Borde negro
        pygame.draw.rect(ventana, (75, 83, 32), rect_atras.inflate(20 - 3*2, 10 - 3*2), border_radius=10, width=0)  # Rojo pastel
        ventana.blit(atras_texto, rect_atras)

        # Agrega aquí la lógica para los mapas y otros elementos del juego
        # ...
        

    else:
        # Pantalla de inicio
        ventana.blit(imagen_fondo_inicio, (0, 0))

        # Dibujar rectángulos alrededor de los textos con un borde negro
        borde_negro = 3  # Grosor del borde negro

        # Rectángulo con borde negro para "Empezar a Jugar"
        pygame.draw.rect(ventana, (0, 0, 0), rect_empezar.inflate(20, 10), border_radius=10, width=0)  # Borde negro
        pygame.draw.rect(ventana, (75, 83, 32), rect_empezar.inflate(20 - borde_negro*2, 10 - borde_negro*2), border_radius=10, width=0)  # Rojo pastel

        # Rectángulo con borde negro para "Salir"
        pygame.draw.rect(ventana, (0, 0, 0), rect_salir.inflate(20, 10), border_radius=10, width=0)  # Borde negro
        pygame.draw.rect(ventana, (75, 83, 32), rect_salir.inflate(20 - borde_negro*2, 10 - borde_negro*2), border_radius=10, width=0)  # Rojo pastel

        # Dibujar el texto con contorno
        draw_text_with_outline(ventana, fuente_titulo, "BATALLA NAVAL AEREA", rect_titulo.topleft, (255, 255, 255), (0, 0, 0), 5)

        ventana.blit(empezar_texto, rect_empezar)
        ventana.blit(salir_texto, rect_salir)

    # Actualizar la pantalla
    pygame.display.flip()

    # Agregamos un pequeño delay para reducir el uso de la CPU
    pygame.time.delay(10)
