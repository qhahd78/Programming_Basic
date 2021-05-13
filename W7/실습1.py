import pygame.mixer # mmixer 임포트. 사운드를 메모리에 적재 후 연주한다. 

sounds = pygame.mixer 
sounds.init() # 사운드 초기화 

def wait_finish(channel): # 함수 정의 
    while channel.get_busy(): # get_busy() 가 거짓일 때까지 반복 
        pass # 아무일도 하지 않고 넘어간다. 

s = sounds.Sound("heartbeat.wav") # Sound 객체 생성 
wait_finish(s.play()) # 

s2 = sounds.Sound("buzz.wav")
wait_finish(s2.play())

s3 = sounds.Sound("ohno.wav")
wait_finish(s3.play())

s4 = sounds.Sound("carhorn.wav")
wait_finish(s4.play())