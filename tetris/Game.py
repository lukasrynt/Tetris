import pygame
from tetris.Tetris import Tetris
from tetris.Colors import colors, GRAY, BLACK, RED, CYAN, MAGENTA, DARK_GRAY, DIM_GRAY


class Game:
    """
    Class responsible for handling image processing and pygame

    size: size of the screen
    screen: screen used by pygame
    game_on: decides whether the game is currently running
    done: decides whether the main menu should be closed
    clock: timer for the game
    fps: frames per seconds
    tetris: current game
    counter: counter of fps - run action only if it is allowed
    accelerated: decides whether down button is currently being held for purpose of piece acceleration
    click: decides whether the mouse button click occured to handle button clickss
    """

    size = (400, 500)
    screen = pygame.display.set_mode(size)
    game_on = True
    done = False
    clock = pygame.time.Clock()
    fps = 48
    tetris = Tetris(20, 10)
    counter = 0
    accelerated = False
    click = False

    def __init__(self):
        pygame.font.init()
        pygame.display.set_caption("Tetris")
        self.font = pygame.font.SysFont('comicsansms', 25)
        self.font1 = pygame.font.SysFont('comicsansms', 65)

    def main_menu(self):
        """
        Represents the main menu of the game
        """

        while not self.done:
            self.screen.fill(DARK_GRAY)

            self.tetris_text()
            self.new_button()
            self.continue_button()
            self.quit_button()

            for evt in pygame.event.get():
                if evt.type == pygame.MOUSEBUTTONDOWN:
                    self.click = True
                if evt.type == pygame.QUIT or evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE:
                    self.done = True

            pygame.display.flip()

    def tetris_text(self):
        """
        Creates a Tetris header for the main menu
        """
        x, y, width, height = 100, 50, 200, 50
        font = pygame.font.SysFont("comicsansms", 72)
        text = font.render("Tetris", True, GRAY)
        self.screen.blit(text, text.get_rect(center=(x + width/2, y + height/2)))


    def new_button(self):
        """
        Creates a 'New Game' button
        """

        x, y, width, height = 100, 100, 200, 50
        new_game = pygame.Rect(x, y, width, height)
        inside = pygame.Rect(x + 2, y + 2, width - 2, height - 2)
        text = self.font.render("New Game", True, GRAY)
        if new_game.collidepoint(pygame.mouse.get_pos()):
            if self.click:
                self.game_on = True
                self.click = False
                self.tetris = Tetris(20, 10)
                self.main_loop()
        pygame.draw.rect(self.screen, GRAY, new_game, 2)
        pygame.draw.rect(self.screen, RED, inside)
        self.screen.blit(text, text.get_rect(center=(x + width/2, y + height/2)))

    def continue_button(self):
        """
        Creates a 'Continue Game' button
        """

        x, y, width, height = 100, 200, 200, 50
        continue_game = pygame.Rect(x, y, width, height)
        inside = pygame.Rect(100 + 2, 200 + 2, 200 - 2, 50 - 2)
        text = self.font.render("Continue Game", True, GRAY)
        if continue_game.collidepoint(pygame.mouse.get_pos()):
            if self.click:
                self.game_on = True
                self.click = False
                if self.tetris.game_on:
                    self.main_loop()
        pygame.draw.rect(self.screen, GRAY, continue_game, 2)
        pygame.draw.rect(self.screen, CYAN, inside)
        self.screen.blit(text, text.get_rect(center=(x + width/2, y + height/2)))

    def quit_button(self):
        """
        Creates a 'Quit Game' button
        """

        x, y, width, height = 100, 300, 200, 50
        quit_game = pygame.Rect(x, y, width, height)
        inside = pygame.Rect(100 + 2, 300 + 2, 200 - 2, 50 - 2)
        text = self.font.render("Quit Game", True, GRAY)
        if quit_game.collidepoint(pygame.mouse.get_pos()):
            if self.click:
                self.done = True
        pygame.draw.rect(self.screen, GRAY, quit_game, 2)
        pygame.draw.rect(self.screen, MAGENTA, inside)
        self.screen.blit(text, text.get_rect(center=(x + width/2, y + height/2)))

    def main_loop(self):
        """
        Main loop of the game, all game logic is centered here
        """

        while self.game_on:
            if self.tetris.piece is None:
                self.tetris.new_piece()

            self.counter += 1
            if self.counter % (self.fps - 5 * self.tetris.level) == 0 or self.accelerated:
                if self.tetris.game_on:
                    self.tetris.move_down()

            for evt in pygame.event.get():
                self.handle_events(evt)

            self.screen.fill(DARK_GRAY)
            self.render_area()

            if self.tetris.piece is not None:
                self.render_piece()

            self.render_texts()

            pygame.display.flip()
            self.clock.tick(self.fps)

    def handle_events(self, evt: pygame.event):
        """
        Handles user input and events
        :param evt: Event to be handled
        """

        if self.tetris.piece is not None:
            if evt.type == pygame.KEYDOWN:
                if self.tetris.game_on:
                    if evt.key == pygame.K_UP:
                        self.tetris.rotate()
                    if evt.key == pygame.K_LEFT:
                        self.tetris.move_side(-1)
                    if evt.key == pygame.K_RIGHT:
                        self.tetris.move_side(1)
                    if evt.key == pygame.K_DOWN:
                        self.accelerated = True
                if evt.key == pygame.K_ESCAPE:
                    self.game_on = False

        if evt.type == pygame.KEYUP:
            if evt.key == pygame.K_DOWN:
                self.accelerated = False

        if evt.type == pygame.QUIT:
            self.game_on = False

    def render_area(self):
        """
        Creates all blocks in the area, imprinted Tetromiones and blank spots
        """

        for y in range(self.tetris.height):
            for x in range(self.tetris.width):
                pygame.draw.rect(self.screen, GRAY,
                                 self.tetris.render_blank_elem_size(x, y), 1)
                if self.tetris.field[y][x] > 0:
                    pygame.draw.rect(self.screen, colors[self.tetris.field.astype(int)[y][x] - 1],
                                     self.tetris.render_filled_elem_size(x, y))
                else:
                    pygame.draw.rect(self.screen, DIM_GRAY,
                                     self.tetris.render_filled_elem_size(x, y))

    def render_piece(self):
        """
        Prints the current piece on the output
        """

        for p in self.tetris.piece.render():
            pygame.draw.rect(self.screen, colors[self.tetris.piece.color],
                             self.tetris.render_filled_elem_size(
                                 p % 4 + self.tetris.piece.x,
                                 p // 4 + self.tetris.piece.y))

    def render_texts(self):
        """
        Creates all text needed for game
        """

        score = self.font.render("Score: " + str(self.tetris.score), True, GRAY)
        level = self.font.render("Level: " + str(self.tetris.level), True, GRAY)
        self.screen.blit(score, [0, 0])
        self.screen.blit(level, [0, 20])

        if not self.tetris.game_on:
            text_game_over = self.font1.render("Game Over", True, (255, 125, 0))
            text_game_over1 = self.font1.render("Press ESC", True, (255, 215, 0))
            self.screen.blit(text_game_over, [20, 200])
            self.screen.blit(text_game_over1, [25, 265])
