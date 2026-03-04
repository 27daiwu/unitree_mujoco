import pygame
import sys

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    print("未检测到手柄")
    sys.exit()

print(f"检测到手柄，包含 {joystick.get_numaxes()} 轴, {joystick.get_numhats()} 十字键, {joystick.get_numbuttons()} 按键")
print("请操作手柄，将打印对应的 ID...")

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"按键按下 (Button ID): {event.button}")
        elif event.type == pygame.JOYAXISMOTION:
            if abs(event.value) > 0.2:
                print(f"摇杆移动 (Axis ID): {event.axis}, 当前值: {event.value:.2f}")
        elif event.type == pygame.JOYHATMOTION:
            print(f"十字键触发 (Hat ID): {event.hat}, 当前值: {event.value}")
            
    pygame.time.wait(50)