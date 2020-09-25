import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """初始化道宽并设置其初始的位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载道宽的位置
        self.image = pygame.image.load('images/daokuan.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每个新的道宽放到屏幕的底部中心
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在道宽的属性center中存储小数点
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整道宽的位置"""
        # 更新center值 而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制道宽  根据self.rect指定的位置将图像绘制在屏幕上"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让道宽在屏幕上居中"""
        self.center = self.screen_rect.centerx