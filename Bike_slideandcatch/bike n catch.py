# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:21:16 2024

@author: Ryan Miller
"""

import pygame, random, simpleGE

class Plankton (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Plankton.png")
        self.setSize(90,50)
        self.position = (300,400)
        self.moveSpeed = 10
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        
        
class Patty(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("kPatty.png")
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
        self.setImage("spongebobroad.jpg")
        self.sndGas = simpleGE.Sound("plaugh.mp3")
        
        self.plankton = Plankton(self)
        
        self.gases = []
        for i in range(3):
            self.gases.append(Patty(self))
            
        self.sprites = [self.plankton,
                        self.gases]
        
        
    def process(self):
      
        for gas in self.gases:
            if self.Plankton.collidesWith(gas):
                self.sndKpatty.play()
                Patty.reset() 

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()