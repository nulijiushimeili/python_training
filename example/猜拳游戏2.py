# 猜拳游戏升级版
import random


# 将结果转换为容易读懂的形势
def change_res_can_read(num):
    if num == 0:
        return "剪刀"
    elif num == 1:
        return "石头"
    else:
        return "布"


while True:
    player = input("石头(0),剪刀(1),布(2)")
    player_num = int(player)
    computer = random.randint(0, 2)

    if player_num == computer:
        print("computer:{} VS player:{} ---- 平局"
              .format(change_res_can_read(computer), change_res_can_read(player_num)))
    elif (player_num == 0) and (computer == 2) \
            or (player_num == 1) and (computer == 0) \
            or (player_num == 2) and (computer == 1):
        print("computer:{} VS player:{} ---- 大获全胜"
              .format(change_res_can_read(computer), change_res_can_read(player_num)))
    else:
        print("computer:{} VS player:{} ---- 输了"
              .format(change_res_can_read(computer), change_res_can_read(player_num)))
