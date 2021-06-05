import pygame

class Obj:
    def __init__(self, addr):
        self.x, self.y = 0, 0
        self.origin_x, self.origin_y = 0, 0
        self.speed = 0
        self.put_img(addr)
        self.face = addr.split('.')[0].split('/')[-1].split('_')[-1]  # 고치기...
        self.angle = 0
        self.shot = 0

    def put_img(self, addr):
        if addr[-3:] == 'png':
            self.img = pygame.image.load(addr).convert_alpha()
        else:
            self.img = pygame.image.load(addr)
        self.sx, self.sy = self.img.get_size()
        self.origin_sx, self.origin_sy = self.img.get_size()
        self.origin_img = self.img.copy()

    def change_size(self, size):
        self.img = pygame.transform.scale(self.img, size)
        self.sx, self.sy = self.img.get_size()
        self.origin_sx, self.origin_sy = self.origin_img.get_size()

    def rotate(self, pos, originPos, angle):
        # source: https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame/54714144#54714144
        # calcaulate the axis aligned bounding box of the rotated image
        w, h       = self.origin_img.get_size()
        box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

        # calculate the translation of the pivot 
        pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
        pivot_rotate = pivot.rotate(angle)
        pivot_move   = pivot_rotate - pivot

        # calculate the upper left origin of the rotated image
        origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

        # get a rotated image
        self.img = pygame.transform.rotate(self.origin_img, angle)
        self.x, self.y = origin
        self.sx, self.sy = self.img.get_size()

    def show(self, screen):
        screen.blit(self.img, (self.x, self.y))