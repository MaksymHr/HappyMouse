import sys
import pygame

from mouse import Mouse
from game_settings import settings, Scoreboard
from food import Food


def main():
    """
    Main game loop

    :return: None
    """

    # create display and set main references
    sc = pygame.display.set_mode((480, 640))
    pygame.display.set_caption('Щасливе мишеня')
    pygame.time.set_timer(pygame.USEREVENT, 3000)
    foods = pygame.sprite.Group()
    Food(sc, foods)
    mouse = Mouse(sc)
    move = 'STOP'
    sb = Scoreboard(sc)

    # loading bg image
    bg = pygame.image.load(r"images\background.jpg")

    # main loop
    while settings.game_active:

        # cycle for catch user press button, to spawn cheese or quit game
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_RIGHT:
                    move = 'RIGHT'
                elif i.key == pygame.K_LEFT:
                    move = 'LEFT'
            elif i.type == pygame.KEYUP:
                move = 'STOP'
            elif i.type == pygame.USEREVENT:
                if foods.__len__() < 15:
                    Food(sc, foods)

        # update bg and player on screen
        sc.blit(bg, (0, 0))
        sc.blit(mouse.image, mouse.rect)

        # update food on screen
        foods.update(sc)
        foods.draw(sc)

        # check if player catch cheese and increase their score
        if pygame.sprite.spritecollideany(mouse, foods):
            for food in foods.copy():
                if pygame.sprite.collide_rect(mouse, food):
                    food.catch()
            settings.score += 1
            sb.prep_score()

        # player move
        if move == 'LEFT':
            mouse.move_left()
        elif move == 'RIGHT':
            mouse.move_right()

        # display player's score, update screen and set FPS
        sb.show_score()
        settings.increase_diff()
        pygame.display.update()
        pygame.time.delay(40)

    # when game stopped
    else:
        # show "game over" and quit game after 5s
        text_color = (0, 0, 0)
        font = pygame.font.SysFont(None, 48)
        msg_image = font.render('Кінець гри', True, text_color)
        msg_rect = msg_image.get_rect()
        msg_rect.center = (240, 320)
        msg_rect.y = 50
        sc.blit(msg_image, msg_rect)
        pygame.display.update()
        pygame.time.delay(5000)


if __name__ == "__main__":
    main()
