import pygame as pg
import random
import menu


pg.init()

def sea_game():
    screen = pg.display.set_mode((1200, 400))
    pg.display.set_caption("Морской бой")
    clock = pg.time.Clock()

    matrix_size = 4
    boats = 4
    player_matrix = [['.' for _ in range(matrix_size)] for _ in range(matrix_size)]
    secret_matrix = [['.'] * matrix_size for _ in range(matrix_size)]
    bot_matrix = [['.' for _ in range(matrix_size)] for _ in range(matrix_size)]
    bot_secret_matrix = [['.' for _ in range(matrix_size)] for _ in range(matrix_size)]
    global player_boats_counter, bot_boats_counter
    player_boats_counter = boats
    bot_boats_counter = boats

    game_started = False

    hit_image = pg.image.load("assets/hit.png") 
    miss_image = pg.image.load("assets/miss.png")  
    bomb_image = pg.image.load("assets/bomb.png")  

    def matrix_fill(mat):
        for i in range(matrix_size):
            for j in range(matrix_size):
                mat[i][j] = "."

    def boats_and_bombs(matrix):
        boat_counter = 0
        while boat_counter < boats:
            i = random.randint(0, matrix_size - 1)
            j = random.randint(0, matrix_size - 1)
            if matrix[i][j] == ".":
                matrix[i][j] = "K"
                boat_counter += 1

        while True:
            i = random.randint(0, matrix_size - 1)
            j = random.randint(0, matrix_size - 1)
            if matrix[i][j] == ".":
                matrix[i][j] = "V"
                break

    matrix_fill(secret_matrix)
    boats_and_bombs(secret_matrix)
    matrix_fill(bot_secret_matrix)
    boats_and_bombs(bot_secret_matrix)

    white = (255, 255, 255)
    gray = (169, 169, 169)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    black = (0, 0, 0)
    font = pg.font.SysFont(None, 35)
    status_font = pg.font.SysFont(None, 25)

    running = True
    game_status = True
    game_message = ""

    def bot_turn():
        global game_status, game_message, player_boats_counter

        # while True:
        #     i = random.randint(0, matrix_size - 1)
        #     j = random.randint(0, matrix_size - 1)
        #     if bot_matrix[i][j] == ".":
        #         if bot_secret_matrix[i][j] == "K":
        #             bot_matrix[i][j] = "X"
        #             player_boats_counter -= 1
        #             if player_boats_counter == 0:
        #                 game_message = "Бот выиграл! Все ваши корабли потоплены."
        #                 game_status = False
        #             else:
        #                 game_message = "Бот потопил ваш корабль!"
        #         elif bot_secret_matrix[i][j] == "V":
        #             bot_matrix[i][j] = ":("
        #             game_message = "Бот попал в вашу бомбу, он проиграл!"
        #             game_status = False
        #         else:
        #             bot_matrix[i][j] = "#"
        #             game_message = "Бот промахнулся!"
        #         break

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if 500 <= mouse_x <= 700 and 0 <= mouse_y <= 80:
                    menu.menu()

                elif 500 <= mouse_x <= 700 and 200 <= mouse_y <= 280:
                    game_started = True
                    game_status = True
                    game_message = ""
                    player_matrix = [['.' for _ in range(matrix_size)] for _ in range(matrix_size)]
                    bot_matrix = [['.' for _ in range(matrix_size)] for _ in range(matrix_size)]
                    matrix_fill(secret_matrix)
                    boats_and_bombs(secret_matrix)
                    matrix_fill(bot_secret_matrix)
                    boats_and_bombs(bot_secret_matrix)
                    player_boats_counter = boats
                    bot_boats_counter = boats

                elif game_started and game_status:
                    cell_size = 100
                    row = mouse_y // cell_size
                    col = mouse_x // cell_size

                    if 0 <= row < matrix_size and 0 <= col < matrix_size:
                        if player_matrix[row][col] == ".":
                            if secret_matrix[row][col] == ".":
                                player_matrix[row][col] = "#"
                            elif secret_matrix[row][col] == "K":
                                player_matrix[row][col] = "X"
                                bot_boats_counter -= 1
                                if bot_boats_counter == 0:
                                    game_message = "Вы выиграли! Все корабли противника уничтожены."
                                    game_status = False
                            elif secret_matrix[row][col] == "V":
                                game_message = "Вы попали в бомбу и проиграли!"
                                player_matrix[row][col] = ":("
                                game_status = False

                            if game_status:
                                bot_turn()
                        else:
                            game_message = "Вы уже стреляли в эту ячейку"
                    i = random.randint(0, matrix_size - 1)
                    j = random.randint(0, matrix_size - 1)
                    if bot_matrix[i][j] == ".":
                        if bot_secret_matrix[i][j] == "K":
                            bot_matrix[i][j] = "X"
                            player_boats_counter -= 1
                            if player_boats_counter == 0:
                                game_message = "Бот выиграл! Все ваши корабли потоплены."
                                game_status = False
                        elif bot_secret_matrix[i][j] == "V":
                            bot_matrix[i][j] = ":("
                            game_message = "Бот попал в вашу бомбу, он проиграл!"
                            game_status = False
                        else:
                            bot_matrix[i][j] = "#"
                        break

        screen.fill(white)
        cell_size = 100

        for i in range(matrix_size):
            for j in range(matrix_size):
                rect = pg.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                if player_matrix[i][j] == "#":
                    pg.draw.rect(screen, gray, rect)
                    screen.blit(miss_image, rect)
                elif player_matrix[i][j] == "X":
                    pg.draw.rect(screen, red, rect)
                    screen.blit(hit_image, rect)
                elif player_matrix[i][j] == ":(":
                    pg.draw.rect(screen, black, rect)
                    screen.blit(bomb_image, rect)
                else:
                    pg.draw.rect(screen, blue, rect)

                pg.draw.rect(screen, black, rect, 2)

        for i in range(matrix_size):
            for j in range(matrix_size):
                rect = pg.Rect(j * cell_size + 800, i * cell_size, cell_size, cell_size)
                if bot_matrix[i][j] == "#":
                    pg.draw.rect(screen, gray, rect)
                    screen.blit(miss_image, rect)
                elif bot_matrix[i][j] == "X":
                    pg.draw.rect(screen, red, rect)
                    screen.blit(hit_image, rect)
                elif bot_matrix[i][j] == ":(":
                    pg.draw.rect(screen, green, rect)
                    screen.blit(bomb_image, rect)
                else:
                    pg.draw.rect(screen, blue, rect)

                pg.draw.rect(screen, black, rect, 2)

        back_button_rect = pg.Rect(500, 0, 200, 80)
        pg.draw.rect(screen, gray, back_button_rect)
        back_button_text = font.render("Назад", True, black)
        back_text_rect = back_button_text.get_rect(center=back_button_rect.center)
        screen.blit(back_button_text, back_text_rect)

        button_rect = pg.Rect(500, 200, 200, 80)
        pg.draw.rect(screen, gray, button_rect)
        button_text = font.render("Играть" if not game_started or not game_status else "Перезапуск", True, black)
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)

        status_text = status_font.render(game_message, True, black)
        status_rect = status_text.get_rect(center=(600, 300))
        screen.blit(status_text, status_rect)

        pg.display.flip()
        clock.tick(30)

    pg.quit()
