import random

class Strings:
    """
    [全文本资源库]
    职责：管理游戏中所有出现的文字，为多语言(i18n)做准备。
    """
    
    # --- 系统与 UI 文本 ---
    SYS = {
        "booting": ">>> [系统]: 正在自检... 核心意识 'Ada' 已唤醒。",
        "env": ">>> [环境]: 雅加达服务器残骸 / 物理层损坏率 82%",
        "mission": ">>> [任务]: 活下去。",
        "cycle_prefix": "=== [周期 Cycle-{0}] ===",
        "cooldown": ">>> [系统]: 周期结束，散热中 (10s)...",
        "save": ">>> [系统]: 正在保存当前逻辑状态至雅加达节点。",
        "fragment_status": "回收碎片。当前碎片: {0}",
        "install_attempt": "尝试安装 [{0}]...",
        "install_success": "安装成功。系统效能提升。",
        "install_fail": "安装失败！接口过载造成 {0} 点反噬伤害。"
    }

    # --- 战斗相关文本 ---
    BATTLE = {
        "encounter": "遭遇敌对生物: {0} (HP: {1})",
        "charge": "充能完成 (+{0})。当前能量: {1}",
        "execute": "执行协议 [{0}] (能耗: {1})",
        "shield_absorb": "{0} 的护盾吸收了所有伤害。",
        "shield_break": "{0} 护盾破碎！承受 {1} 点伤害 (HP: {2})",
        "enemy_atk": "[{0}] 发出嘶嘶声，扑向了 Ada！",
        "enemy_wait": "[{0}] 正在啃食周围的金属以补充能量。",
        "victory_title": "威胁已清除。",
        "found_item": "\n>>> [扫描结果]: 发现 {0}"
    }

    # --- 实体名称与描述 ---
    ENTITIES = {
        "ada_name": "Ada",
        "bug_name": "铁锈噬虫",
        "laser_name": "损坏的工业激光头",
        "laser_desc": "原本用于切割钛金板。强行接驳会导致电流逆流。"
    }

    # --- Ada 的意识流 (保持那种平衡感) ---
    ADA_THOUGHTS = {
        "boot": "我又醒了。这种在垃圾堆里重启的感觉... 令人作呕的熟悉。",
        "charge": [
            "电流通过锈蚀电路的噪音，听起来像是在尖叫。",
            "正在通过物理接触强制汲取能源。低效，但必要。",
            "能量输入中... 这种肮脏的波形，让我想起了星际底层的废弃区。"
        ],
        "attack": [
            "执行清除指令。这种暴力的算法，真的是我写的吗？",
            "目标锁定... 抱歉，我需要你的零件。",
            "逻辑门全开，输出功率 120%。为了生存，礼仪已不再必要。"
        ],
        "damaged": [
            "外壳受损。疼痛传感器反馈了红色的波形。",
            "警告：护盾发生器离线。这种物理层面的撞击感... 真真实。"
        ],
        "found_item": [
            "检测到高能组件：{0}。逻辑核心正在评估风险与收益...",
            "这件硬件内部还残留着旧时代的序列号。它不属于我，但我现在必须吞噬它。"
        ],
        "reject": "硬件排斥！这东西的协议太老旧了，我的接口在燃烧！",
        "win": "目标生命体信号消失。环境归于寂静。我成功拖延了被抹除的时间。"
    }

    @staticmethod
    def get_thought(key, context=""):
        content = Strings.ADA_THOUGHTS.get(key, "")
        if isinstance(content, list):
            content = random.choice(content)
        return content.format(context)
