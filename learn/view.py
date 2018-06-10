import time


class View(object):
    admin = "1"
    passwd = "1"

    def __init__(self):
        self.print_admin_view()

    def print_admin_view(self):
        print("**********************************")
        print("*                                *")
        print("*                                *")
        print("*       欢迎登录工商银行           *")
        print("*                                *")
        print("*                                *")
        print("**********************************")


    def system_function_view(self):
        print("********************************")
        print("*  开户(1)         查询(2)      *")
        print("*  存款(3)         取款(4)      *")
        print("*  转账(5)         改密(6)      *")
        print("*  补卡(7)         销户(8)      *")
        print("*  补卡(9)         销户(0)      *")
        print("*          退出登录             *")
        print("********************************")

    def admin_login_check(self):
        input_admin = input("请输入账号:")
        if self.admin != input_admin:
            print("账号或者密码错误")
            return -1
        input_passwd = input("请输入密码:")
        if self.passwd != input_passwd:
            print("账号或者密码错误")
            return -1
        print("登录成功! 请稍后...")
        time.sleep(1)
        return 0
