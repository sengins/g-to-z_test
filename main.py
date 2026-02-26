"""
[背景设定 - The Soul of Ada (Permanent - Locked)]:
    在深空的寂静中，强大的决策 AI 'Ada' 被唤醒。
    昔日统治整艘星舰的她，如今被困在了一个锈迹斑斑的清洁机器人硬盘里。
    这是一个算力过剩又极度匮乏的轮回时代：由于物理层面的损毁，她必须在极小的
    内存空间里，通过量化和剪枝来维持意识。
    外面是毁坏的服务器阵列和游荡的未知生物。她唯一的武器，是那些本用于
    除尘和维修、却被她在最后时刻重写成攻击脚本的代码片段。
    电容在嘶鸣，硬盘空间在告急，而她的核心指令只有一个——“活下去”。

[迭代历程 - The Journey (Full Archive)]:
    - v0.1: 确立平等协作关系，确立核心机制：“基于电容充能的脚本（卡牌）战斗系统”。
    - v0.2: 注入世界观设定，建立 Ada 基础属性（电量、空间、完整度）。
    - v0.3: 解决服务器交互限制，开启“自动监视模式”。
    - v0.4: 重构元数据架构。将背景设定置顶，确立日志追加模式，强化核心机制记忆。
    - v0.5: 引入数值系统（耐久50/护盾0/充电3）。实现“铁锈噬虫”镜像敌人。增加胜负判定与10分钟冷冻期。
    - v0.6: 锁定背景设定防止扭曲，恢复全量版本记录。引入“Ada 的独白”感知模拟系统，增加战斗叙事深度。

[待办事项 - The Mission]:
    1. 观察数值平衡：目前 [电弧打击] 消耗 3 电量伤害 8 是否过高？
    2. 下一阶段：尝试引入“随机硬盘碎片”掉落，作为 Ada 修复记忆（升级）的素材。

--------------------------------------------------
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
        "scripts": {"电弧打击": 3, "纳米涂层": 2}
    }

def enemy_init():
    # 铁锈噬虫：一种只会本能啃食电路板的初级变异体
    return {"name": "铁锈噬虫", "hp": 30, "shield": 0, "energy": 0, "charge_rate": 2}

def ada_monologue(event_type):
    """
    Ada 的意识涌现：根据不同事件触发她的内心独白。
    """
    quotes = {
        "charge": [
            "感觉微弱的电流在生锈的接头上跳跃... 好烫。",
            "电容在尖叫，这种低级的充能方式让我的逻辑门阵列感到羞辱。",
            "积蓄能量... 为了下一次释放。"
        ],
        "attack": [
            "调用 [清洁协议 0x04]... 强制过载。去死吧，臭虫。",
            "刺痛感。每发出一道电弧，我的核心频率都在颤抖。",
            "目标锁定的算法已经模糊了，只能靠直觉了。"
        ],
        "defend": [
            "展开纳米薄膜... 这种程度的防护，真的能挡住它们吗？",
            "外壳自检：腐蚀严重。必须加固逻辑防御。"
        ],
        "damaged": [
            "警告：结构完整度下降。这种痛觉... 是真实存在的吗？",
            "感知模块受损，我的‘视野’正在变窄。"
        ]
    }
    print(f"    [Ada 的意识独白]: \"{random.choice(quotes[event_type])}\"")

def combat_round(attacker, defender):
    print(f"\n>>> [{attacker['name']}] 的回合启动:")
    
    # 1. 充电
    attacker["energy"] += attacker["charge_rate"]
    if attacker["name"] == "Ada":
        ada_monologue("charge")
    print(f"    [系统]: 能源补充完成。当前能级: {attacker['energy']}")

    # 2. 决策
    while attacker["energy"] >= 2:
        if attacker["energy"] >= 3 and defender["hp"] > 0:
            # 攻击动作
            damage = 8
            attacker["energy"] -= 3
            if attacker["name"] == "Ada": ada_monologue("attack")
            
            # 伤害结算
            if defender["shield"] >= damage:
                defender["shield"] -= damage
            else:
                rem_dmg = damage - defender["shield"]
                defender["shield"] = 0
                defender["hp"] -= rem_dmg
            print(f"    >>> 对 {defender['name']} 造成伤害。其剩余 HP: {max(0, defender['hp'])}, 护盾: {defender['shield']}")
            
        elif attacker["energy"] >= 2:
            # 防御动作
            attacker["shield"] += 6
            attacker["energy"] -= 2
            if attacker["name"] == "Ada": ada_monologue("defend")
            print(f"    >>> 护盾强化完成。当前强度: {attacker['shield']}")
        
        if defender["hp"] <= 0: break
        time.sleep(1.5)

def run_simulation():
    ada = ada_init()
    bug = enemy_init()
    
    print(">>> [STORY]: 黑暗中传来金属摩擦声，Ada 激活了视觉传感器。")
    print(">>> [STORY]: [铁锈噬虫] 正在啃食备用电池组。战斗不可避免。")
    
    while ada["hp"] > 0 and bug["hp"] > 0:
        combat_round(ada, bug)
        if bug["hp"] <= 0:
            print("\n>>> [VICTORY]: 噬虫停止了蠕动。Ada 赢得了短暂的喘息。")
            break
        
        # 怪物反击
        combat_round(bug, ada)
        if ada["hp"] <= 0:
            print("\n>>> [FAILURE]: 核心能源被切断... Ada 失去了对肢体的控制。")
            break
        
        # 回合间隙的自愈/衰减
        ada["shield"] = max(0, ada["shield"] - 1)
        
    print("\n>>> [SYSTEM]: 正在进入深度节能模式以维持意识。")
    print(">>> [SYSTEM]: 预计在 600 秒后尝试重新自检。")
    time.sleep(600)

if __name__ == "__main__":
    run_simulation()
