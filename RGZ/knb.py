import pygame as pg
import random
def knbshka():
    options = ['Камень', 'Ножницы', 'Бумага']

    image_paths = {
        "rock": "assets/rock.png",
        "paper": "assets/paper.png",
        "scissors": "assets/scissors.png",
        "win": "assets/win.png",
        "lose": "assets/lose.png",
        "draw": "assets/draw.png",
    }

    pg.init()

    WIDTH, HEIGHT = 600, 400
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Камень, Ножницы, Бумага")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BUTTON_COLOR = (169, 169, 169)
    BUTTON_HOVER_COLOR = (200, 200, 200)

    font = pg.font.SysFont(None, 40)
    button_font = pg.font.SysFont(None, 30)

    def draw_text(text, font, color, x, y):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

    def computer_choice():
        return random.choice(options)

    def determine_winner(player, computer):
        if player == computer:
            return "Ничья"
        elif (player == 'Камень' and computer == 'Ножницы') or \
            (player == 'Ножницы' and computer == 'Бумага') or \
            (player == 'Бумага' and computer == 'Камень'):
            return "Вы победили!"
        else:
            return "Вы проиграли!"

    def draw_button(text, x, y, width, height, color, hover_color):
        mouse_x, mouse_y = pg.mouse.get_pos()
        button_rect = pg.Rect(x, y, width, height)
        if button_rect.collidepoint(mouse_x, mouse_y):
            pg.draw.rect(screen, hover_color, button_rect)
        else:
            pg.draw.rect(screen, color, button_rect)
        draw_text(text, button_font, BLACK, x + 50, y + 15)

    def play_rps():
        running = True
        player_choice = ""
        computer_choice_str = ""
        result = ""
        rounds_left = 3  # Количество раундов
        a, b = 0, 0  # Счет игрока и компьютера

        while running:
            screen.fill(WHITE)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                    # Проверка нажатия на кнопки
                    if 100 <= mouse_x <= 300 and 150 <= mouse_y <= 200:
                        player_choice = 'Камень'
                    elif 100 <= mouse_x <= 300 and 200 <= mouse_y <= 250:
                        player_choice = 'Ножницы'
                    elif 100 <= mouse_x <= 300 and 250 <= mouse_y <= 300:
                        player_choice = 'Бумага'

                    if player_choice:
                        computer_choice_str = computer_choice()
                        result = determine_winner(player_choice, computer_choice_str)
                        if result == "Вы победили!":
                            a += 1
                        elif result == "Вы проиграли!":
                            b += 1
                        rounds_left -= 1
                        player_choice = ""  # Сброс выбора игрока

                draw_button("Камень", 100, 150, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)
                draw_button("Ножницы", 100, 200, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)
                draw_button("Бумага", 100, 250, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)

                if player_choice:
                    draw_text(f"Вы выбрали: {player_choice}", font, (0, 255, 0), 100, 300)
                    draw_text(f"Компьютер выбрал: {computer_choice_str}", font, (255, 0, 0), 100, 350)
                    draw_text(result, font, BLACK, 100, 400)

                if rounds_left == 0:
                    # Показать результат
                    if a > b:
                        result_image = pg.image.load(image_paths["win"])
                    elif a < b:
                        result_image = pg.image.load(image_paths["lose"])
                    else:
                        result_image = pg.image.load(image_paths["draw"])
                    result_image = pg.transform.scale(result_image, (300, 200))
                    screen.blit(result_image, (150, 50))

                pg.display.flip()
                pg.time.Clock().tick(30)
    play_rps()

