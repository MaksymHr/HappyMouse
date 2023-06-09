import pygame.font


class Game_Settings:
    """
    Game mode and difficulty settings
    """

    food_speed = 2
    score = 0
    game_active = True

    def increase_diff(self):
        """
        Increase difficult. +2 to fall speed every 10 points in player's score
        :return:
        """
        if self.score % 10 == 0:
            self.food_speed = self.score / 5 + 2


class Scoreboard:
    """
    Showing player's score
    """

    def __init__(self, sc):
        """
        Set text mode for displayed score

        :param sc:
        """
        pygame.init()
        self.screen = sc
        self.rect = self.screen.get_rect()
        self.settings = settings

        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('Colibri', 48)
        self.score_image = ''
        self.score_rect = ''
        self.prep_score()

    def prep_score(self):
        """
        Create score entity and adding it to screen

        :return: None
        """

        score_str = str(self.settings.score)
        self.score_image = self.font.render(score_str, True, self.text_color, (224, 181, 147))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.rect.right - 30

        self.score_rect.top = 20

    def show_score(self):
        """
        Display score

        :return: None
        """
        self.screen.blit(self.score_image, self.score_rect)


# Create settings variable to import on other moduls
settings = Game_Settings()
