import pygame
import os
import sys
from button import Button

pygame.init()

# Screen Details
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("The Game")

# Background
background = pygame.image.load(os.path.join('assets/BG_Main.png'))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/Retro Gaming.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        screen.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu(): 
    run = True
    while run:

        # Gets mouse position for hovering
        menu_mouse_pos = pygame.mouse.get_pos()

        # Button Design
        play_button = Button(image=pygame.image.load("assets/green_button.png"), pos=(640, 340), 
                            text_input="PLAY", font=get_font(40), base_color="White", hovering_color="#2d422c")
        
        quit_button = Button(image=pygame.image.load("assets/red_button.png"), pos=(640, 420), 
                            text_input="QUIT", font=get_font(35), base_color="White", hovering_color="#6e373a")
        
        
        # Blit background image
        screen.blit(background, (0, 0))

        # Updates button appearance
        for button in [play_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    play()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()


        # Update Screen
        pygame.display.update()

main_menu()  # Call the main_menu function to start the game loop

pygame.quit()
