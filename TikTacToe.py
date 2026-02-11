import time
import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption('Shapes')
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

def show_text(msg,x,y,color):
  fontobj=pygame.font.SysFont('freesans',100)
  msgobj=fontobj.render(msg,False,color)
  screen.blit(msgobj,(x,y))
pygame.draw.rect(screen,green,(50,250,200,100))
show_text('Play',50,250,black)
pygame.display.update()

pygame.draw.rect(screen,red,(350,250,200,100))
show_text('Quit',350,250,black)
pygame.display.update()

show_text('Tic Tac Toe',25,100,white)
pygame.display.update()

def show_text(msg,x,y,color):
  fontobj=pygame.font.SysFont('freesans',25)
  msgobj=fontobj.render(msg,False,color)
  screen.blit(msgobj,(x,y))
show_text('creator: Ben Gomes',200,200,white)
pygame.display.update()
f=0

z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
def game():
  global f

  a=red
  b=blue

  def show_text(msg,x,y,color):
     fontobj=pygame.font.SysFont('freesans',175)
     msgobj=fontobj.render(msg,False,color)
     screen.blit(msgobj,(x,y))
  
  for x in range(0,600,200):
     for y in range(0,600,200):
        pygame.draw.line(screen,blue,(0,200),(600,200),10)
        pygame.draw.line(screen,blue,(0,400),(600,400),10)
        pygame.draw.line(screen,blue,(200,0),(200,600),10)
        pygame.draw.line(screen,blue,(400,0),(400,600),10)
        a,b=b,a

     def X(x,y):
        pygame.draw.line(screen,red,(x,y),(x+100,y+100),7)
        pygame.draw.line(screen,red,(x,y+100),(x+100,y),7)


     def O(x,y):
         pygame.draw.circle(screen,green,(x,y),70,5)

     def show_text(msg,x,y,color):
        fontobj=pygame.font.SysFont('freesans',175)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))


     def win():
        global z
        #print(z)
        if z[1]==z[2]==z[3]=='x':
           show_text('X wins',40,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()
        if z[4]==z[5]==z[6]=='x':
           show_text('X wins',40,200,white)
           pygame.display.update()
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()
        if z[7]==z[8]==z[9]=='x':
           show_text('X wins',40,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()

           
        if z[1]==z[4]==z[7]=='x':
           show_text('X wins',40,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()
        if z[2]==z[5]==z[8]=='x':
           show_text('X wins',40,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()
        if z[3]==z[6]==z[9]=='x':
           show_text('X wins',40,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()

           
        if z[1]==z[5]==z[9]=='x':
           show_text('X wins',40,200,white)
           pygame.display.time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()
        if z[3]==z[5]==z[7]=='x':
           show_text('X wins',40,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()



        if z[1]==z[2]==z[3]=='o':
           show_text('O wins',50,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()
        if z[4]==z[5]==z[6]=='o':
           show_text('O wins',50,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()
        if z[7]==z[8]==z[9]=='o':
           show_text('O wins',50,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()

           
        if z[1]==z[4]==z[7]=='o':
           show_text('O wins',50,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()
        if z[2]==z[5]==z[8]=='o':
           show_text('O wins',50,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()
        if z[3]==z[6]==z[9]=='o':
           show_text('O wins',50,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()


        if z[1]==z[5]==z[9]=='o':
           show_text('O wins',50,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()
        if z[3]==z[5]==z[7]=='o':
           show_text('O wins',50,200,white)
           pygame.display.update()
           time.sleep(2)
           z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
           menu()

     #z={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}

     while True:
        pygame.display.update()
        win()
        for event in pygame.event.get():
           #print(event)
           if event.type==QUIT:
              pygame.quit()
              exit()

           elif event.type==pygame.MOUSEBUTTONUP and event.button==1:
              x,y=event.pos     
              if x in range(0,200) and y in range(0,200):
                 if z[1]=='_':
                    if f==0:
                       z[1]='x'
                       x=50
                       y=50
                       X(x,y)
                       f=1
                    
                    elif f==1:
                       z[1]='o'
                       x=100
                       y=100
                       O(x,y)
                       f=0
                   
              elif x in range(200,400) and y in range(0,200):
                    if z[2]=='_':
                       if f==0:
                          z[2]='x'
                          x=250
                          y=50
                          X(x,y)
                          f=1

                       elif f==1:
                          z[2]='o'
                          x=300
                          y=100
                          O(x,y)
                          f=0
                
                    
              elif x in range(400,600) and y in range(0,200):
                    if z[3]=='_':
                       if f==0:
                          z[3]='x'
                          x=450
                          y=50
                          X(x,y)
                          f=1

                       elif f==1:
                          z[3]='o'
                          x=500
                          y=100
                          O(x,y)
                          f=0
               
                    
              elif x in range(0,200) and y in range(200,400):
                    if z[4]=='_':
                       if f==0:
                          z[4]='x'
                          x=50
                          y=250
                          X(x,y)
                          f=1

                       elif f==1:
                          z[4]='o'
                          x=100
                          y=300
                          O(x,y)
                          f=0

                    
              elif x in range(200,400) and y in range(200,400):
                    if z[5]=='_':
                       if f==0:
                          z[5]='x'
                          x=250
                          y=250
                          X(x,y)
                          f=1

                       elif f==1:
                          z[5]='o'
                          x=300
                          y=300
                          O(x,y)
                          f=0
                      
                    
              elif x in range(400,600) and y in range(200,400):
                    if z[6]=='_':
                       if f==0:
                          z[6]='x'
                          x=450
                          y=250
                          X(x,y)
                          f=1

                       elif f==1:
                          z[6]='o'
                          x=500
                          y=300
                          O(x,y)
                          f=0

                       
                                            
                 
                    
              elif x in range(0,200) and y in range(400,600):
                    if z[7]=='_':
                       if f==0:
                          z[7]='x'
                          x=50
                          y=450
                          X(x,y)
                          f=1

                       elif f==1:
                          z[7]='o'
                          x=100
                          y=500
                          O(x,y)
                          f=0

                       
              
                    
              elif x in range(200,400) and y in range(400,600):
                    if z[8]=='_':
                       if f==0:
                          z[8]='x'
                          x=250
                          y=450
                          X(x,y)
                          f=1

                       elif f==1:
                          z[8]='o'
                          x=300
                          y=500
                          O(x,y)
                          f=0

                       

                       
                    
              elif x in range(400,600) and y in range(400,600):
                    if z[9]=='_':
                       if f==0:
                          z[9]='x'
                          x=450
                          y=450
                          X(x,y)
                          f=1

                       elif f==1:
                          z[9]='o'
                          x=500
                          y=500
                          O(x,y)
                          f=0



                  
def menu():
  screen.fill(black)

  def show_text(msg,x,y,color):
     fontobj=pygame.font.SysFont('freesans',100)
     msgobj=fontobj.render(msg,False,color)
     screen.blit(msgobj,(x,y))
  pygame.draw.rect(screen,green,(50,250,200,100))
  show_text('Play',50,250,black)
  pygame.display.update()

  pygame.draw.rect(screen,red,(350,250,200,100))
  show_text('Quit',350,250,black)
  pygame.display.update()

  show_text('Tic Tac Toe',25,100,white)
  pygame.display.update()

  def show_text(msg,x,y,color):
     fontobj=pygame.font.SysFont('freesans',25)
     msgobj=fontobj.render(msg,False,color)
     screen.blit(msgobj,(x,y))
  show_text('creator: Ben Gomes',200,200,white)
  pygame.display.update()
  f=0
  
  while True:
     pygame.display.update()
     for event in pygame.event.get():
        if event.type==QUIT:
           pygame.quit()
           exit()

        elif event.type==pygame.MOUSEBUTTONUP and event.button==1:
           x,y=event.pos
           if x in range(50,250) and y in range (250,350):
              screen.fill(black)
              game()
           elif x in range(350,550) and y in range(250,350):
              pygame.quit()
              exit()
menu()
