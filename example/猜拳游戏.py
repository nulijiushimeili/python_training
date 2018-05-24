import random


# 猜拳游戏

# 将猜拳结果显示为人可读的
def get_can_read_res(num):
    if num == 0:
        return "剪刀"
    elif num == 1:
        return "石头"
    else:
        return "布"


def game(player_num):
    computer = random.randint(0, 2)
    if player_num == computer:
        print("computer:{} VS player:{} ---- 平局".format(get_can_read_res(computer),
                                                        get_can_read_res(player_num)))
    # 这是一段有bug的代码
    # else:
    #     if player_num == 0 or computer == 0:
    #         if player_num == 0:
    #             print("computer:{} VS player:{} ---- 很遗憾你输了".format(get_can_read_res(computer),
    #                                                                 get_can_read_res(player_num)))
    #         else:
    #             print("computer:{} VS player:{} ---- 恭喜你,获胜".format(get_can_read_res(computer),
    #                                                                 get_can_read_res(player_num)))
    #     else:
    #         if player_num > computer:
    #             print("computer:{} VS player:{} ---- 恭喜你,获胜".format(get_can_read_res(computer),
    #                                                                 get_can_read_res(player_num)))
    #         else:
    #             print("computer:{} VS player:{} ---- 很遗憾你输了".format(get_can_read_res(computer),
    #                                                                 get_can_read_res(player_num)))
    elif 0 <= player_num < 3:
        if player_num == 0:
            if computer == 1:
                print("computer:{} VS player:{} ---- 很遗憾你输了"
                      .format(get_can_read_res(computer), get_can_read_res(player_num)))
            else:
                print("computer:{} VS player:{} ---- 恭喜你,获胜"
                      .format(get_can_read_res(computer), get_can_read_res(player_num)))
        elif player_num == 1:
            if computer == 2:
                print("computer:{} VS player:{} ---- 很遗憾你输了"
                      .format(get_can_read_res(computer), get_can_read_res(player_num)))
            else:
                print("computer:{} VS player:{} ---- 恭喜你,获胜"
                      .format(get_can_read_res(computer), get_can_read_res(player_num)))

        else:
            if computer == 0:
                print("computer:{} VS player:{} ---- 很遗憾你输了"
                      .format(get_can_read_res(computer), get_can_read_res(player_num)))
            else:
                print("computer:{} VS player:{} ---- 恭喜你,获胜"
                      .format(get_can_read_res(computer), get_can_read_res(player_num)))
    else:
        print("你这是什么手势,不要耍赖哦")


while True:
    print("开始游戏,退出请输入quit")
    player_guess = input("剪刀(0),石头(1),布(2)")
    if player_guess == "quit":
        break
    player_num = int(player_guess)
    game(player_num)
