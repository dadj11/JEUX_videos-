import pygame
from config import(SCREEN_HIGHT,SCREEN_WITH)
from sprite.mouse import Mouse 
class Cat(pygame.sprite.Sprite):
   image:pygame.Surface=None
   rect:pygame.Rect=None
   frames:list[pygame.Surface]
   curent_frame_index:int
   is_instart_position:bool
   life_score:int
   
  
    
   def __init__(self,position:tuple ):
      super().__init__() 
      #la position a pour valeur (x,y)
      self.eat_musique=pygame.mixer.Sound("./music/FOODEat_Pomme croquee 5 (ID 3083)_LaSonotheque.fr.wav")
      # self.nb_eat_food=0
      self.load_sprite_sheet()
      self.is_instart_position=True
      self.life_score=0 #0 a 7
      print(self.frames)
      self.curent_frame_index=0
      self.image=self.frames[self.curent_frame_index]
      self.rect=self.image.get_rect(center=position)
   def decrement_life_score(self):
       self.life_score-=1 if self.life_score >= 1 else 0
   def increment_life_score(self):
      self.life_score+=1 if 7>self.life_score else 0
   def eat(self,mouses :list[Mouse]):
        self.eat_musique.play()
        for mouse in mouses:
          if mouse.is_sik:
            self.decrement_life_score()
          else:
             self.increment_life_score()
            
   def set_in_start_position(self):
             self.is_instart_position=True
   def set_not_in_start_position(self):
             self.is_instart_position=False
   def reset_position(self):
               self.rect.x=0
               self.set_in_start_position()
         
   def load_sprite_sheet(self):
            cat=pygame.image.load("./image/cat_spritesheet.png").convert_alpha()
            print(cat.get_rect())
            fram_Whitdh=204
            fram_height=204
            self.frames=[]
            for j in range(2):
                for i in range(3):
                
                    frame= cat.subsurface(204*i,204*j,fram_Whitdh,fram_height)
                    self.frames.append(frame)
                    print(frame.get_rect())    
   def update(self):
        super().update()
        kes=pygame.key.get_pressed()
        if kes[pygame.K_RIGHT]:
            self.move_rigth()
        if kes[pygame.K_LEFT]:
            self.set_not_in_start_position()
            self.move_left()

   def move_rigth(self):
         self.animate_rigth()
         self.rect.x+=20
         if self.rect.x>=SCREEN_WITH:
               self.reset_position()
   def move_left(self):
         pass
#          self.animate_left()
#          self.rect.x-=20
   def animate_rigth(self):
          self.curent_frame_index+=1
          if self.curent_frame_index==3:
               self.curent_frame_index=0
          self.image=self.frames[self.curent_frame_index]
   def animate_left(self):
         self.curent_frame_index-=1
         if 0>=self.curent_frame_index:
               self.curent_frame_index=2
         self.image=self.frames[self.curent_frame_index]
