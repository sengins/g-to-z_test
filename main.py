import time

def run_task():
    print("--- 自动化 Debug 实验启动 ---")
    time.sleep(2) # 模拟处理时间
    print("正在尝试计算关键数据...")
    
    # 故意制造错误
    result = 10 / 0 
    print(f"结果是: {result}")

if __name__ == "__main__":
    try:
        run_task()
    except Exception as e:
        # 将错误打印到日志，这样我才能在侧边栏帮你分析
        print(f"检测到程序崩溃！错误类型: {type(e).__name__}")
        print(f"详细错误信息: {str(e)}")
        # 为了防止服务不断重启，我们可以让它在这里睡一会儿
        time.sleep(60)
