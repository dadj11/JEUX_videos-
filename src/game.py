import pygame
from config import (SCREEN_HIGHT,SCREEN_WITH)
from sprite.cat import Cat
from typing import List
from sprite.mouse import Mouse
class Game:
    screen:pygame.surface=None
    clock:pygame.time.Clock=None
    
    
    
    
    
    def __init__(self,sise:tuple,title:str):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.mixer.music.load("./music/prettyjohn1-easter-490466.mp3")
        pygame.mixer.music.play()
        self.screen=pygame.display.set_mode(sise)
        self.clock=pygame.time.Clock()
        self.bakground=pygame.image.load("./image/bakground.jpeg").convert_alpha()
        self.font=pygame.font.Font('./fonts/my_font/static/Montserrat-BlackItalic.ttf',40)
        
        pygame.display.set_caption(title)
        self.cat_groupe=pygame.sprite.Group()
        self.mouse_groupe=pygame.sprite.Group()
        self.cat=Cat((200,SCREEN_HIGHT-140))
      
        self.life_score=self.font.render(f"score : {self.cat.life_score}", False, 'white', None)
       
        self.cat_groupe.add(self.cat)

    def genarate_mouses(self,nb_mouses):
        cat_x=self.cat.rect.x+300
        mouse_y=SCREEN_HIGHT-100
        for i in range(nb_mouses):
            self.mouse_groupe.add(Mouse((cat_x+i*100,mouse_y)))
            

    def run_loop(self):
        runnig=True
        while runnig:
            #eccoute de l'evenement 
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    runnig=False
              
             #----update----
            
            self.update_game()
            
                    
            self.clock.tick(10)
            
             # ----- le rendu ----
            #self.screen.fill("gray" )
            if self.cat.is_instart_position:
                self.genarate_mouses(4)
                self.cat.set_not_in_start_position()
            self.screen.blit(self.bakground,(0,0)) 
            # self.screen.blit(self.score_text, (900, 10))
            self.screen.blit(self.life_score, (850, 25))
            self.cat_groupe.draw(self.screen)
            self.mouse_groupe.draw(self.screen)
            pygame.display.flip()
            
    def update_game(self) : 
        self.cat_groupe.update() 
        self.mouse_groupe.update()  
        sprite_liste=pygame.sprite.spritecollide(self.cat,self.mouse_groupe,True) 
        if sprite_liste!=[]:
            self.cat.eat(sprite_liste)
        self.life_score=self.font.render(f"score : {self.cat.life_score}", False, 'white', None)
            # cat1=self.cats[0] 
       
       # print(self.cate.rect)
       
        # for self.cat in self.cats:  
        #   self.screen.blit(self.cat.image,self.cat.rect)
        
    
    

        pygame.quit
            
print("je suis dans game")