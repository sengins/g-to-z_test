import time
import random
from lore import LoreStream
from entities import Ada, Enemy
from assets import Hardware

class GameEngine:
    def __init__(self):
        self.player = Ada()
        self.cycle_count = 0

    def start(self):
        # 播放开场
        for line in LoreStream.GAME_INTRO:
            print(line)
            time.sleep(1)
        LoreStream.ada_think("boot")
        self.loop()

    def loop(self):
        while self.player.is_alive:
            self.cycle_count += 1
            print(f"\n=== [周期 Cycle-{self.cycle_count}] ===")
            
            # 1. 探索阶段
            bug = Enemy("铁锈噬虫", hp=30, atk=6)
            LoreStream.story(f"遭遇敌对生物: {bug.name} (HP: {bug.hp})")
            
            # 2. 战斗阶段
            self.battle(self.player, bug)
            
            # 3. 结算阶段
            if self.player.is_alive:
                self.post_battle()
                
            # 4. Zeabur 保护性休眠
            print("\n>>> [系统]: 周期结束，散热中 (10s)...")
            time.sleep(10)

    def battle(self, player, enemy):
        while player.is_alive and enemy.is_alive:
            # --- 玩家回合 ---
            player.charge() 
            if player.energy >= 3:
                card = player.deck[0] 
                player.energy -= card.cost
                effect, val = card.execute()
                
                if effect == 'attack':
                    enemy.take_damage(val)
                    LoreStream.ada_think("attack")
                elif effect == 'defend': # 这里简化了逻辑，实际上Card execute只返回数值
                     pass # 暂时没实现防御逻辑的 self buff，先略过
            
            if not enemy.is_alive: 
                LoreStream.ada_think("win")
                break
            time.sleep(1)
            
            # --- 敌人回合 ---
            enemy.act(player)
            if not player.is_alive:
                LoreStream.ada_think("hit")
            time.sleep(1)

    def post_battle(self):
        # 掉落逻辑
        if random.random() > 0.6:
            LoreStream.ada_think("hardware_found")
            junk = Hardware("损坏的激光头", "高危组件", power=10, risk=5)
            self.player.install_hardware(junk)
        else:
            self.player.fragments += 1
            LoreStream.log(f"回收碎片。当前碎片: {self.player.fragments}")
