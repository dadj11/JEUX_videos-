import pygame

pygame.init

screen=pygame.display.set_mode((1080,720)) 
pygame.display.set_caption("Coure N2 : jeux video")
clock=pygame.time.Clock()

# ---- Personnage -----
cat = pygame.image.load("./image/cat_spritesheet.png").convert_alpha()
print(cat.get_rect())

fram_Whitdh=204
fram_height=204



frames=[]
for j in range(2):
     for i in range(3):
   
            frame= cat.subsurface(204*i,204*j,fram_Whitdh,fram_height)
            frames.append(frame)
            print(frame.get_rect())

current_frame_index=0
current_cate_x=0

runnig=True
while runnig:
    
    
    
 # ------- eccoute de l'evenement --------
  
    for event in pygame.event.get():
        # print(event.type)
        # print(pygame.K_DOWN)
        if event.type== pygame.QUIT:
            runnig=False
    
    
    

 # ---- update -----
    kes=pygame.key.get_pressed()
    print(kes[pygame.K_RIGHT])
    if kes[pygame.K_RIGHT]:
        current_cate_x+=10
        current_frame_index+=1
        if current_frame_index ==3:
            current_frame_index=0
        print("touche de direction droit ")
   
    
    
    screen.fill("gray" ) 
    screen.blit(frames[current_frame_index],(current_cate_x,0))
    
    # i+=1
    # if i==3:
    #     i=0
    
    
    
        
 # ----- le rendu ----
    
    pygame.display.flip()
    clock.tick(3)
    
    
    
    

pygame.quit