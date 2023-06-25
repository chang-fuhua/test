# import cv2
#
# # 创建摄像头对象
# cap = cv2.VideoCapture(0)
#
# while True:
#     # 逐帧捕获视频流
#     ret, frame = cap.read()
#
#     # 显示当前帧
#     cv2.imshow('Video', frame)
#
#     # 按下 'q' 键退出循环
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # 释放摄像头资源
# cap.release()
# cv2.destroyAllWindows()

# import keyboard
# import threading
#
# # 按键状态字典，用于存储按键的状态（按下或释放）
# key_states = {}
#
# # 按键事件处理函数
# def on_key_event(event):
#     if event.event_type == 'down':
#         key_states[event.name] = True
#     elif event.event_type == 'up':
#         key_states[event.name] = False
#
# # 在单独的线程中监听键盘事件
# def keyboard_listener():
#     keyboard.on_press(on_key_event)
#     keyboard.on_release(on_key_event)
#     keyboard.wait()
#
# # 启动键盘监听线程
# keyboard_thread = threading.Thread(target=keyboard_listener)
# keyboard_thread.start()
#
# # 主循环
# while True:
#     # 检查按键状态
#     if key_states.get('r'):
#         print("按下了'r'键")
#     if key_states.get('q'):
#         print("按下了'q'键")
#         break
#
#     # 在这里继续执行其他的循环逻辑
#
# # 等待键盘监听线程结束
# keyboard_thread.join()

# import keyboard
#
# def on_key_release(event):
#     if event.name == 'r':
#         print("'r'键被释放")
#
#
# keyboard.on_release(on_key_release)
#
# # 保持监听，直到按下 'q' 键退出
# keyboard.wait('q')

# import keyboard
# import threading
#
# # 标识按键是否被按下的全局变量
# key_pressed = False
#
#
# def key_check():
#     global key_pressed
#
#     while True:
#         if keyboard.is_pressed('q'):
#             break
#
#         if keyboard.is_pressed('r'):
#             key_pressed = True
#             print("按下了'r'键")
#         elif keyboard.is_pressed('s'):
#             key_pressed = True
#             print("按下了's'键")
#         else:
#             key_pressed = False
#
#
# # 创建并启动按键检测的线程
# key_thread = threading.Thread(target=key_check)
# key_thread.start()
#
# # 主循环
# while True:
#     # 在主循环中检查按键是否被按下
#     if key_pressed:
#         # 执行按键触发的操作
#         # ...
#         # 重置按键状态
#         key_pressed = False
#
# key_thread.join()

# import keyboard
#
# def on_key_release(event):
#     if event.name == 'r':
#         print("'r'键被释放")
#
#
# keyboard.on_release(on_key_release)
#
# # 保持监听，直到按下 'q' 键退出
# keyboard.wait('q')

# import keyboard
# while True:
#     if keyboard.is_pressed('b'):
#         print('b Key was pressed')
#         break

# import keyboard
# import threading
#
# # 标识按键是否被按下的全局变量
# key_pressed = False
#
#
# def key_check():
#     global key_pressed
#
#     while True:
#         if keyboard.is_pressed('q'):
#             break
#
#         if keyboard.is_pressed('r'):
#             key_pressed = True
#             print("按下了'r'键")
#         elif keyboard.is_pressed('s'):
#             key_pressed = True
#             print("按下了's'键")
#         else:
#             key_pressed = False
#
#
# # 创建并启动按键检测的线程
# key_thread = threading.Thread(target=key_check)
# key_thread.start()
#
# # 主循环
# while True:
#     # 在主循环中检查按键是否被按下
#     if key_pressed:
#         # 执行按键触发的操作
#         # ...
#         # 重置按键状态
#         key_pressed = False


# import keyboard
# import threading
#
# def on_key_release(event):
#     if event.name == 'r':
#         print("'r'键被释放")
#     elif event.name == 't':
#         print("'t'键被释放")
#     elif event.name == 'y':
#         print("'y'键被释放")
#
# # 创建键盘监听线程
# keyboard_thread = threading.Thread(target=keyboard.on_release, args=(on_key_release,))
#
# # 启动键盘监听线程
# keyboard_thread.start()
#
# # 保持主线程运行，直到按下 'q' 键退出
# keyboard.wait('q')

import cv2
import threading
import keyboard

# 全局变量，用于存储最新的视频帧
latest_frame = None
record_key = False
def on_key_release(event):
    global record_key
    if event.name == 'r':
        record_key = True
        print("'r'键被释放")
    elif event.name == 't':
        print("'t'键被释放")
    elif event.name == 'y':
        print("'y'键被释放")

# 创建键盘监听线程
keyboard_thread = threading.Thread(target=keyboard.on_release, args=(on_key_release,))

# 启动键盘监听线程
keyboard_thread.start()

# 用于截取视频帧的线程函数
def capture_frames():
    global latest_frame
    global record_key

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # 存储最新的视频帧
        latest_frame = frame

        if record_key:
            cv2.imwrite('D:\\test\\captured_image.jpg', latest_frame)
            record_key = False

    cap.release()


# 用于显示最新视频帧的线程函数
def display_frames():
    global latest_frame

    while True:
        if latest_frame is not None:
            cv2.imshow('Video', latest_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


# 创建并启动截取视频帧的线程
capture_thread = threading.Thread(target=capture_frames)
capture_thread.start()

# 创建并启动显示视频帧的线程
display_thread = threading.Thread(target=display_frames)
display_thread.start()
