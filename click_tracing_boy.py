from pico2d import *

back_hight = 1280
back_width = 1024
open_canvas(back_hight, back_width)

back = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

# 클릭 좌표
x1, y1 = back_hight // 2, back_width // 2
points = [x1, y1]
hide_cursor()

moving = True
frame = 0

# 클릭 좌표 저장
def handle_events():
    global moving

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            moving = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            points[0], points[1] = event.x, back_hight - 250 - event.y

# 클릭한 곳에 손 그리기
while moving:
    handle_events()
    x2, y2 = points[0], points[1]

    # 소년 이동
    for i in range (0, 100 + 1, 5):
        t = i / 100
        x = (1-t)*x1 + t*x2
        y = (1-t)*y1 + t*y2
        back.draw_now(back_hight // 2, back_width // 2)
        
        # 소년이 도착하지 않았다면 손을 계속 그리기
        if(x1 != x2):
            hand.draw_now(x2, y2)
        
        # 소년 애니메이션
        character.clip_draw(frame * 100, 0, 100, 100, x, y) 
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
    
    # 소년 도착
    x1, y1 = x2, y2