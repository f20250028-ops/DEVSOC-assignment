import pygame, sys, random

def ball_animation():
	global ball_speed_x, ball_speed_y , player_score, opponent_score
	
	ball.x += ball_speed_x

	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		pygame.mixer.Sound.play(pong_sound)
		ball_speed_y *= -1

    
	# Player Score
	if ball.left <= 0: 
		pygame.mixer.Sound.play(score_sound)
		ball_start()
		player_score += 1

	# Opponent Score
	if ball.right >= screen_width:
		pygame.mixer.Sound.play(score_sound)	
		ball_start()
		opponent_score += 1

	if ball.left <= 0 or ball.right >= screen_width:
		ball_start()

	if ball.colliderect(player) or ball.colliderect(opponent):
		pygame.mixer.Sound.play(pong_sound)
		ball_speed_x *= -1

def player_animation():
	player.y += player_speed

	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height

def opponent_ai():
	if opponent.top < ball.y:
		opponent.y += opponent_speed
	if opponent.bottom > ball.y:
		opponent.y -= opponent_speed

	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height

def ball_start():
	global ball_speed_x, ball_speed_y

	ball.center = (screen_width/2, screen_height/2)
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()


screen_width = 1500
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')


pure_blue = (0,255,255)
pure_green = (0,255,0)
light_red = (255,0,0)
black = (0,0,0)
bg_color = pygame.Color('grey12')


ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)


ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf' , 32)


pong_sound = pygame.mixer.Sound("pongsound.ogg")
score_sound = pygame.mixer.Sound("scoresound.ogg")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player_speed -= 6
			if event.key == pygame.K_DOWN:
				player_speed += 6
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player_speed += 6
			if event.key == pygame.K_DOWN:
				player_speed -= 6
	
	
	ball_animation()
	player_animation()
	opponent_ai()

	
	screen.fill(bg_color)
	pygame.draw.rect(screen, pure_blue, player)
	pygame.draw.rect(screen, light_red, opponent)
	pygame.draw.ellipse(screen, pure_green, ball)
	pygame.draw.aaline(screen, black, (screen_width / 2, 0),(screen_width / 2, screen_height))

	player_text = basic_font.render(f'{player_score}',False,pure_blue)
	screen.blit(player_text,(770,400))

	opponent_text = basic_font.render(f'{opponent_score}',False,light_red)
	screen.blit(opponent_text,(710,400))

	pygame.display.flip()
	clock.tick(120)	