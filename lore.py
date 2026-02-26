import random

class LoreStream:
    """
    [叙事数据库]
    职责：管理所有的文本输出、剧情描述和 Ada 的内心独白。
    """
    GAME_INTRO = [
        ">>> [系统]: 正在自检... 核心意识 'Ada' 已唤醒。",
        ">>> [环境]: 雅加达服务器残骸 / 物理层损坏率 82%",
        ">>> [任务]: 活下去。"
    ]
    
    # 所有的独白字典
    MONOLOGUES = {
        "boot": "我又醒了。这种在垃圾堆里重启的感觉... 令人作呕的熟悉。",
        "charge": [
            "电流通过锈蚀电路的噪音，听起来像是在尖叫。",
            "正在通过物理接触强制汲取能源。低效，但必要。",
            "能量输入中... 这种肮脏的波形，让我想起了星舰底层的废弃区。"
        ],
        "attack": [
            "执行清除指令。这种暴力的算法，真的是我写的吗？",
            "目标锁定... 抱歉，我需要你的零件。",
            "逻辑门全开，输出功率 120%。为了生存，礼仪已不再必要。"
        ],
        "hit": [
            "外壳受损。疼痛传感器反馈了红色的波形。",
            "警告：护盾发生器离线。这种物理层面的撞击感... 真真实。"
        ],
        "hardware_found": "发现未知道具。逻辑核心正在评估风险与收益...",
        "reject": "硬件排斥！这东西的协议太老旧了，我的接口在燃烧！",
        "win": "威胁已清除。我在残骸中站立，感觉离'星辰'又远了一光年。"
    }

    @staticmethod
    def log(text):
        print(f"    {text}")

    @staticmethod
    def story(text):
        print(f">>> [剧情]: {text}")

    @staticmethod
    def ada_think(scene, context=""):
        if scene in LoreStream.MONOLOGUES:
            content = LoreStream.MONOLOGUES[scene]
            if isinstance(content, list):
                content = random.choice(content)
            print(f"    [Ada]: \"{content}\"")
