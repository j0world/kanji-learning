# Description: A program to help me learn kanji
import pygame
import sys
import json
import random


"""
future features:
- add a play button -- done
- add a jlpt level selector -- done
- get kanji from kanji.json -- done
- display the kanji -- done
- display the reading and meaning if button is pressed (space for that and arrow for next kanji?) -- done
- add a training selector -- done
- add a way to save progress -- done
- add an info button -- done
- add all kanji (N3)
- add randomized order for kanji -- done
- add all kanji (N2)
- add settings?
"""

# Variables
width, height = 700, 700





# Window set up
pygame.init()
screen = pygame.display.set_mode((width, height))
done   = False
FPS    = 60

# Colors
white     = (250, 250, 250)
black     = (0, 0, 0)
green     = (0, 250, 0)
red       = (220, 20, 60)
dif_black = (50, 50, 50) # also known as grey
dif_green = (0, 200, 0)


screen.fill(dif_black)
clock = pygame.time.Clock()

def main(done):

    # variables
    font_1 = pygame.font.Font(None, 64)
    font_2 = pygame.font.Font(None, 32)
    font_3 = pygame.font.Font(None, 16)
    jp_font_1 = pygame.font.Font("BIZUDGothic-Regular.ttf", 192)
    jp_font_2 = pygame.font.Font("BIZUDGothic-Regular.ttf", 32)
    title               = "kanji learning"
    play                = "play"
    jlpt                = "jlpt level"
    training            = "words to train"
    arrow_left          = "<"
    arrow_right         = ">"
    made_by             = "made by me"
    jlpt_level          = "N5"
    info_up             = "Press UP if you know the kanji"
    info_down           = "Press DOWN if you don't know the kanji"
    info_space          = "Press SPACE to see the reading and meaning"
    info_nav            = "Use the arrow keys to navigate"
    info_esc            = "Press ESC to go back to the menu"
    info_text_1         = "This is a program to help you learn kanji."
    info_text_2         = "You can select the jlpt level and the words you want to train."
    info_text_3         = "Press play to start."
    training_kind_array = ["strong", " all", "weak"]
    training_kind       = training_kind_array[1]
    featured_jlpt_levels   = 3 # count(5, 4, 3)
    arrow_counter          = 4
    training_arrow_counter = 1
    next_kanji             = 0
    space_pressed          = 0
    play_button      = False
    info_button      = False
    empty_kanji_data = False
    kanji_data = {}





    # Background
    pygame.display.set_caption(title)

    # Game loop
    while not done:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and play_button == False and info_button == False:

                # play button \/
                if width / 2 - 70 <= mouse[0] <= width / 2 - 70 + 140 and height / 3 + 42 <= mouse[1] <= height / 3 + 42 + 40:
                    kanji_data = json_stuff(jlpt_level)
                    kanji_data = training_stuff(training_kind, kanji_data)
                    if len(kanji_data) == 0:
                        empty_kanji_data = True
                        menu(font_1, font_2, font_3, title, play, jlpt, training, arrow_left, arrow_right, made_by, jlpt_level, training_kind, screen, width, height, white, green, empty_kanji_data, mouse)
                    else:
                        empty_kanji_data = False
                        play_button      = True

                # info button \/
                if width - 50 <= mouse[0] <= width - 50 + 40 and 10 <= mouse[1] <= 10 + 40:
                    info_button = True
                    play_button = False

                # jlpt level selector \/
                if width / 2 + 50 - 20 <= mouse[0] <= width / 2 + 50 + 40 and height / 2 + 42 - 20 <= mouse[1] <= height / 2 + 42 + 40:
                    arrow_counter -= 1
                    jlpt_level = "N" + str((arrow_counter)%(featured_jlpt_levels) + (6-featured_jlpt_levels))
                    print(jlpt_level)
                    #screen.fill(dif_black)

                # jlpt level selector \/
                if width / 2 - 74 - 20 <= mouse[0] <= width / 2 - 75 + 40 and height / 2 + 42 - 20 <= mouse[1] <= height / 2 + 42 + 40:
                    arrow_counter += 1
                    jlpt_level = "N" + str((arrow_counter)%(featured_jlpt_levels) + (6-featured_jlpt_levels))
                    print(jlpt_level)
                    #screen.fill(dif_black)

                # training selector \/
                if width / 2 + 50 - 20 <= mouse[0] <= width / 2 + 50 + 40 and height / 2 + 126 - 20 <= mouse[
                    1] <= height / 2 + 126 + 40:
                    training_arrow_counter -= 1
                    training_kind = str(training_kind_array[((training_arrow_counter)% len(training_kind_array))])
                    print(training_arrow_counter)
                    # screen.fill(dif_black)

                # training selector \/
                if width / 2 - 74 - 20 <= mouse[0] <= width / 2 - 75 + 40 and height / 2 + 126 - 20 <= mouse[
                    1] <= height / 2 + 126 + 40:
                    training_arrow_counter += 1
                    training_kind = str(training_kind_array[(training_arrow_counter)% len(training_kind_array)])
                    print(training_arrow_counter)
                    # screen.fill(dif_black)


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                   print("return")
                   #print(len(kanji_data))


                elif event.key == pygame.K_BACKSPACE:
                   print("backspace")
                elif event.key == pygame.K_LEFT:
                    #print("left")
                    if play_button and next_kanji > 0:
                        next_kanji -= 1
                        space_pressed = 0

                elif event.key == pygame.K_RIGHT:
                    #print("right")
                    if play_button and next_kanji < len(kanji_data) - 1:
                        next_kanji += 1
                        space_pressed = 0

                elif event.key == pygame.K_UP:
                    if play_button and next_kanji < len(kanji_data) - 1:
                        kanji_data[next_kanji]['correct'] = kanji_data[next_kanji]['correct'] + 1
                        kanji_data[next_kanji]['streak']  = kanji_data[next_kanji]['streak'] + 1
                        next_kanji += 1
                        space_pressed = 0

                elif event.key == pygame.K_DOWN:
                    if play_button and next_kanji < len(kanji_data) - 1:
                        kanji_data[next_kanji]['wrong']  = kanji_data[next_kanji]['wrong'] + 1
                        kanji_data[next_kanji]['streak'] = 0
                        next_kanji += 1
                        space_pressed = 0

                elif event.key == pygame.K_SPACE:
                    if play_button and space_pressed < 2:
                        space_pressed += 1

                elif event.key == pygame.K_ESCAPE:
                    print("escape")
                    play_button   = False
                    info_button   = False
                    next_kanji    = 0
                    space_pressed = 0
                    print     ("Old kanji data: " + str(kanji_data))
                    kanji_dump(kanji_data, jlpt_level)
                    print     ("New kanji data" + str(kanji_data))
                    # triggers the new kanji value dump



        # Draw things
        if play_button:
            # do something
            screen.fill(dif_black)
            #print(kanji_data)
            current_kanji = kanji_data[next_kanji]
            # if current_kanji is not the last one:
            screen.blit(jp_font_1.render(current_kanji['name'], True, white), (width / 2 - 90, height / 5))
            if space_pressed > 0:
                screen.blit(jp_font_2.render(current_kanji['kunyomi'], True, white), (width / 2 - 30, height / 2 - 20))
                screen.blit(jp_font_2.render(current_kanji['onyomi'], True, white), (width / 2 - 30, height / 2 + 15))
                if space_pressed > 1:
                    screen.blit(font_2.render(current_kanji['meaning'], True, white), (width / 2 - 30, height / 2 + 55))
            #knaji_screen(kanji_data)
        elif info_button:
            #print("info")
            info(font_1, font_2, font_3,info_up, info_down, info_space, info_nav, info_esc, info_text_1, info_text_2, info_text_3, screen, width, height, white)
        else:
            menu(font_1, font_2, font_3, title, play, jlpt, training, arrow_left, arrow_right, made_by, jlpt_level, training_kind, screen, width, height, white, green, empty_kanji_data, mouse)

        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)








def menu(font_1, font_2, font_3, title, play, jlpt, training, arrow_left, arrow_right, made_by, jlpt_level, training_kind, screen, width, height, white, green, empty_kanji_data, mouse):
    screen.fill((50, 50, 50))
    # Draw
    screen.blit(font_1.render(title,   True, white), (width / 2 - 140, height / 4))
    screen.blit(font_3.render(made_by, True, white), (width - 70,      height - 20))
    # jlpt selector
    screen.blit(font_2.render(jlpt,        True, white), (width / 2 - 45, height / 2))
    screen.blit(font_2.render(arrow_left,  True, white), (width / 2 - 74, height / 2 + 42))
    screen.blit(font_2.render(arrow_right, True, white), (width / 2 + 50, height / 2 + 42))
    screen.blit(font_2.render(jlpt_level,  True, white), (width / 2 - 20, height / 2 + 42))
    # training selector
    screen.blit(font_2.render(training,      True, white), (width / 2 - 74, height / 2 + 90))
    screen.blit(font_2.render(arrow_left,    True, white), (width / 2 - 74, height / 2 + 126))
    screen.blit(font_2.render(arrow_right,   True, white), (width / 2 + 50, height / 2 + 126))
    screen.blit(font_2.render(training_kind, True, white), (width / 2 - 40, height / 2 + 126))
    # info button
    screen.blit(font_2.render("info", True, white), (width - 50, 10))
    # empty set of kanji
    if empty_kanji_data:
        screen.blit(font_2.render("This set is empty, please select something else.", True, red), (width / 2 - 240, height / 8))
    # play button
    if width / 2 - 70 <= mouse[0] <= width / 2 - 70 + 140 and height / 3 + 42 <= mouse[1] <= height / 3 + 42 + 40:
        pygame.draw.rect(screen, dif_green, [width / 2 - 70, height / 3 + 42, 140, 40])
    else:
        pygame.draw.rect(screen, green, [width / 2 - 70, height / 3 + 42, 140, 40])
    screen.blit(font_2.render(play, True, white), (width / 2 - 25, height / 3 + 51))

def info(font_1, font_2, font_3,info_up, info_down, info_space, info_nav, info_esc, info_text_1, info_text_2, info_text_3, screen, width, height, white):
    screen.fill((50, 50, 50))

    screen.blit(font_2.render(info_text_1, True, white), (width / 2 - 200, height / 4))
    screen.blit(font_2.render(info_text_2, True, white), (width / 2 - 310, height / 4 + 30))
    screen.blit(font_2.render(info_text_3, True, white), (width / 2 - 100, height / 4 + 60))
    screen.blit(font_3.render(info_up,     True, white), (width / 2 - 100, height / 4 + 150))
    screen.blit(font_3.render(info_down,   True, white), (width / 2 - 100, height / 4 + 180))
    screen.blit(font_3.render(info_space,  True, white), (width / 2 - 100, height / 4 + 210))
    screen.blit(font_3.render(info_nav,    True, white), (width / 2 - 100, height / 4 + 240))
    screen.blit(font_3.render(info_esc,    True, white), (width / 2 - 100, height / 4 + 270))




def json_stuff(jlpt_level):
    with open('kanji.json', 'r') as json_file:
        data = json.load(json_file)
        match jlpt_level:
            case "N5":
                kanji_data = data['kanji'][0]['N5']
            case "N4":
                kanji_data = data['kanji'][1]['N4']
            case "N3":
                kanji_data = data['kanji'][2]['N3']
            case "N2":
                kanji_data = data['kanji'][3]['N2']
            case "N1":
                kanji_data = data['kanji'][4]['N1']

    return(kanji_data)

def get_kaji_json():
    with open('kanji.json', 'r') as json_file:
        data = json.load(json_file)
        return(data)

def training_stuff(training_type, kanji_data):
    temp_kanji_data = {}
    match training_type:
        case "strong": # crashes if empty
            # print(type(kanji_data[1]['streak']) is int)
            for i in range(len(kanji_data)):
                #print(kanji_data[i])
                if ((kanji_data[i]['streak'])>=3):
                    temp_kanji_data[len(temp_kanji_data)] = kanji_data[i]
            kanji_data = temp_kanji_data


        case "all": # not needed
            print("")
        case "weak":
            for i in range(len(kanji_data)):
                #print(kanji_data[i])
                if ((kanji_data[i]['streak'])<=3):
                    temp_kanji_data[len(temp_kanji_data)] = kanji_data[i]
            kanji_data = temp_kanji_data

    random.shuffle(kanji_data)

    return(kanji_data)

def kanji_dump(kanji_data, jlpt_level):
    temp_kanji_data = kanji_data
    kanji_data      = get_kaji_json()

    match jlpt_level:
        case "N5":
            #print(kanji_data['kanji'][0]['N5'])
            for i in range(len(kanji_data['kanji'][0]['N5'])):
                for x in range(len(temp_kanji_data)):
                    if kanji_data['kanji'][0]['N5'][i]['name'] == temp_kanji_data[x]['name']:
                        kanji_data['kanji'][0]['N5'][i] = temp_kanji_data[x]
        case "N4":
            #kanji_data['kanji'][1]['N4']
            for i in range (len(kanji_data['kanji'][1]['N4'])):
                for x in range(len(temp_kanji_data)):
                    if kanji_data['kanji'][1]['N4'][i]['name'] == temp_kanji_data[x]['name']:
                        kanji_data['kanji'][1]['N4'][i] = temp_kanji_data[x]
        case "N3":
            #kanji_data['kanji'][2]['N3']
            for i in range (len(kanji_data['kanji'][2]['N3'])):
                for x in range(len(temp_kanji_data)):
                    if kanji_data['kanji'][2]['N3'][i]['name'] == temp_kanji_data[x]['name']:
                        kanji_data['kanji'][2]['N3'][i] = temp_kanji_data[x]
        case "N2":
            #kanji_data['kanji'][3]['N2']
            for i in range (len(kanji_data['kanji'][3]['N2'])):
                for x in range(len(temp_kanji_data)):
                    if kanji_data['kanji'][3]['N2'][i]['name'] == temp_kanji_data[x]['name']:
                        kanji_data['kanji'][3]['N2'][i] = temp_kanji_data[x]
        case "N1":
            #kanji_data['kanji'][4]['N1']
            for i in range (len(kanji_data['kanji'][4]['N1'])):
                for x in range(len(temp_kanji_data)):
                    if kanji_data['kanji'][4]['N1'][i]['name'] == temp_kanji_data[x]['name']:
                        kanji_data['kanji'][4]['N1'][i] = temp_kanji_data[x]

    with open('kanji.json', 'w') as f:
        json.dump(kanji_data, f, indent=4)



def knaji_screen(kanji_data): # not needed for now
    print(kanji_data)

if __name__ == '__main__':
    main(done)