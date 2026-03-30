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

    if (x+y)%2==0:
                
       #pygame.draw.polygon(screen, )
    pass
    
def draw_hexagons(centres):     

    for x in range(-10,11):
        for y in range(-10,11):
            if (x+y)%2 == 0:

                centre = centres[(x,y)]
                #pygame.draw.circle(screen, (0,0,0), c:= toScreenCoords(centre), 5, 5) draw centres

                edges = centreToHexCoords(centre)
                pygame.draw.polygon(screen, (0,0,0), toScreenCoords(edges), 3)        #Draw hexagon

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
centres_dictionary = {(x, y): 0  for x in range(-10,11) for y in range(-10,11) if (x+y)%2==0}

centres = [(grid_scalar * x, grid_scalar * y * np.sqrt(3)) for x in range(-10,11) for y in range(-10,11) if (x+y)%2==0]


# Running Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_hexagons(centres)
    
    # Render Window
    pygame.display.flip()
        
    mouse_coords = toGameCoords(pygame.mouse.get_pos())
    scaled_mouse_coords = (mouse_coords[0] / grid_scalar, mouse_coords[1] / (grid_scalar*maths.sqrt(3)))

    corners = [(maths.ceil(scaled_mouse_coords[0]), maths.ceil(scaled_mouse_coords[1])),
    (maths.ceil(scaled_mouse_coords[0]), maths.floor(scaled_mouse_coords[1])),
    (maths.floor(scaled_mouse_coords[0]), maths.ceil(scaled_mouse_coords[1])),
    (maths.floor(scaled_mouse_coords[0]), maths.floor(scaled_mouse_coords[1]))]

<<<<<<< HEAD
    min_dist = 100
    closest_corner = 0
    for corner in corners:
        if (corner[0] + corner[1]) % 2 == 0:
            dist = maths.sqrt((scaled_mouse_coords[0] - corner[0])**2 + (scaled_mouse_coords[1] - corner[1])**2)
=======

    min_dist = float('inf')
    closest_corner = None
    for corner in corners:
        if (corner[0] + corner[1]) % 2 == 0:
            corner_game = (grid_scalar * corner[0], grid_scalar * corner[1] * np.sqrt(3))
            dist = np.sqrt((mouse_coords[0] - corner_game[0])**2 + (mouse_coords[1] - corner_game[1])**2)
>>>>>>> 85975276a77ce5f0b69205468c7320238abde18a

            if dist < min_dist:
                closest_corner = corner
                min_dist = dist

    print(closest_corner)



    




