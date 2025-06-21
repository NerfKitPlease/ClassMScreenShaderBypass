import os
import time

try:
    delay = float(input("Delay : "))
except ValueError:
    print("잘못된 입력입니다. 숫자를 입력해주세요.")
    exit(1)

target_process = "hscagent.exe"

while True:
    processes = os.popen('tasklist').read()

    if target_process in processes:
        print(f"{target_process} 감지 O - 종료 시도")
        result = os.system(f'taskkill /f /im {target_process} >nul 2>&1')
        
        if result == 0:
            print(f"{target_process} 종료 성공")
        else:
            print(f"{target_process} 종료 실패 - Code : {result}")
    else:
        print(f"{target_process} 감지 X")

    time.sleep(delay)
