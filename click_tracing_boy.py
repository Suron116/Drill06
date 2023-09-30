from pico2d import *

back_hight = 1280
back_width = 1024
open_canvas(back_hight, back_width)

back = load_image('TUK_GROUND.png')
left = load_image('left.png')
right= load_image('right.png')
hand = load_image('hand_arrow.png')

x1, y1 = back_hight // 2, back_width // 2
points = [0, 0]
moving = True
hide_cursor()

back.draw_now(640, 512)

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
    #back.draw_now(640, 512)
    handle_events()
    x2, y2 = points[0], points[1]
    hand.draw_now(x2, y2)
    delay(0.05)
    update_canvas()