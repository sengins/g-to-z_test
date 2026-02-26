import random
from lore import LoreStream
from assets import Card, Hardware

class Unit:
    def __init__(self, name, hp, max_energy):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.shield = 0
        self.energy = 0
        self.max_energy = max_energy
        self.is_alive = True

    def take_damage(self, dmg):
        if self.shield >= dmg:
            self.shield -= dmg
            LoreStream.log(f"{self.name} 的护盾吸收了所有伤害。")
        else:
            real_dmg = dmg - self.shield
            self.shield = 0
            self.hp -= real_dmg
            LoreStream.log(f"{self.name} 护盾破碎！承受 {real_dmg} 点伤害 (HP: {self.hp})")
        
        if self.hp <= 0:
            self.is_alive = False

class Ada(Unit):
    def __init__(self):
        super().__init__("Ada", hp=50, max_energy=12)
        # 初始卡组
        self.deck = [
            Card("电弧打击", 3, 'attack', 8),
            Card("纳米涂层", 2, 'defend', 6)
        ]
        self.hardware_slot = [] 
        self.fragments = 0      

    def charge(self):
        gain = random.randint(2, 4)
        self.energy = min(self.max_energy, self.energy + gain)
        LoreStream.log(f"充能完成 (+{gain})。当前能量: {self.energy}")
        LoreStream.ada_think("charge")

    def install_hardware(self, item: Hardware):
        LoreStream.story(f"尝试安装 [{item.name}]...")
        LoreStream.log(item.description)
        
        if item.risk > 0:
            LoreStream.ada_think("reject")
            self.take_damage(item.risk)
            LoreStream.log(f"安装失败！接口过载造成 {item.risk} 点反噬伤害。")
        else:
            self.hardware_slot.append(item)
            LoreStream.log("安装成功。系统效能提升。")

class Enemy(Unit):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, max_energy=5)
        self.base_atk = atk

    def act(self, target):
        self.energy += 2
        if self.energy >= 3:
            LoreStream.log(f"[{self.name}] 发出嘶嘶声，扑向了 Ada！")
            target.take_damage(self.base_atk)
            self.energy -= 3
        else:
            LoreStream.log(f"[{self.name}] 正在啃食周围的金属以补充能量。")
