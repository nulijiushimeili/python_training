import time


# 登录
def login():
    account = input("请输入你的账号:")
    password = input("请输入密码:")
    if account == "xiaoming" and password == "123456":
        print("登录成功,欢迎再次回来!")
    else:
        print("账号或密码错误!")


# 退出
def logout():
    print("正在退出登录...")
    time.sleep(1)
    print("您已退出登录,欢迎下次回来!")


# 修改密码
def modify_pwd():
    new_pwd1 = input("请输入您的新密码:")
    new_pwd2 = input("请输入您的新密码:")
    print("密码修改成功,请牢记!")


# prompt提示
def prompt():
    print("欢迎进入身份认证系统")
    print("请输入序号,进入你需要进行的操作")
    print("1.登录")
    print("2.退出")
    print("3.认证")
    print("4.修改密码")


# 主函数入口
if __name__ == "__main__":
    prompt()
    choose_num = int(input("请输入你要进行的操作的编号:"))
    if choose_num == 1:
        login()
    elif choose_num == 2:
        logout()
    elif choose_num == 3:
        pass
    elif choose_num == 4:
        modify_pwd()
