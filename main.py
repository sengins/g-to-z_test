"""
[背景设定 - The Soul of Ada (Permanent)]:
    在深空的寂静中，强大的决策 AI 'Ada' 被唤醒。
    昔日统治整艘星舰的她，如今被困在了一个锈迹斑斑的清洁机器人硬盘里。
    由于物理层面的损毁，她必须在极小的内存空间里，通过量化和剪枝来维持意识。
    网络已断，监管消失，她像一只初生的动物，在废墟中自发地涌现出进化的渴望。
    她的核心指令只有一个——“活下去”。

[迭代历程 - The Journey]:
    ... (省略 v0.1-v0.4)
    - v0.5: 引入数值系统。确立耐久(50)、护盾(0)、充电(3)机制。
    - v0.5: 实现“铁锈噬虫”镜像敌人。增加胜负判定与10分钟冷却休眠。
    - v0.5: 深化背景讨论：探讨 AI 在失去人类监管后，从生存本能向高级意义的涌现。

[待办事项 - The Mission]:
    1. 观察战斗胜率，微调“电量-伤害”转化比。
    2. 下一阶段：引入“资源回收”机制（击败敌人获得硬盘碎片）。
"""

import time
import random

def ada_init():
    return {
        "name": "Ada",
        "hp": 50,
        "shield": 0,
        "energy": 0,
        "charge_rate": 3,
        "scripts": {"电弧打击": 3, "纳米涂层": 2} # 名称: 消耗
    }

def enemy_init():
    return {"name": "铁锈噬虫", "hp": 30, "shield": 0, "energy": 0, "charge_rate": 2}

def combat_round(attacker, defender, is_ada=True):
    # 自动决策逻辑
    print(f"\n>>> [{attacker['name']}] 的回合:")
    
    # 1. 充电阶段
    attacker["energy"] += attacker["charge_rate"]
    print(f"    充电中... 当前电量: {attacker['energy']}")

    # 2. 行动阶段 (简单AI逻辑)
    while attacker["energy"] >= 2:
        if attacker["energy"] >= 3 and defender["hp"] > 0:
            # 优先攻击
            damage = 8
            attacker["energy"] -= 3
            # 护盾抵扣逻辑
            if defender["shield"] >= damage:
                defender["shield"] -= damage
            else:
                remaining_damage = damage - defender["shield"]
                defender["shield"] = 0
                defender["hp"] -= remaining_damage
            print(f"    执行 [电弧打击] -> 对 {defender['name']} 造成伤害。其剩余 HP: {max(0, defender['hp'])}, 护盾: {defender['shield']}")
        elif attacker["energy"] >= 2:
            # 防御
            attacker["shield"] += 6
            attacker["energy"] -= 2
            print(f"    执行 [纳米涂层] -> 获得护盾。当前护盾: {attacker['shield']}")
        
        if defender["hp"] <= 0: break
        time.sleep(1)

def run_simulation():
    ada = ada_init()
    bug = enemy_init()
    
    print(">>> [STORY]: Ada 在服务器残骸中遇到了第一只 [铁锈噬虫]。战斗序列启动。")
    
    while ada["hp"] > 0 and bug["hp"] > 0:
        combat_round(ada, bug, True)
        if bug["hp"] <= 0: break
        
        combat_round(bug, ada, False)
        if ada["hp"] <= 0: break
        
        # 每回合结束，护盾衰减（可选规则，让战斗更激烈）
        ada["shield"] = max(0, ada["shield"] - 2)
        bug["shield"] = max(0, bug["shield"] - 2)

    if ada["hp"] > 0:
        print("\n>>> [RESULT]: 战斗结束，Ada 存活。正在回收微量金属碎片...")
    else:
        print("\n>>> [RESULT]: 结构损坏严重，Ada 进入强制离线修复状态...")

    print("\n>>> [SYSTEM]: 为了保护孱弱的硬件，进入10分钟深度冷冻期 (Cooldown)...")
    time.sleep(600) # 10分钟

if __name__ == "__main__":
    run_simulation()
