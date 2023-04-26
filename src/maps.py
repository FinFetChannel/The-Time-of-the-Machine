def read_map(image):

    color_map = {
        #### any color not in the dict -> floor block
        (  0,   0,   0): 1,  # black -> brick wall
        (127, 127, 127): 2,  # gray -> tiled wall
        (195, 195, 195): 3,  # light gray -> concrete
        (255, 201,  14): 4,  # gold -> office window
        (136,   0,  21): 5,  # dark red -> office no window
        (255, 127,  39): 6,  # orange -> office door inside
        (181, 230,  29): 7,  # light green -> office door
        (  0, 255,   0): 8,  # pure green -> open door
        (  0, 162, 232): 9, # blue -> open window
        (255, 174, 201): 10, # pink -> fence
    }

    entity_map = {
        (237,  28,  36): 0, # red -> robot
        (34, 177,  76): 1,  # green -> tree
        (255, 242,   0): 2 # yellow - > vase
    }

    # Convert the image to a 2D list of integers using the color map
    map_data = []
    entity_data = []
    height = image.get_height()
    for x in range(image.get_width()):
        map_data.append([])
        for y in range(height):
            pixel_color = image.get_at((x, y))
            block_type = color_map.get((pixel_color.r, pixel_color.g, pixel_color.b), 0)

            map_data[x].append(block_type)
            entity_type = entity_map.get((pixel_color.r, pixel_color.g, pixel_color.b), -1)
            if entity_type >= 0:
                entity_data.append([entity_type, x + 0.5, y+0.5, 0, 0, 0, 0, 5])# type, x, y, direction, distance, status, cooldown, health
                if entity_type in [1, 2]:
                    map_data[x][-1] = -1
    
    return map_data, entity_data