import pygame



        
class RenderSystem:
        def __init__(self,game,screen):
            self.game = game
            self.screen = screen
            self.renders = []
            ###

        def addRenderer(self,renderer):
            self.renders.append(renderer)

        def draw(self):
            for r in self.renders:
                if not r.visible:
                    continue
                
                pos = r.gameObject.pos
                
                if r.name == 'AnimationRenderer':
                    if r.animation is not None:
                    
                        ###sp#黑喵:
                        #第一步，获取动画当前的图片
                        #第二步 得到这个图片的大小信息（长方形）
                        #第三步 设置这个长方形中心点在r的位置
                        #第四步 画到屏幕上
                        sp = r.animation.get_sprite(self.game.time // 1000)
                        rect = sp.get_rect()
                        rect.center = (pos[0], pos[1])
                        self.screen.blit(sp, rect)

                elif r.name == "CircleRenderer":
                    pygame.draw.circle(self.screen, (255, 255, 255), pos, r.radius)

                elif r.name == "RectangleRenderer":
                    pygame.draw.rect(self.screen, r.color , (pos[0], pos[1], r.width, r.height))
                    
                elif r.name == 'TextRenderer':
                    print(r.font)
                    text = r.font.render(r.text, True, r.fontColor, (0,0,0))
                    #获得显示对象的rect区域坐标
                    textRect = text.get_rect()
                    # 设置显示对象居中
                    textRect.bottomleft = (pos[0], pos[1])
                    # 将准备好的文本信息，绘制到主屏幕 Screen 上。
                    self.screen.blit(text, textRect)





                        

 

