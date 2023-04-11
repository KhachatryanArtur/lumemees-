import pygame

pygame.init()

ekraani_pind = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Khachatryan-lumemees")

white = ("#FFFFFF")
black = ("#000000")
orange = ("#FF8C00")
lightblue = ("#00BFFF")
gray = ("#DCDCDC")


ekraani_pind.fill(lightblue)

pygame.draw.circle(ekraani_pind, white, (150, 100), 30)
pygame.draw.circle(ekraani_pind, white, (150, 160), 40)
pygame.draw.circle(ekraani_pind, white, (150, 220), 50)

pygame.draw.circle(ekraani_pind, black, (140, 85), 5)
pygame.draw.circle(ekraani_pind, black, (160, 85), 5)


pygame.draw.circle(ekraani_pind, black, (150, 135), 4)
pygame.draw.circle(ekraani_pind, black, (150, 155), 4)
pygame.draw.circle(ekraani_pind, black, (150, 175), 4)
pygame.draw.circle(ekraani_pind, black, (150, 205), 4)
pygame.draw.circle(ekraani_pind, black, (150, 225), 4)
pygame.draw.circle(ekraani_pind, black, (150, 245), 4)


pygame.draw.polygon(ekraani_pind, orange, [(150, 115), (145, 100), (155, 100)])


pygame.draw.circle(ekraani_pind, gray, (120, 270), 25)
pygame.draw.circle(ekraani_pind, gray, (180, 270), 25)



pilt=pygame.image.load("päike.png")
ekraani_pind.blit(pilt,(1, 1))

ristkülik=pygame.Rect(0, 285, 300, 300 )
pygame.draw.rect(ekraani_pind, ("#DCDCDC"), ristkülik)





pygame.display.update()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

pygame.quit()
