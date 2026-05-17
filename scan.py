import cv2

def scan_cameras(max_tested=10):
    print("开始扫描连接的摄像头设备...\n")
    available_cameras = []
    
    for i in range(max_tested):
        # 尝试静默打开摄像头
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW) # 使用 DirectShow 加快速度并减少警告
        if cap.isOpened():
            # 尝试读取一帧来确认是否真的有画面
            ret, _ = cap.read()
            if ret:
                print(f"✅ 发现可用摄像头：索引号 {i}")
                available_cameras.append(i)
            else:
                print(f"⚠️ 索引号 {i} 可打开，但无法读取画面 (可能是虚拟摄像头或被占用)")
            cap.release()
        else:
            print(f"❌ 索引号 {i} 无法打开")

    print("\n--- 扫描结果 ---")
    if available_cameras:
        print(f"当前可用的摄像头索引为: {available_cameras}")
        print("请逐个尝试将 app.py 中的 CAMERA_INDEX 替换为上述数字。")
    else:
        print("没有找到任何可用的摄像头！请检查 USB 连接或系统权限。")

if __name__ == "__main__":
    scan_cameras()