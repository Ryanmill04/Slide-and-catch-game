# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:54:27 2024

@author: Ryan Miller
"""

import pygame, random
import simpleGE

class bike (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("bike.png")
        self.setSize(90,50)
        self.position = (300,400)
        self.moveSpeed = 10
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        
        
class women(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("women.png")
        self.setSize(20,20)
        self.reset()
        
    def Bounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
        
    def reset(self):
      self.y = 12
      self.x = random.randint(0, self.screenWidth)
      self.dy = random.randint(3, 8)
        
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Abandoned.jpg")
        self.sndwomen = simpleGE.Sound("Excited_scream.wav")
        
        self.bike = bike(self)
        
        self.women = []
        for i in range(3):
            self.women.append(women(self))
            
        self.sprites = [self.bike,
                        self.women]
        
        
    def process(self):
      
        for women in self.women:
            if self.bike.collidesWith(women):
                self.sndwomen.play()
                women.reset() 

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()