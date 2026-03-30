import pygame
import numpy as np
import math as maths

def toScreenCoords(log_coords):
    if type(log_coords) == list:
        return [toScreenCoords(i) for i in log_coords]
    elif type(log_coords) == tuple:
        return (width*0.5 + log_coords[0], height*0.5 - log_coords[1])

def toGameCoords(screen_coords):
    if type(screen_coords) == list:
        return [toGameCoords(i) for i in screen_coords]
    elif type(screen_coords) == tuple:
        return (screen_coords[0] - width*0.5, height*0.5 - screen_coords[1])

def centreToHexCoords(centre):
    edges = []

    for vect in edge_vectors:
        edge = (centre[0] + vect[0], centre[1] + vect[1])
        edges.append(edge)
    
    return edges

def fill_hexagon(centre, colour):

    #if (x+y)%2==0:
      #  pass      
       #pygame.draw.polygon(screen, )
    pass
    
def draw_hexagons(centres):     

    for x in range(-10,11):
        for y in range(-10,11):
            if (x+y)%2 == 0:

                centre = (grid_scalar* x, grid_scalar*y*np.sqrt(3))
                owner = centres[(x,y)][1]
                if owner == 1:
                    colour = (50,50, 180)
                    width = 0
                elif owner==-1:
                    colour = (180,50,50)
                    width = 0
                else:
                    colour = (0,0,0)
                    width = 3
                #pygame.draw.circle(screen, (0,0,0), c:= toScreenCoords(centre), 5, 5) draw centres

                edges = centreToHexCoords(centre)
                pygame.draw.polygon(screen, colour, toScreenCoords(edges), width)        #Draw hexagon

# Window Setup Values
(width, height) = (1200,600)
background_colour = (255,255,255)
icon = pygame.image.load('happy_hex.png')
caption = "Hex Tac Toe Bot"

# Window Setup
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)
pygame.display.set_caption(caption)
pygame.display.set_icon(icon)

# Coordinate Setup
grid_scalar = 60

edge_vectors = []

for angle in range(30, 360, 60):
    angle_rad = np.deg2rad(angle)
    radius = grid_scalar * np.sqrt(3)*2/3 * 0.95
    vect = (radius * np.cos(angle_rad), radius * np.sin(angle_rad))

    edge_vectors.append(vect)

hexagons = {}

# Draw Hex Grid

#Key : centre, Value : [R-value, ownership]
centres= {(x, y): [0, 0]  for x in range(-10,11) for y in range(-10,11) if (x+y)%2==0}

#centres = [(grid_scalar * x, grid_scalar * y * np.sqrt(3)) for x in range(-10,11) for y in range(-10,11) if (x+y)%2==0]

player = 1

# Running Loop
running = True

last_mouse_clicked = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        mouse_clicked = event.type == pygame.MOUSEBUTTONDOWN

    draw_hexagons(centres)
    
    # Render Window
    pygame.display.flip()
    
    move = mouse_clicked and not last_mouse_clicked

    if move:
        mouse_coords = toGameCoords(pygame.mouse.get_pos())
        scaled_mouse_coords = (mouse_coords[0] / grid_scalar, mouse_coords[1] / (grid_scalar*maths.sqrt(3)))

        corners = [(maths.ceil(scaled_mouse_coords[0]), maths.ceil(scaled_mouse_coords[1])),
        (maths.ceil(scaled_mouse_coords[0]), maths.floor(scaled_mouse_coords[1])),
        (maths.floor(scaled_mouse_coords[0]), maths.ceil(scaled_mouse_coords[1])),
        (maths.floor(scaled_mouse_coords[0]), maths.floor(scaled_mouse_coords[1]))]

        min_dist = float('inf')
        closest_corner = None
        for corner in corners:
            if (corner[0] + corner[1]) % 2 == 0:
                corner_game = (grid_scalar * corner[0], grid_scalar * corner[1] * np.sqrt(3))
                dist = np.sqrt((mouse_coords[0] - corner_game[0])**2 + (mouse_coords[1] - corner_game[1])**2)

                if dist < min_dist:
                    closest_corner = corner
                    min_dist = dist

        r = centres[closest_corner][0]
        centres[closest_corner] = [r, player]

        player = -player

    last_mouse_clicked = mouse_clicked


    



    




