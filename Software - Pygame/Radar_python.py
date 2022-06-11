import math
from math import cos,sin
import sys
import serial
import pygame

def pie(scr,color,center,radius,start_angle,stop_angle):
    theta=start_angle
    while theta <= stop_angle:
        pygame.draw.line(scr,color,center, 
        (center[0]+radius*cos(theta*math.pi/180),center[1]+radius*sin(theta*math.pi/180)),1)
        theta+=0.01

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    label = ''
    print("Avalible ports:")
    print(serial_ports())
    x = input("Select serial port:")
    open_port = serial.Serial(x,baudrate=9600,timeout=1)

    pygame.init()
    screen = pygame.display.set_mode((800,500))
    screen.fill((0,80,0))
    for r in range(50,450,50):
        pygame.draw.circle(screen,(0,255,0),(400,400),r,1)
    for r in range(50,800,50):
        pygame.draw.line(screen,(0,255,0),(0,r),(800,r))
    for r in range(50,800,50):
        pygame.draw.line(screen,(0,255,0),(r,0),(r,800))
    pie(screen,(0,150,0),(400,400),300,180,360)
    pygame.display.update()

    running = True
    font = pygame.font.SysFont(None, 24)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

        open_port.write(b'1')
        data = open_port.read().decode('ascii')
        if(str(data)!='\n'):
            label = label + str(data)
        else:
            end_of_line = float(label.split()[1])*0.01*300
            angle = int(label.split()[0])
            pie(screen,(0,150,0),(400,400),300,179+angle,179+angle+1)
            pie(screen,(0,255,0),(400,400),300-end_of_line,179+angle,179+angle+1)
            img = font.render(f"angle:{angle}", True, (255,255,255))
            pygame.draw.rect(screen,(0,0,0),(330,420,120,40))
            screen.blit(img, (350, 430))
            label = ''
        pygame.display.update()