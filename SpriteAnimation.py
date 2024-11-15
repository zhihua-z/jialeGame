import pygame

# 动画类
class AnimatedSprite:
    def __init__(
        self, 
        sprite, 
        start_x, 
        start_y, 
        num_of_frames, 
        frame_width, 
        frame_height, 
        animation_name
        ):
        
        self.sprite = sprite
        
        # 动画贴图列表
        self.frames = []
        
        self.start_x = start_x
        self.start_y = start_y
        self.num_of_frames = num_of_frames
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.animation_name = animation_name
        
        self.fps = 4
        
        # 动画时间
        self.animation_time = 0
        # 当前在第0帧
        self.current_frame = 0
        
        self.load_frame()
        
    def load_frame(self):
        # 数帧数
        frame_count = 0
        
        # 
        
        while frame_count < self.num_of_frames:
            frame_x = self.start_x + frame_count * self.frame_width
            frame_y = self.start_y
            
            
            frame = self.sprite.subsurface(pygame.Rect(
                frame_x,
                frame_y,
                self.frame_width,
                self.frame_height
            ))
            self.frames.append(frame)
            frame_count += 1
        
    
    def get_sprite(self, time):
        # 获取当前帧率下一帧所需要的时间
        frame_shijian = 1 / self.fps * 1000 # 毫秒
        
        # 获取到当前时间和动画时间的值
        time_difference = time - self.animation_time
        
        # 如果超过了一帧的时间，就让帧数+1
        if time_difference >= frame_shijian:
            self.current_frame = (self.current_frame + 1) % self.num_of_frames
            # 更新当前动画时间
            self.animation_time = time
        
        return self.frames[self.current_frame]
    #*****