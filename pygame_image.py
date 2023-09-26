import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230926/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)

    kk_img = pg.image.load("ex01-20230926/fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)

    kk_img3 = pg.transform.rotate(kk_img,3)
    kk_img4 = pg.transform.rotate(kk_img,6)
    kk_img5 = pg.transform.rotate(kk_img,9)
    kk_img6 = pg.transform.rotate(kk_img,12)
    kk_img7 = pg.transform.rotate(kk_img,9)
    kk_img8 = pg.transform.rotate(kk_img,6)
    kk_img9 = pg.transform.rotate(kk_img,3)
    kk_imgs = [kk_img,kk_img3,kk_img4,kk_img5,kk_img6,kk_img7,kk_img8,kk_img9]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2,[1600-x,0])
        screen.blit(bg_img,[3200-x,0])

        screen.blit(kk_imgs[tmr%2],[300,200])


        pg.display.update()
        tmr += 1      
        clock.tick(1000)

    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()