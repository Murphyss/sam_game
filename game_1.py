#!/usr/bin/env python

import pygame,sys

possib_col=[]
mapas = []
ini=[]
img = pygame.image.load("chao_1.png")
fundo = pygame.image.load("fundo.png")
ini_img=pygame.image.load("ini_img.png")
clock=pygame.time.Clock()
fas="1"
end_rect = 0

def load_image(name):
	image = pygame.image.load(name)
	return image

class walk_right(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super (walk_right,self).__init__()
		self.images = []
		self.images.append(load_image('pa_2.png'))
		self.images.append(load_image('pa_3.png'))
		self.images.append(load_image('pa_4.png'))
		self.images.append(load_image('pa_5.png'))
		
		self.index = 0
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)
        
        
	def update(self,x,y):
		self.index+=1
		if self.index >= len(self.images):
			self.index = 0
		
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)
		
class walk_right_v(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super (walk_right_v,self).__init__()
		self.images = []
		self.images.append(load_image('pa_2v.png'))
		self.images.append(load_image('pa_3v.png'))
		self.images.append(load_image('pa_4v.png'))
		self.images.append(load_image('pa_5v.png'))
		
		self.index = 0
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)
        
        
	def update(self,x,y):
		self.index+=1
		if self.index >= len(self.images):
			self.index = 0
		
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)

class walk_left(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super (walk_left,self).__init__()
		self.images = []
		self.images.append(load_image('pa_2l.png'))
		self.images.append(load_image('pa_3l.png'))
		self.images.append(load_image('pa_4l.png'))
		self.images.append(load_image('pa_5l.png'))
		
		self.index = 0
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)
        
        
	def update(self,x,y):
		self.index+=1
		if self.index >= len(self.images):
			self.index = 0
		
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)

class walk_left_v(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super (walk_left_v,self).__init__()
		self.images = []
		self.images.append(load_image('pa_2vl.png'))
		self.images.append(load_image('pa_3vl.png'))
		self.images.append(load_image('pa_4vl.png'))
		self.images.append(load_image('pa_5vl.png'))
		
		self.index = 0
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)
        
        
	def update(self,x,y):
		self.index+=1
		if self.index >= len(self.images):
			self.index = 0
		
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)
		
#ini_img_1.png

class Wl(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super (Wl,self).__init__()
		self.images = []
		self.images.append(load_image('ini_img_1.png'))
		self.images.append(load_image('ini_img_2.png'))
		self.images.append(load_image('ini_img_3.png'))
		self.images.append(load_image('ini_img_4.png'))
		
		self.index = 0
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)
        
        
	def update(self,x,y):
		self.index+=1
		if self.index >= len(self.images):
			self.index = 0
		
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)
		
class Wll(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super (Wll,self).__init__()
		self.images = []
		self.images.append(load_image('ini_img__1.png'))
		self.images.append(load_image('ini_img__2.png'))
		self.images.append(load_image('ini_img__3.png'))
		self.images.append(load_image('ini_img__4.png'))
		
		self.index = 0
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)
        
        
	def update(self,x,y):
		self.index+=1
		if self.index >= len(self.images):
			self.index = 0
		
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)

class para(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super (para,self).__init__()
		self.images = []
		self.images.append(load_image('para1.png'))
		self.images.append(load_image('para2.png'))
		self.images.append(load_image('para3.png'))
		self.images.append(load_image('para4.png'))
		self.images.append(load_image('para5.png'))
		
		self.index = 0
		self.image=self.images[self.index]
		self.rect = pygame.Rect(0,0,800,600)
        
        
	def update(self,x,y):
		self.index+=1
		if self.index >= len(self.images):
			self.index = 0
		
		self.image=self.images[self.index]
		self.rect = pygame.Rect(0,0,800,600)
		
		
class Atk(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super (Atk,self).__init__()
		self.images = []
		self.images.append(load_image('ff.png'))
		self.images.append(load_image('ff2.png'))
		self.images.append(load_image('ff3.png'))
		self.images.append(load_image('ff4.png'))
		self.images.append(load_image('ff5.png'))
		
		self.index = 0
		self.image=self.images[self.index]
		self.rect = pygame.Rect(0,0,19,34)
        
        
	def update(self,x,y):
		self.index+=1
		if self.index >= len(self.images):
			self.index = 0
		
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)
class Atkk(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super (Atkk,self).__init__()
		self.images = []
		self.images.append(load_image('f.png'))
		self.images.append(load_image('f2.png'))
		self.images.append(load_image('f3.png'))
		self.images.append(load_image('f4.png'))
		self.images.append(load_image('f5.png'))
		
		self.index = 0
		self.image=self.images[self.index]
		self.rect = pygame.Rect(0,0,19,34)
        
        
	def update(self,x,y):
		self.index+=1
		if self.index >= len(self.images):
			self.index = 0
		
		self.image=self.images[self.index]
		self.rect = pygame.Rect(x,y,19,34)
		
		
class Player(object):
	def __init__(self):
		self.rect = pygame.Rect(80, 526, 19, 34)
	
	
	def move(self,dx,dy):
		if dx != 0:
			self.single_move(dx,0)
		if dy != 0:
			self.single_move(0,dy)
	
	def single_move(self,dx,dy):
		self.rect.x += dx
		self.rect.y += dy
		for wal in mapas:
			if self.rect.colliderect(wal.rect):
				if dx > 0: # Moving right; Hit the left side of the wall
					self.rect.right = wal.rect.left
				if dx < 0: # Moving left; Hit the right side of the wall
					self.rect.left = wal.rect.right
				if dy > 0: # Moving down; Hit the top side of the wall
					self.rect.bottom = wal.rect.top
				if dy < 0: # Moving up; Hit the bottom side of the wall
					self.rect.top = wal.rect.bottom
					
longend=[]
longend_x_inv=[]
player = Player()
class mapa(object):
	
	def __init__(self,pos):
		
		mapas.append(self)
		self.rect = pygame.Rect(pos[0], pos[1], 40, 40)

tx = 800
ty = 600 
tela = pygame.display.set_mode((tx,ty))
		
class Inimigo(object):
	
	def __init__(self,pos):
		
		ini.append(self)
		self.rect = pygame.Rect(pos[0], pos[1], 19, 34)
		self.posafe = (pos[0], pos[1])
		for cont_d_ini in ini:
			wl = Wl(cont_d_ini.rect.x,cont_d_ini.rect.y)
			self.wll= pygame.sprite.Group(wl)
			
			at = Atk(cont_d_ini.rect.x,cont_d_ini.rect.y)
			self.atk= pygame.sprite.Group(at)
			
			ak = Atkk(cont_d_ini.rect.x,cont_d_ini.rect.y)
			self.atkk= pygame.sprite.Group(ak)
			
			wlr = Wll(cont_d_ini.rect.x,cont_d_ini.rect.y)
			self.wlr= pygame.sprite.Group(wlr)
			
			self.d=False
			self.e=False
			self.anime = False
			
		self.move()	
		self.cair()

	def move(self):
		
		
		lony = self.rect.y - player.rect.y 
		yonl = player.rect.y - self.rect.y
		
		lonor = self.rect.x - player.rect.x 
		
		if self.rect.x <= player.rect.x and lonor >= -100 and lony >= -40 and yonl >= -40:
			self.rect.x += 6
			self.e = True
			self.d = False
			self.anime = True
		elif self.rect.x >= player.rect.x and lonor <= 100 and lony >= -40 and yonl >= -40:
			self.rect.x += -6
			self.d = True
			self.e = False 
			self.anime = True
		elif self.rect.x == player.rect.x:
			self.rect.x += 0
			self.e = False 
			self.d = False
			self.anime = False
		else:
			self.anime = False
			self.e = False 
			self.d = False
		
		for wal in mapas:
			if self.rect.colliderect(wal.rect):
				if self.e: # Moving right; Hit the left side of the wall
					self.rect.right = wal.rect.left
				if self.d: # Moving left; Hit the right side of the wall
					self.rect.left = wal.rect.right
		if self.rect.colliderect(player.rect):
			if self.e: # Moving right; Hit the left side of the wall
					self.atacar("rig")
			if self.d: # Moving left; Hit the right side of the wall
					self.atacar("lef")
			
		
		
	def atacar(self,t): 
		
		if t == "rig":
			self.atk.update(self.rect.x,self.rect.y)
			self.atk.draw(tela)
		if t == "lef":
			self.atkk.update(self.rect.x,self.rect.y)
			self.atkk.draw(tela)
		self.inic()
		"""
			d=False
			e=False
			
			lon = player.rect.x - cont_d_ini.rect.x
			lonor = cont_d_ini.rect.x - player.rect.x 
			lony = cont_d_ini.rect.y - player.rect.y 
			yonl = player.rect.y - cont_d_ini.rect.y
			if lon <= -2 and lony >= -34 and yonl >= -34:
				cont_d_ini.rect.x += -5
				d = True
				e = False 
			elif lonor <= 30 and lony >= -34 and yonl >= -34:
				cont_d_ini.rect.x += 5
				self.wll.update(cont_d_ini.rect.x,cont_d_ini.rect.y)
				self.wll.draw(tela)
				e = True
				d = False
			elif lonor == 0 and lony == 0:
				cont_d_ini.rect.x += 0
				
			lony = cont_d_ini.rect.y - player.rect.y 
			yonl = player.rect.y - cont_d_ini.rect.y
			
			lonor = cont_d_ini.rect.x - player.rect.x 
			if cont_d_ini.rect.x <= player.rect.x and lonor >= -100 and lony >= -40 and yonl >= -40:
				cont_d_ini.rect.x += 5
				self.wll.update(cont_d_ini.rect.x,cont_d_ini.rect.y)
				self.wll.draw(tela)
				e = True
				d = False
			elif cont_d_ini.rect.x >= player.rect.x and lonor <= 100 and lony >= -40 and yonl >= -40:
				cont_d_ini.rect.x += -5
				self.wlr.update(cont_d_ini.rect.x,cont_d_ini.rect.y)
				self.wlr.draw(tela)
				clock.tick(5)
				d = True
				e = False 
			elif cont_d_ini.rect.x == player.rect.x:
				cont_d_ini.rect.x += 0
				
			for cont_dini in ini:
				for wal in mapas:
					if cont_dini.rect.colliderect(wal.rect):
						if e: # Moving right; Hit the left side of the wall
							cont_dini.rect.right = wal.rect.left
						if d: # Moving left; Hit the right side of the wall
							cont_dini.rect.left = wal.rect.right
							
				
				if cont_dini.rect.colliderect(player.rect):
					if e == True:
						self.atk.update(cont_d_ini.rect.x,cont_d_ini.rect.y)
						self.atk.draw(tela)
					if d == True:
						self.atkk.update(cont_d_ini.rect.x,cont_d_ini.rect.y)
						self.atkk.draw(tela)
						
			"""
						
	def cair(self):
		mdy = -5
		dy = 5
		for cont_dini in ini:
			cont_dini.rect.y +=dy
			for wal in mapas:
					if cont_dini.rect.colliderect(wal.rect):
						if dy > 0: # Moving down; Hit the top side of the wall
							cont_dini.rect.bottom = wal.rect.top
						#if mdy < 0: # Moving up; Hit the bottom side of the wall
							#cont_dini.rect.top = wal.rect.bottom
	def inic(self):
		for co in ini:
			co.rect.x = co.posafe[0]
			co.rect.y = co.posafe[1]
			co.anime = False
			player.rect.x = 80
			player.rect.y = 526


level = [
"WWWWWWWWWWWWWWWWWWWW",
"W                  W",
"W   I     I        W",
"W WWWWWWWWWWWWWWW  W",
"W W   I         W  W",
"W W   WWWWWWWW  W  W",
"W W   W      W  W  W",
"W W   W   I EW  W  W",
"W W   W   WWWW  W  W",
"W W   W         W  W",
"W W   WWWWWWWWWWW  W",
"W W                W",
"W WWWWWWWWWWWWWWWWWW",
"W                  W",
"WWWWWWWWWWWWWWWWWWWW",
]
x = y = 0
for row in level:
	for col in row:
		if col == "W":
			mapa((x, y))
		if col == "E":
			end_rect = pygame.Rect(x, y, 36, 40)
		if col =="I":
			Inimigo((x,y))
			
		x += 40
	y += 40
	x = 0
	


def other_1():
	fas = "2"
	
	for xia in range(0,30):
		for c in ini:
			ini.remove(c)
		for w in mapas:
			mapas.remove(w)
		

	level = [
"WWWWWWWWWWWWWWWWWWWW",
"W                  W",
"W       I      E   W",
"W   WWWWWWWWWWWWW  W",
"WI  W    I         W",
"WW  W   WWWWWWWWW  W",
"W   W   WWWWWWWWW  W",
"W   W   IWWWWWWWI  W",
"W  IW   WWWWWWWWW  W",
"W  WI   WWWWIWWWW  W",
"W   W   WWWWWWWWI  W",
"W   W   IWWWWWWWW  W",
"W   W   WWWWWWWWW  W",
"W       I          W",
"WWWWWWWWWWWWWWWWWWWW",
]
	x = y = 0
	for row in level:
		for col in row:
			if col == "W":
				mapa((x, y))
			if col == "E":
				end_rect.x = x
				end_rect.y = y
			if col =="I":
				Inimigo((x,y))
				
			x += 40
		y += 40
		x = 0	
		player.rect.x = 80
		player.rect.y = 526	
def other_2():
	fas = "3"
	
	for xia in range(0,30):
		for c in ini:
			ini.remove(c)
		for w in mapas:
			mapas.remove(w)
		
	
	
	level = [
"WWWWWWWWWWWWWWWWWWWW",
"W            I     W",
"W     I   WWWWWW   W",
"W   WWWW      IWI  W",
"W   W        WWWW  W",
"W WWW  WWWW I      W",
"W   W     W W  I   W",
"W   WI    W   WWW WW",
"W   WWW WWW   W W  W",
"WI    W   W I W W  W",
"WWW   W  IWWWWW W  W",
"W W      WW        W",
"W W   WWWW   WWW   W",
"W     W    E I W   W",
"WWWWWWWWWWWWWWWWWWWW",
]
	x = y = 0
	for row in level:
		for col in row:
			if col == "W":
				mapa((x, y))
			if col == "E":
				end_rect.x = x
				end_rect.y = y
			if col =="I":
				Inimigo((x,y))
				
			x += 40
		y += 40
		x = 0	
		player.rect.x = 80
		player.rect.y = 526					
	fas="3"
		




walk_rr = walk_right(player.rect.x,player.rect.y)
walk_r = pygame.sprite.Group(walk_rr)

walk_llv = walk_left_v(player.rect.x,player.rect.y)
walk_lv = pygame.sprite.Group(walk_llv)

paras = para(0,0)
parass = pygame.sprite.Group(paras)

walk_rrv = walk_right_v(player.rect.x,player.rect.y)
walk_rv = pygame.sprite.Group(walk_rrv)

walk_ll = walk_left(player.rect.x,player.rect.y)
walk_l = pygame.sprite.Group(walk_ll)

rodando = True
efect = "morrer"
white=(255,255,255)

saida = pygame.image.load("saida.png")
personagem = pygame.image.load("pa_1.png")
personagem2 = pygame.image.load("pa_1l.png")
personagem3 = pygame.image.load("pa_1vl.png")
personagem4 = pygame.image.load("pa_1v.png")


def main():
	
	pygame.init()
	"""
	rodando = True
	efect = "morrer"
	white=(255,255,255)
	 
	saida = pygame.image.load("saida.png")
	personagem = pygame.image.load("pa_1.png")
	personagem2 = pygame.image.load("pa_1l.png")
	personagem3 = pygame.image.load("pa_1vl.png")
	personagem4 = pygame.image.load("pa_1v.png")
	"""


	
	
	y_cair = 0
	gravitys= False
	
	cair = True
	v_cair=0
	gravity = 5
	
	andar=False
	mig = True
	
	esta_chao=True
	
	fas="1"
	
	while rodando:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				
				
				
		key = pygame.key.get_pressed()
		if key[pygame.K_w] and gravitys == False:
			esta_chao=False
			gravitys = True
			y_cair = -10
		if key[pygame.K_s]:
			esta_chao=True
			gravitys = False
		
		if gravitys:
			if (player.rect.y + y_cair) > 0:
				player.move(0,y_cair)
		
		
			
		if player.rect.colliderect(end_rect):
			"""
			for passos in range(0,100):
				parass.update(0,0)
				parass.draw(tela)
				pygame.display.flip()
			raise SystemExit ("You win!")
			"""
			if fas == "1":
				fas="2"
				other_1()
			elif fas == "2":
				fas="3"
				other_2()
			elif fas == "3":
				"""
				for passos in range(0,100):
					parass.update(0,0)
					parass.draw(tela)
					pygame.display.flip()
				"""
				raise SystemExit ("You win!")
		
		if cair:
			v_cair +=gravity
			
			for wals in mapas:
				if player.rect.y+v_cair > 0:
					player.move(0,v_cair)
					v_cair = 0
					
				else:
					
					v_cair = 0 
					
		tela.blit(fundo,(0,0))
		for chao in mapas:
			tela.blit(img,(chao.rect.x,chao.rect.y))
			
		for cont_ini in ini:
			
			#tela.blit(ini_img,(cont_ini.rect.x,cont_ini.rect.y))
			cont_ini.move()
			if cont_ini.d == True and cont_ini.e == False and cont_ini.anime == True:
				cont_ini.wlr.update(cont_ini.rect.x,cont_ini.rect.y)
				cont_ini.wlr.draw(tela)
			elif cont_ini.e == True and cont_ini.d == False and cont_ini.anime == True:
				cont_ini.wll.update(cont_ini.rect.x,cont_ini.rect.y)
				cont_ini.wll.draw(tela)
			#cont_ini.cair()
			if cont_ini.e == False and cont_ini.d == False:
				tela.blit(ini_img,(cont_ini.rect.x,cont_ini.rect.y))
			cont_ini.cair()
			
			
		tela.blit(saida,(end_rect.x,end_rect.y))	
		if andar==False and mig == False and esta_chao==True:
			tela.blit(personagem2,(player.rect))
		elif andar == False and mig == True and esta_chao == True:
			tela.blit(personagem,(player.rect))
		elif andar == False and mig == False and esta_chao == False:
			tela.blit(personagem3,(player.rect))
		elif andar == False and mig == True and esta_chao == False:
			tela.blit(personagem4,(player.rect))
		if key[pygame.K_d]:
			andar = True
			player.move(4, 0)
			if esta_chao:
				walk_r.update(player.rect.x,player.rect.y)
				walk_r.draw(tela)
			else:
				walk_rv.update(player.rect.x,player.rect.y)
				walk_rv.draw(tela)
			mig = True
			

		elif key[pygame.K_a]:
			andar=True
			player.move(-4, 0)
			if esta_chao:
				walk_l.update(player.rect.x,player.rect.y)
				walk_l.draw(tela)
			else:
				walk_lv.update(player.rect.x,player.rect.y)
				walk_lv.draw(tela)
			mig = False
		else:
			andar=False
		#pygame.draw.rect(tela,white,player.rect)
		
		pygame.display.flip()
		clock.tick(30)
		
		
				
main()
