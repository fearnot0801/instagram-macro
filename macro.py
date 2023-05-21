import pyautogui
import keyboard 
import time

print(pyautogui.size()) #현재 사용하는 모니터 해상도 출력

x_coordiante_id = 459
x_coordiante_follower = 825
x_coordiante_submit = 477

y_coordiante_id = 639
y_coordiante_follower = 634
y_coordiante_submit = 847

while True:
    if keyboard.is_pressed('shift') and keyboard.is_pressed('1'):
        position = pyautogui.position()
        x_coordiante_id = position[0]
        y_coordiante_id = position[1]
        print('id-position = ' , '(' , x_coordiante_id ,',', y_coordiante_id , ')')
        time.sleep(0.2)
    
    if keyboard.is_pressed('shift') and keyboard.is_pressed('2'):
        position = pyautogui.position()
        x_coordiante_follower = position[0]
        y_coordiante_follower = position[1]
        print('follower-position = ' , '(' , x_coordiante_follower ,',', y_coordiante_follower , ')')
        time.sleep(0.2)

    if keyboard.is_pressed('shift') and keyboard.is_pressed('3'):
        position = pyautogui.position()
        x_coordiante_submit = position[0]
        y_coordiante_submit = position[1]
        print('submit-position = ' , '(' , x_coordiante_submit ,',', y_coordiante_submit , ')')
        time.sleep(0.2)

    #input information
    if keyboard.is_pressed('shift') and keyboard.is_pressed('enter'):
        user_id = input('아이디 입력 : ')
        follower = input('구매수량 입력 : ')
        repeat = int(input('반복횟수 입력 : ')) #input integer
        type = int(input('외국인 팔로워(1 또는 0) :'))
        time.sleep(1)

        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)

        i = 0
        while i < repeat:
            start_time = time.perf_counter()

            if type == 1:
                pyautogui.click(495,519)
                time.sleep(0.1)
                pyautogui.click(494,834)
                time.sleep(0.1)
                
            # input id
            pyautogui.moveTo(x_coordiante_id, y_coordiante_id)
            pyautogui.click(x_coordiante_id, y_coordiante_id)
            pyautogui.typewrite(user_id, interval = 0)

            # input follower
            pyautogui.moveTo(x_coordiante_follower, y_coordiante_follower)
            pyautogui.click(x_coordiante_follower, y_coordiante_follower)
            pyautogui.typewrite(follower, interval = 0)

            #submit button click
            pyautogui.moveTo(x_coordiante_submit, y_coordiante_submit)
            pyautogui.click(x_coordiante_submit, y_coordiante_submit)
            
            i += 1
            end_time = time.perf_counter()

            execution_time = end_time - start_time
            print('작업 수행 시간 :', execution_time, '초') #작업 시간 측정
            time.sleep(5) #5초 시간지연
        break