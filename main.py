import time

def run_task():
    print("--- 自动化 Debug 实验：修复版启动 ---")
    
    # 修复之前的 10 / 0 错误
    print("正在尝试计算关键数据...")
    result = 10 / 2 
    print(f"计算成功！结果是: {result}")
    
    print("进入持续运行模式，防止服务重启...")
    # 添加死循环，每 10 秒打印一次状态
    while True:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 系统运行中 - 状态正常")
        time.sleep(10)

if __name__ == "__main__":
    try:
        run_task()
    except Exception as e:
        # 即使发生意外错误，也会捕获并打印，方便我们在侧边栏继续 Debug
        print(f"检测到未预期崩溃！错误类型: {type(e).__name__}")
        print(f"详细错误信息: {str(e)}")
        # 保持容器存活，方便查看日志
        time.sleep(60)
