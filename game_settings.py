import pygame.font


class Game_Settings:
    food_speed = 2
    score = 0
    game_active = True

    def increase_diff(self):
        if self.score % 10 == 0:
            self.food_speed = self.score / 5 + 2


class Scoreboard:
    def __init__(self, sc):
        pygame.init()
        self.screen = sc
        self.rect = self.screen.get_rect()
        self.settings = settings

        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('Times New Roman', 48)
        self.score_image = ''
        self.score_rect = ''
        self.prep_score()

    def prep_score(self):
        import main
        score_str = str(self.settings.score)
        self.score_image = self.font.render(score_str, True, self.text_color, (200, 100, 50))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.rect.right - 30
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)


settings = Game_Settings()
