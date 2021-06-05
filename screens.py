import pygame
import cv2
import random
import time

from api import getApi, parseJson
from obj import Obj

class Game():
    def __init__(self):
        pygame.init()
        self.screen_size = [1280, 720]
        self.screen =  pygame.display.set_mode(self.screen_size)
        self.background = pygame.image.load('./resource/start_background.bmp')
        self.running = True 
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.screen_size[0])
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.screen_size[1])

        self.title = 'Emo Challenge'
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()

        self.black = (0, 0, 0)
        self.white = (255, 255 , 255)

        self.character = "emo"
        self.difficulty = "Normal"
        self.music = "Paradise"
        self.score = 0

        self.mysound = pygame.mixer.music.load(f'resource/{self.music}.wav')

class StartScreen(Game):
    def __init__(self):
        super(StartScreen, self).__init__()      
        self.start_button = pygame.image.load('./resource/start_button.png')
        self.character_button = pygame.image.load('./resource/character_button.bmp')
        self.difficulty_button = pygame.image.load('./resource/difficulty_button.bmp')
        self.music_button = pygame.image.load('./resource/music_button.bmp')
        self.character_selecter = pygame.image.load('./resource/character_selecter.bmp')
        self.difficulty_selecter = pygame.image.load('./resource/difficulty_selecter.bmp')
        self.music_selecter = pygame.image.load('./resource/music_selecter.bmp')
        self.c_button = False
        self.d_button = False
        self.m_button = False
        self.character = "emo"
        self.difficulty = "Normal"
        self.music = "Paradise"
    
    def run(self):
        
        EXIT = 0
        while not EXIT:
            self.clock.tick(60)
            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.start_button,(440,560))
            self.screen.blit(self.character_button,(440,300))
            self.screen.blit(self.difficulty_button,(440,370))
            self.screen.blit(self.music_button,(440,440))
            if self.c_button:
                self.screen.blit(self.character_selecter,(440,300))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        posx = event.pos[0]
                        posy = event.pos[1]
                        if posx>440:
                            if posx<880:
                                if posy>356.25:
                                    if posy<440.625:
                                        pygame.draw.rect(self.screen,(0,0,0),(440,880,365.25,440.625),2)
                                        self.character = "emo"
                                        self.c_button = False
                        if posx>440:
                            if posx<880:
                                if posy>440.625:
                                    if posy<525:
                                        character = "samchon"
                                        self.c_button = False
                        
            if self.d_button:
                self.screen.blit(self.difficulty_selecter,(440,300))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        posx = event.pos[0]
                        posy = event.pos[1]
                        if posx>440:
                            if posx<880:
                                if posy>356.25:
                                    if posy<418.5:
                                        self.difficulty = "Hard"
                                        self.d_button = False
                        if posx>440:
                            if posx<880:
                                if posy>418.5:
                                    if posy<474.75:
                                        self.difficulty = "Normal"
                                        self.d_button = False
                        if posx>440:
                            if posx<880:
                                if posy>474.75:
                                    if posy<531:
                                        self.difficulty = "easy"
                                        self.d_button = False
            if self.m_button:
                self.screen.blit(self.music_selecter,(440,300))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        posx = event.pos[0]
                        posy = event.pos[1]
                        if posx>440:
                            if posx<880:
                                if posy>356.25:
                                    if posy<418.5:
                                        self.music = "Paradise"
                                        self.m_button = False
                        if posx>440:
                            if posx<880:
                                if posy>418.5:
                                    if posy<474.75:
                                        self.music = "Party"
                                        self.m_button = False
                        if posx>440:
                            if posx<880:
                                if posy>474.75:
                                    if posy<531:
                                        self.music = "Palm"
                                        self.m_button = False
                
                
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    posx = event.pos[0]
                    posy = event.pos[1]
                    if posx>440:
                        if posx<840:
                            if posy>560:
                                if posy<651:
                                    EXIT = 1
                                    
                if event.type == pygame.MOUSEBUTTONUP:
                    posx= event.pos[0]
                    posy = event.pos[1]
                    if posx>440:
                        if posx<840:
                            if posy>300:
                                if posy<340:
                                    self.c_button = True
                    if posx>440:
                        if posx<840:
                            if posy>370:
                                if posy<410:
                                    self.d_button = True
                    if posx >440:
                        if posx<840:
                            if posy>440:
                                if posy<480:
                                    self.m_button = True
    
            font = pygame.font.Font('resource/NanumGothic.ttf', 20)
            # screen.blit(background,(0,0))
            pygame.display.flip()

        return self.character, self.difficulty, self.music

class MainScreen(Game):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.testing = 0

        self.value = 'None'
        self.confidence = 0

        self.Again = 0
        self.running = True 
        self.note_speed = 5
        self.note_size = (150, 150)
        self.note_dropfreq = 0.99
        self.line_y = self.screen_size[1] - 200
        self.note_list = []
        self.note_on_line = None

        # angry disgust fear laugh neutral sad surprise smile talking
        self.aunt_facials = {'smile':'resource/aunt_smile.png', 
                    'surprise':'resource/aunt_surprise.png',
                    'angry':'resource/aunt_angry.png',
                    'sad':'resource/aunt_sad.png',
                    'disgust':'resource/aunt_disgust.png'}
        self.uncle_facials = {'smile':'resource/uncle_smile.png', 
                    'surprise':'resource/uncle_surprise.png',
                    'angry':'resource/uncle_angry.png',
                    'sad':'resource/uncle_sad.png',
                    'disgust':'resource/uncle_disgust.png'}
        self.facial = self.aunt_facials

        self.mysound = pygame.mixer.music.load('resource/Paradise.wav')
    
    def run(self):
        pygame.mixer.music.play(-1)
        if self.character == 'uncle':
            self.facials = self.uncle_facials
        else:
            self.facials = self.aunt_facials

        score_to_fever = 3
        scene_score = 0
        EXIT = 0
        while not EXIT:
            self.clock.tick(60)

            # BackGround 설정 (카메라)
            ret, frame = self.camera.read()

            back_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            back_frame = back_frame.swapaxes(0, 1)
            back_frame = cv2.flip(back_frame, 0)
            pygame.surfarray.blit_array(self.screen, back_frame)
            #pygame.display.update()

            #   4-2. 입력 감지
            # 키보드나 마우스의 동작을 가져옴. 동시에 누를 수 있으므로. 리스트로 받음.
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    EXIT = 'finish'
                    pygame.mixer.music.stop()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.score += 1  
                        scene_score += 1
                    if event.key == pygame.K_DOWN:
                        try: ## 땜빵
                            offset = 70
                            rec_x1 = self.note_on_line.x - offset
                            rec_y1 = self.note_on_line.y - offset
                            rec_x2 = self.note_on_line.x + self.note_on_line.sx + offset
                            rec_y2 = self.note_on_line.y + self.note_on_line.sy + offset

                            if rec_x1 < 0:
                                rec_x1 = 0
                            if rec_x2 > self.screen_size[0]:
                                rec_x2 = self.screen_size[0]
                            if rec_y1 < 0:
                                rec_y1 = 0
                            if rec_y2 > self.screen_size[1]:
                                rec_y2 = self.screen_size[1]

                            snap = cv2.flip(frame, 1)
                            # print(snap.shape)
                            snap = snap[rec_y1:rec_y2, rec_x1:rec_x2]
                            cv2.imwrite('webcam_snap.jpg', snap)
                            response = getApi(img_path='webcam_snap.jpg')
                            self.value, self.confidence = parseJson(response)
                            if self.value == self.note_on_line.face:
                                self.score += 1
                                scene_score += 1
                        except Exception as ex:
                            print(f'{ex}')
                        # 얼굴이 없을 경우 터지는 문제...
                        # snapshot이 안찍히는거 --> rect의 범위
            if self.testing == 0 and \
                self.note_on_line is not None and \
                self.note_on_line.y + self.note_on_line.sy//2 + 20 > self.line_y and self.note_on_line.shot == 0:
                try: ## 땜빵
                    offset = 70
                    rec_x1 = self.note_on_line.x - offset
                    rec_y1 = self.note_on_line.y - offset
                    rec_x2 = self.note_on_line.x + self.note_on_line.sx + offset
                    rec_y2 = self.note_on_line.y + self.note_on_line.sy + offset
                    if rec_x1 < 0:
                        rec_x1 = 0
                    if rec_x2 > self.screen_size[0]:
                        rec_x2 = self.screen_size[0]
                    if rec_y1 < 0:
                        rec_y1 = 0
                    if rec_y2 > self.screen_size[1]:
                        rec_y2 = self.screen_size[1]
                    snap = cv2.flip(frame, 1)
                    # print(snap.shape)
                    snap = snap[rec_y1:rec_y2, rec_x1:rec_x2]
                    cv2.imwrite('webcam_snap.jpg', snap)
                    response = getApi(img_path='webcam_snap.jpg')
                    self.value, self.confidence = parseJson(response)
                    if self.value == self.note_on_line.face:
                        self.score += 1
                        scene_score += 1
                except Exception as ex:
                    print(f'{ex}')
                self.note_on_line.shot = 1

            if scene_score >= score_to_fever:
                self.running = False
                EXIT = 'enter_fever'                

            #   4-3. 입력과 시간에 따른 변화
            # create notes
            if random.random() >= self.note_dropfreq:
                if len(self.note_list) == 0:
                    fkey = random.choice(list(self.facials.keys()))
                    note = Obj(addr=self.facials[fkey])
                    note.change_size(self.note_size)
                    note.x = random.randrange(0, self.screen_size[0] - note.sx - round(note.sx/2))
                    note.y = 10
                    note.speed = self.note_speed
                    self.note_list.append(note)
                elif (self.note_list[-1].y > self.note_list[-1].sy):  # 코드 중복 수정 요
                    fkey = random.choice(list(self.facials.keys()))
                    note = Obj(addr=self.facials[fkey])
                    note.change_size(self.note_size)
                    note.x = random.randrange(0, self.screen_size[0] - note.sx - round(note.sx/2))
                    note.y = 10
                    note.speed = self.note_speed
                    self.note_list.append(note)

            note_del_list = []
            for i, note in enumerate(self.note_list):
                note.y += note.speed
                if note.y >= self.screen_size[1]:
                    note_del_list.append(i)
                if note.y + note.sy >= self.line_y and note.y < self.line_y:
                    self.note_on_line = note

            for idx in note_del_list:
                del self.note_list[idx]

            # Draw
            pygame.draw.line(self.screen, 'red', (0, self.line_y), (self.screen_size[0], self.line_y), 10)

            font = pygame.font.Font('resource/NanumGothic.ttf', 40)
            text_score = font.render('Score: {}'.format(self.score), True, (255, 255, 0))
            self.screen.blit(text_score, (self.screen_size[0] - 200, 5))

            # text_facial = font.render('Facial: {} {:0.2f}'.format(self.value, self.confidence), True, (255, 255, 0))
            text_facial = font.render('Facial: {}'.format(self.value), True, (255, 255, 0))
            self.screen.blit(text_facial, (round(self.screen_size[0]/2-300), round(self.screen_size[1]-60)))

            for note in self.note_list:
                note.show(self.screen)

            pygame.display.flip()

        return EXIT

class FeverScreen(Game):
    def __init__(self):
        super(FeverScreen, self).__init__()
        self.testing = 0

        self.running = False
        self.score = 0
        self.value = 'None'
        self.confidence = 0
        self.note_speed = 8
        self.note_size = (150, 150)
        self.note_dropfreq = 0.99
        self.line_y = self.screen_size[1] - 200
        self.note_list = []
        self.note_on_line = None

        # angry disgust fear laugh neutral sad surprise smile talking
        self.aunt_facials = {'smile':'resource/aunt_smile.png', 
                    'surprise':'resource/aunt_surprise.png',
                    'angry':'resource/aunt_angry.png',
                    'sad':'resource/aunt_sad.png',
                    'disgust':'resource/aunt_disgust.png'}
        self.uncle_facials = {'smile':'resource/uncle_smile.png', 
                    'surprise':'resource/uncle_surprise.png',
                    'angry':'resource/uncle_angry.png',
                    'sad':'resource/uncle_sad.png',
                    'disgust':'resource/uncle_disgust.png'}
        self.facial = self.aunt_facials

        self.mysound = pygame.mixer.music.load('resource/music_fever.wav')

    def run(self):
        pygame.mixer.music.play(-1)
        if self.character == 'uncle':
            self.facials = self.uncle_facials
        else:
            self.facials = self.aunt_facials

        fever_timelimit = 20
        start_time = time.time()
        EXIT = 0
        while not EXIT:
            self.clock.tick(60)
            #pygame.draw.rect(self.screen,(255,0,0),(0,0,1280,720),50)
            #pygame.display.flip()
           # BackGround 설정 (카메라)
            ret, frame = self.camera.read()

            back_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            back_frame = back_frame.swapaxes(0, 1)
            back_frame = cv2.flip(back_frame, 0)
            pygame.surfarray.blit_array(self.screen, back_frame)
            

            #   4-2. 입력 감지
            # 키보드나 마우스의 동작을 가져옴. 동시에 누를 수 있으므로. 리스트로 받음.
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    self.running = 1
                    EXIT = 'finish'
                    pygame.mixer.music.stop()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.score += 2
                    if event.key == pygame.K_DOWN:
                        try: ## 땜빵
                            offset = 70
                            rec_x1 = self.note_on_line.x - offset
                            rec_y1 = self.note_on_line.y - offset
                            rec_x2 = self.note_on_line.x + self.note_on_line.sx + offset
                            rec_y2 = self.note_on_line.y + self.note_on_line.sy + offset

                            if rec_x1 < 0:
                                rec_x1 = 0
                            if rec_x2 > self.screen_size[0]:
                                rec_x2 = self.screen_size[0]
                            if rec_y1 < 0:
                                rec_y1 = 0
                            if rec_y2 > self.screen_size[1]:
                                rec_y2 = self.screen_size[1]

                            snap = cv2.flip(frame, 1)
                            # print(snap.shape)
                            snap = snap[rec_y1:rec_y2, rec_x1:rec_x2]
                            cv2.imwrite('webcam_snap.jpg', snap)
                            response = getApi(img_path='webcam_snap.jpg')
                            self.value, self.confidence = parseJson(response)
                            if self.value == self.note_on_line.face:
                                self.score += 2
                        except Exception as ex:
                            print(f'{ex}')
                        # 얼굴이 없을 경우 터지는 문제...
                        # snapshot이 안찍히는거 --> rect의 범위

            # need fix
            if self.testing == 0 and \
                self.note_on_line is not None and \
                self.note_on_line.y + self.note_on_line.sy//2 + 20 > self.line_y and self.note_on_line.shot == 0:
                try: ## 땜빵
                    offset = 70
                    rec_x1 = self.note_on_line.x - offset
                    rec_y1 = self.note_on_line.y - offset
                    rec_x2 = self.note_on_line.x + self.note_on_line.sx + offset
                    rec_y2 = self.note_on_line.y + self.note_on_line.sy + offset
                    if rec_x1 < 0:
                        rec_x1 = 0
                    if rec_x2 > self.screen_size[0]:
                        rec_x2 = self.screen_size[0]
                    if rec_y1 < 0:
                        rec_y1 = 0
                    if rec_y2 > self.screen_size[1]:
                        rec_y2 = self.screen_size[1]
                    
                    snap = cv2.flip(frame, 1)
                    # print(snap.shape)
                    snap = snap[rec_y1:rec_y2, rec_x1:rec_x2]
                    cv2.imwrite('webcam_snap.jpg', snap)
                    response = getApi(img_path='webcam_snap.jpg')
                    self.value, self.confidence = parseJson(response)
                    if self.value == self.note_on_line.face:
                        self.score += 2
                except Exception as ex:
                    print(f'{ex}')
                self.note_on_line.shot = 1
                # 얼굴이 없을 경우 터지는 문제...
                # snapshot이 안찍히는거 --> rect의 범위


            curr_time = time.time()
            if curr_time - start_time >= fever_timelimit:
                EXIT = 'fever_out'

            #   4-3. 입력과 시간에 따른 변화
            # create notes
            if random.random() >= self.note_dropfreq:
                if len(self.note_list) == 0:
                    fkey = random.choice(list(self.facials.keys()))
                    note = Obj(addr=self.facials[fkey])
                    note.change_size(self.note_size)
                    note.x = random.randrange(0, self.screen_size[0] - note.sx - round(note.sx/2))
                    note.y = 10
                    note.speed = self.note_speed
                    self.note_list.append(note)
                elif (self.note_list[-1].y > self.note_list[-1].sy):  # 코드 중복 수정 요
                    fkey = random.choice(list(self.facials.keys()))
                    note = Obj(addr=self.facials[fkey])
                    note.change_size(self.note_size)
                    note.x = random.randrange(0, self.screen_size[0] - note.sx - round(note.sx/2))
                    note.y = 10
                    note.speed = self.note_speed
                    self.note_list.append(note)

            note_del_list = []
            for i, note in enumerate(self.note_list):
                note.y += note.speed
                if note.y >= self.screen_size[1]:
                    note_del_list.append(i)
                if note.y + note.sy >= self.line_y and note.y < self.line_y:
                    self.note_on_line = note

            for idx in note_del_list:
                del self.note_list[idx]

            # Draw
            pygame.draw.line(self.screen, 'red', (0, self.line_y), (self.screen_size[0], self.line_y), 10)

            font = pygame.font.Font('resource/NanumGothic.ttf', 30)
            big_font = pygame.font.Font('resource/NanumGothic.ttf', 50)
            text_score = font.render('SCORE: {}'.format(self.score), True, (255, 255, 0))
            self.screen.blit(text_score, (self.screen_size[0] - 200, 1))
            
            text_timeout = big_font.render('TIME LEFT: {}'.format(fever_timelimit - int(curr_time-start_time)), True, (255, 255, 0))
            self.screen.blit(text_timeout, (self.screen_size[0]//2 - 200, 50))

            # text_facial = font.render('Facial: {} {:0.2f}'.format(self.value, self.confidence), True, (255, 255, 0))
            text_facial = font.render('Facial: {}'.format(self.value), True, (255, 255, 0))
            self.screen.blit(text_facial, (round(self.screen_size[0]/2-300), round(self.screen_size[1]-65)))

            text_fever = font.render('{}'.format('FEVER MODE'), True, (255,0,0))
            self.screen.blit(text_fever,(self.screen_size[0] - 800, 1))

            text_fever1 = font.render('{}'.format('FEVER MODE'), True, (255,0,0))
            self.screen.blit(text_fever1,(self.screen_size[0] - 500, 1))

            text_fever2 = font.render('{}'.format('FEVER MODE'), True, (255,0,0))
            self.screen.blit(text_fever2,(self.screen_size[0] - 1100, 1))

            text_fever3 = font.render('{}'.format('FEVER MODE'), True, (255,0,0))
            self.screen.blit(text_fever3,(round(self.screen_size[0] - 500), round(self.screen_size[1]-35)))

            text_fever4 = font.render('{}'.format('FEVER MODE'), True, (255,0,0))
            self.screen.blit(text_fever4,(round(self.screen_size[0] - 800), round(self.screen_size[1]-35)))

            text_fever5 = font.render('{}'.format('FEVER MODE'), True, (255,0,0))
            self.screen.blit(text_fever5,(round(self.screen_size[0] - 1100), round(self.screen_size[1]-35)))

            #pygame.draw.rect(self.screen,(255,0,0),(0,0,1280,720),50)
            #pygame.display.flip()

            for note in self.note_list:
                note.show(self.screen)

            pygame.display.flip()
        return EXIT

class MiniChamScreen(Game):
    '''
    data = response.json()
    print(data['result']['faces'][0]['pitch'])
    print(data['result']['faces'][0]['yaw'])

    0 deg = 0 rad
    30 deg = 0.52 rad
    45 deg = 0.78 rad
    60 deg = 1.04 rad
    90 deg = 1.57 rad

    left is positive
    '''
    def __init__(self):
        super(MiniChamScreen, self).__init__()
        self.hand = Obj('resource/hand.png')
        self.hand.origin_x = self.hand.x = self.screen_size[0] // 2 - (self.hand.origin_sx // 2)
        self.hand.origin_y = self.hand.y = self.screen_size[1] - self.hand.sy
        
        self.origin_pos = (self.hand.origin_sx//2, self.hand.origin_sy)
        self.pos = (self.hand.origin_x + self.hand.origin_sx//2, 
                    self.hand.origin_y + self.hand.origin_sy)

        self.hand_direction_list = ['left', 'right', 'front']
        self.hand_direction = 'left'
        # Rect(left, top, width, height)
        self.snap_box = pygame.Rect(self.screen_size[0]//2 - 160,
                                    self.screen_size[1]//2 - 200,
                                    160*2,
                                    300)
        self.yaw = 0
        self.pitch = 0

        self.mysound = pygame.mixer.music.load('resource/Paradise.wav')
    
    def run(self):
        pygame.mixer.music.play(-1)
        start_time = time.time()
        round_time = 0
        curr_time = 0

        chances = 3
        hit, miss = 0, 0
        round_init = 0
        hand_change = 0
        shot = 0
        EXIT = 0
        while not EXIT:
            self.clock.tick(60)

            # BackGround 설정 (카메라)
            ret, frame = self.camera.read()

            back_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            back_frame = back_frame.swapaxes(0, 1)
            back_frame = cv2.flip(back_frame, 0)
            pygame.surfarray.blit_array(self.screen, back_frame)

            #   4-2. 입력 감지
            # 키보드나 마우스의 동작을 가져옴. 동시에 누를 수 있으므로. 리스트로 받음.
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    EXIT = 'finish'
                    pygame.mixer.music.stop()
                
                # for testing
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        hit += 1
                    if event.key == pygame.K_LEFT:
                        # self.hand_direction = random.choice(self.hand_direction_list)
                        self.hand_direction = 'left'
                        if self.hand_direction == 'left':
                            self.hand.angle += 60
                            self.hand.rotate(self.pos, self.origin_pos, self.hand.angle)
                    elif event.key == pygame.K_RIGHT:
                        # self.hand_direction = random.choice(self.hand_direction_list)
                        self.hand_direction = 'right'
                        if self.hand_direction == 'right':
                            self.hand.angle -= 60
                            self.hand.rotate(self.pos, self.origin_pos, self.hand.angle)
                    
                    if event.key == pygame.K_DOWN:
                        try: ## 땜빵
                            rec_x1 = self.snap_box.left
                            rec_y1 = self.snap_box.top
                            rec_x2 = rec_x1 + self.snap_box.width
                            rec_y2 = rec_y1 + self.snap_box.height

                            snap = cv2.flip(frame, 1)
                            # print(snap.shape)

                            snap = snap[rec_y1:rec_y2, rec_x1:rec_x2]
                            cv2.imwrite('webcam_snap.jpg', snap)
                            response = getApi(img_path='webcam_snap.jpg', api='kakao')
                            self.yaw, self.pitch = parseJson(response, target='face_direction')
                            if self.hand_direction == 'left':
                                if self.yaw >= 0.5:
                                    hit += 1
                                else:
                                    miss += 1
                            elif self.hand_direction == 'right':
                                if self.yaw <= -0.5:
                                    hit += 1
                                else:
                                    miss += 1
                            elif self.hand_direction == 'front':
                                if self.yaw > -0.5 and self.yaw < 0.5:
                                    hit += 1
                                else:
                                    miss += 1
                        except Exception as ex:
                            print(f'{ex}')
                            pass
                        # 얼굴이 없을 경우 터지는 문제...
                        # snapshot이 안찍히는거 --> rect의 범위

            if round_init == 1:
                round_time = time.time()
                round_init = 0

            if curr_time - round_time > 3 and hand_change == 0:
                self.hand_direction = random.choice(self.hand_direction_list)
                if self.hand_direction == 'left':
                    self.hand.angle = 60
                elif self.hand_direction == 'right':
                    self.hand.angle = -60
                elif self.hand_direction == 'front':
                    self.hand.angle = 0
                self.hand.rotate(self.pos, self.origin_pos, self.hand.angle)
                hand_change = 1

            if curr_time - round_time > 3.3 and shot == 0:
                try: ## 땜빵
                    rec_x1 = self.snap_box.left
                    rec_y1 = self.snap_box.top
                    rec_x2 = rec_x1 + self.snap_box.width
                    rec_y2 = rec_y1 + self.snap_box.height
                    snap = cv2.flip(frame, 1)
                    # print(snap.shape
                    snap = snap[rec_y1:rec_y2, rec_x1:rec_x2]
                    cv2.imwrite('webcam_snap.jpg', snap)
                    response = getApi(img_path='webcam_snap.jpg', api='kakao')
                    self.yaw, self.pitch = parseJson(response, target='face_direction')
                    if self.hand_direction == 'left':
                        if self.yaw >= 0.5:
                            hit += 1
                        else:
                            miss += 1
                    elif self.hand_direction == 'right':
                        if self.yaw <= -0.5:
                            hit += 1
                        else:
                            miss += 1
                    elif self.hand_direction == 'front':
                        if self.yaw > -0.3 and self.yaw < 0.3:
                            hit += 1
                        else:
                            miss += 1
                except Exception as ex:
                    print(f'{ex}')
                    miss += 1
                    pass
                shot = 1

            if hit >= 2:
                EXIT = 'enter_fever'
            if miss >= 2:
                EXIT = 'go_back'

            if curr_time - round_time > 6:
                round_init = 1
                hand_change = 0
                shot = 0
                self.hand.angle = 0
                self.hand.rotate(self.pos, self.origin_pos, self.hand.angle)

            # Draw
            pygame.draw.rect(self.screen, (255, 0, 0), self.snap_box, width=5)
            self.hand.show(self.screen)

            font = pygame.font.Font('resource/NanumGothic.ttf', 40)
            big_font = pygame.font.Font('resource/NanumGothic.ttf', 250)
            text_score = font.render('Hit-Miss ({} Chances): {}-{}'.format(chances, hit, miss), True, (255, 255, 0))
            text_cham = font.render('Cham Cham Cham', True, (255, 0, 0))
        
            self.screen.blit(text_score, (self.screen_size[0] - 600, 5))
            self.screen.blit(text_cham, (self.screen_size[0]//2 - 175, self.screen_size[1]//2 - 260))

            curr_time = time.time()
            if curr_time - start_time <= 3:
                text_ready = big_font.render('Ready~', True, (255, 255, 0))
                self.screen.blit(text_ready, (self.screen_size[0]//2 - 380, self.screen_size[1]//2 - 200))
                round_init = 1
            elif curr_time - round_time <= 3:
                text_counter = big_font.render(f'{3 - int(curr_time - round_time)}', True, (255, 255, 0))
                self.screen.blit(text_counter, (self.screen_size[0]//2 - 80, self.screen_size[1]//2 - 180))


            # text_facial = font.render('Facial: {} {:0.2f}'.format(self.value, self.confidence), True, (255, 255, 0))
            # self.screen.blit(text_facial, (round(self.screen_size[0]/2-300), round(self.screen_size[1]-60)))

            pygame.display.flip()
        
        return EXIT

class EndScreen(Game):
    def __init__(self):
        super(EndScreen, self).__init__()
        self.game_over = pygame.image.load('./resource/game_over.bmp')
        
    def run(self):

        EXIT = 0
        while not EXIT:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    EXIT = 'finish'
    
            font = pygame.font.Font('resource/NanumGothic.ttf', 40)
            text1 = font.render(f"Score : {self.score}", True, (255,255,255))
            #text2 = font.render(, True, (255,255,255))
            self.screen.blit(self.game_over,(0,0))
            self.screen.blit(text1,(500,280))
            #self.screnn.blit(text2,(700,280))
            
            pygame.display.flip()
            pygame.mixer.music.stop()

        pygame.quit()