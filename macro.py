import pyautogui
import keyboard 
import time

print(pyautogui.size()) #현재 사용하는 모니터 해상도 출력

user_id = input('아이디 입력 : ') #input str
follower = input('구매수량 입력 : ') #input primary
repeat = int(input('반복횟수 입력 : ')) #input integer

print('PRESS ENTER!')

while True:
    if keyboard.is_pressed('enter'):
        i = 0 #Number of iterations
        start_time = time.perf_counter()
        while i < repeat:
            # 아이디 입력
            pyautogui.moveTo(426,655)
            pyautogui.click(426,655)
            pyautogui.typewrite(user_id, interval = 0)

            # 구매수량 입력
            pyautogui.moveTo(426,742)
            pyautogui.click(426,742)
            pyautogui.typewrite(follower, interval = 0)

            #input information
            pyautogui.moveTo(426,912)
            pyautogui.click(426,912)
            
            i += 1
            time.sleep(1.5) #1.5초 시간지연
            end_time = time.perf_counter()

            execution_time = end_time - start_time
            print('작업 수행 시간: {excution_time}초') #작업 시간 측정
        break #end