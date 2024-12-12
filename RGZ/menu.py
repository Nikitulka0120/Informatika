import pygame as pg
import sea
import catch
import knb

def menu():
    pg.init()

    screen = pg.display.set_mode((370, 320))
    pg.display.set_caption("Главное меню")
    clock = pg.time.Clock()

    white = (255, 255, 255)
    gray = (169, 169, 169)
    black = (0, 0, 0)

    font = pg.font.SysFont(None, 40)

    buttons = [
        {"label": "Морской бой", "rect": pg.Rect(10, 10, 350, 50)},
        {"label": "Камень, ножницы, бумага", "rect": pg.Rect(10, 90, 350, 50)},
        {"label": "Поймай фрукт", "rect": pg.Rect(10, 170, 350, 50)},
        {"label": "Выход", "rect": pg.Rect(10, 250, 350, 50)}
    ]

    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for button in buttons:
                    if button["rect"].collidepoint(mouse_x, mouse_y):
                        if button["label"] == "Морской бой":
                            sea.sea_game()
                        # elif button["label"] == "Камень, ножницы, бумага":
                        #     knb.knbshka()
                        elif button["label"] == "Поймай фрукт":
                            catch.catcher()
                        elif button["label"] == "Выход":
                            running = False

        screen.fill(white)

        for button in buttons:
            pg.draw.rect(screen, gray, button["rect"])
            text = font.render(button["label"], True, black)
            text_rect = text.get_rect(center=button["rect"].center)
            screen.blit(text, text_rect)

        pg.display.flip()
        clock.tick(30)

    pg.quit()
