import time
def tim():
    for i in range(5):
        second = i % 60
        # minute = int(timer / 60) % 60
        time.sleep(1)
        print(f"{second:02} seconds remain")
    print("Times up!!")
