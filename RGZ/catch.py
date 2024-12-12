import pygame as pg
import random
import menu

def catcher():
    pg.init()

    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Поймай фрукт")
    clock = pg.time.Clock()

    object_width, object_height = 100, 100
    player_width, player_height = 200, 10
    object_speed = 20
    player_speed = 10
    lives = 3
    score = 0

    white = (255, 255, 255)
    blue = (0, 0, 255)
    black = (0, 0, 0)

    fruit_image = pg.image.load("assets/fruit.png")  # Замените на свой путь к изображению
    fruit_image = pg.transform.scale(fruit_image, (object_width, object_height))

    object_x = random.randint(0, 750)
    object_y = 0
    player_x = 300
    player_y = 550
    start_counter = 0

    font = pg.font.SysFont(None, 35)
    lives_font = pg.font.SysFont(None, 25)

    def reset_game():
        nonlocal object_x, object_y, player_x, score, lives, game_started
        object_x = random.randint(0, 750)
        object_y = 0
        player_x = 300
        score = 0
        lives = 3
        game_started = True  # Устанавливаем флаг game_started в True, чтобы начать игру заново.
    
    

    running = True
    game_started = False
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if start_counter == 0:
                
                    screen.fill(white)
                    title_text = font.render("Поймай фрукт", True, black)
                    screen.blit(title_text, (300, 150))
                    start_button_rect = pg.Rect(300, 250, 200, 50)
                    pg.draw.rect(screen, (169, 169, 169), start_button_rect)
                    start_button_text = font.render("Играть", True, black)
                    start_text_rect = start_button_text.get_rect(center=start_button_rect.center)

                    back_button = pg.Rect(300, 0, 200, 50)
                    pg.draw.rect(screen, (169, 169, 169), back_button)
                    back_button_text = font.render("Назад", True, black)
                    back_text_rect = back_button_text.get_rect(center=back_button.center)

                    screen.blit(back_button_text, back_text_rect)
                    screen.blit(start_button_text, start_text_rect)
                    if event.type == pg.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        if start_button_rect.collidepoint(mouse_x, mouse_y):
                            start_counter += 1
                            game_started = True
                        if back_text_rect.collidepoint(mouse_x, mouse_y):
                            menu.menu()


            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if lives == 0:
                    restart_button_rect = pg.Rect(300, 300, 200, 50)
                    back_button = pg.Rect(300, 0, 200, 50)
                    if restart_button_rect.collidepoint(mouse_x, mouse_y):
                        reset_game()
                    if back_text_rect.collidepoint(mouse_x, mouse_y):
                        menu.menu()
                

        if game_started:
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] and player_x > 0:
                player_x -= player_speed
            if keys[pg.K_RIGHT] and player_x < 600:
                player_x += player_speed

            object_y += object_speed

            if player_x < object_x + object_width and player_x + player_width > object_x:
                if player_y < object_y + object_height and player_y + player_height > object_y + object_height - 10:
                    score += 1
                    object_x = random.randint(0, 750)
                    object_y = 0

            if object_y > 600:
                lives -= 1
                if lives == 0:
                    game_started = False
                object_x = random.randint(0, 750)
                object_y = 0

            screen.fill(white)
            screen.blit(fruit_image, (object_x, object_y))
            pg.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))

            score_text = font.render(f"Счет: {score}", True, black)
            screen.blit(score_text, (10, 10))

            lives_text = lives_font.render(f"Жизней: {lives}", True, black)
            screen.blit(lives_text, (700, 10))

            if lives == 0:
                game_over_text = font.render("Игра окончена", True, black)
                screen.blit(game_over_text, (300, 250))

                restart_button_rect = pg.Rect(300, 300, 200, 50)
                pg.draw.rect(screen, (169, 169, 169), restart_button_rect)
                restart_button_text = font.render("Перезапуск", True, black)
                text_rect = restart_button_text.get_rect(center=restart_button_rect.center)
                screen.blit(restart_button_text, text_rect)
                back_button = pg.Rect(300, 0, 200, 50)
                pg.draw.rect(screen, (169, 169, 169), back_button)
                back_button_text = font.render("Назад", True, black)
                back_text_rect = back_button_text.get_rect(center=back_button.center)
                screen.blit(back_button_text, back_text_rect)


        pg.display.flip()
        clock.tick(60)

    pg.quit()
