#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pygame

pygame.init()
caption = pygame.display.set_caption('Python App')
screen=pygame.display.set_mode([320,200]) # 窗口大小为 320*200
while True:
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
        pygame.quit()
 pygame.draw.rect(screen,[255,0,0],[150,10,20,40],0)
 pygame.draw.circle(screen,[0,0,0],[20,50],20,1)
 pygame.display.update()
 screen.fill([255,255,255]) # 用白色填充窗体
sys.exit()
