from config import (SCREEN_WITH,SCREEN_HIGHT)
import pygame
import random
class Mouse(pygame.sprite.Sprite):
    image:pygame.Surface=None
    rect:pygame.Rect=None
    is_sik:bool
    
    def __init__(self,position:tuple):
        super().__init__() 
        
        self.image=pygame.Surface((6,6))
        self.image=pygame.image.load("./image/mouse.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.is_sik=bool(random.randint(0,1))
        # print(self.image.get_rect())
       
        self.rect=self.image.get_rect(center=position)
        
    def mouve(self):
        self.chec_out_of_screen()
        self.rect.x+=random.randint(1,10)
        
    def chec_out_of_screen(self):
        if self.rect.x>=SCREEN_WITH:
            print('kill')
            self.kill()
        
    def update(self):
        self.mouve()
        return super().update()
      