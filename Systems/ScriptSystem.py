'''
这是一个脚本系统，负责管理游戏中的脚本组件。脚本组件可以附加到游戏对象上，实现各种自定义行为和逻辑。
脚本系统会在每一帧更新时调用脚本组件的update方法，从而实现游戏逻辑的更新。

脚本系统还可以用于统计游戏中的信息，例如分数、时间等。通过在脚本组件中编写相应的逻辑，可以实现各种游戏机制和功能。
'''

import pygame

from Component.component import Component

class ScriptSystem:
    def __init__(self,game,screen):
        self.game = game
        self.screen = screen
        self.scripts = [] # 存储所有脚本组件的列表
		

    def addScript(self, script):
        self.scripts.append(script)
    
    def removeScript(self, script):
        if script in self.scripts:
            self.scripts.remove(script)

    def update(self, time):
        for script in self.scripts:
            script.update(time)