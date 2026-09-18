import pygame

pygame.init

screen=pygame.display.set_mode((1080,720)) 
pygame.display.set_caption("Coure N2 : jeux video")
clock=pygame.time.Clock()

x=0
y=0
vilosite=10
runnig=True
direction=1
directionx=1
while runnig:
    
    #eccoute de l'evenement 
    for event in pygame.event.get():
        # print(event.type)
        # print(pygame.K_DOWN)
        if event.type== pygame.QUIT:
            runnig=False
        # if event.type==pygame.KEYDOWN:
        #     print("key up presser")
        #     if event.key ==pygame.K_DOWN:
        #         y+=vilosite
        #         print(f"key up presser  .. {event.key}")
        #     elif event.key ==pygame.K_UP:
        #         y-=vilosite
        #         print(f"key up presser  .. {event.key}")
        #     elif event.key ==pygame.K_RIGHT:
        #         x+=vilosite
        #         print(f"key up presser  .. {event.key}")
        #     elif event.key ==pygame.K_LEFT:
        #         x-=vilosite
        #         print(f"key up presser  .. {event.key}")
    key=pygame.key.get_pressed()
    # print(key)
    # print(pygame.K_a)
    # print(key[pygame.K_DOWN] )
    if key[pygame.K_DOWN] :
            y+=vilosite
            print(f"key up presser  .. {event.key}")
    elif key[pygame.K_UP]  :
                y-=vilosite
                print(f"key up presser  .. {event.key}")
    elif key[pygame.K_RIGHT] :
                x+=vilosite
                print(f"key up presser  .. {event.key}")
    elif key[pygame.K_LEFT]  :
                x-=vilosite
                print(f"key up presser  .. {event.key}")
    
    
    
    # update
    screen.fill("gray" ) 
    
      # nouvell surface 
    carre=pygame.Surface((100,100))
    
    carre.set_alpha(128)
    carre_rect=carre.get_rect()
    carre_rect.left=60
    # print(carre_rect)
    
    screen.blit(carre,carre_rect)
    
    #charger l'image
    image_pygame= pygame.image.load('./image/logo_lofi.png')
    #optimiser le chargement de l'image
    # image_pygame= image_pygame.convert()
    image_pygame=image_pygame.convert_alpha()
    image_pygame_rect= image_pygame.get_rect()
    image_pygame_rect.left=80
    
    # print(image_pygame)
    #ajouter a l'ecran
    screen.blit(image_pygame,image_pygame_rect)
    
    
    #annimation de surface
    screen_whith= screen.get_width()
    screen_height= screen.get_height()
    personnage= pygame.Surface((150,150))
    personnage.fill("purple")
    
    # x=(screen_whith//2)-(personnage.get_width()//2)
    # y=(screen_height//2)-(personnage.get_height()//2)
    
    # 
    
    # y+=vitesse*direction
    # x+=vitesse*directionx
    
    # if  (screen_whith-personnage.get_width())==x :
    #     directionx=-1
    # if x==0:
    #     directionx=1
        
    # if ((screen.get_height())-personnage.get_height())==y :
    #     direction=-1
    # if y==0:
    #     direction=1
      
    screen.blit(personnage,(x,y))
    
    clock.tick(60)
    
    # le rendu 
    pygame.display.flip()
    
    
    

pygame.quit