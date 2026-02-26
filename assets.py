from lore import LoreStream

class Card:
    """[卡牌基类]"""
    def __init__(self, name, cost, effect_type, value):
        self.name = name
        self.cost = cost
        self.type = effect_type # 'attack' or 'defend'
        self.value = value

    def execute(self):
        LoreStream.log(f"执行协议 [{self.name}] (能耗: {self.cost})")
        # 返回 (效果类型, 数值)
        return (self.type, self.value)

class Hardware:
    """[装备基类]"""
    def __init__(self, name, desc, power=0, risk=0):
        self.name = name
        self.description = desc
        self.power = power   # 提供的额外数值
        self.risk = risk     # 装备时的自伤风险
