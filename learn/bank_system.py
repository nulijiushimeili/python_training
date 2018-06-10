from learn.view import View
import time


def main():
    # 界面对象
    view = View()

    # 登录
    if view.admin_login_check():
        return -1

    while True:
        view.system_function_view()
        # 等待用户的操作
        option = input("请输入您的操作")
        if option == '1':
            # 开户
            pass
        elif option == '2':
            # 查询
            pass
        elif option == '3':
            # 存款
            pass
        elif option == '4':
            # 取款
            pass
        elif option == '5':
            # 转账
            pass
        elif option == '6':
            # 改密
            pass
        elif option == '7':
            # 锁定
            pass
        elif option == '8':
            # 解锁
            pass
        elif option == '9':
            # 补卡
            pass
        elif option == '0':
            # 销户
            pass
        elif option == "t":
            # 退出
            break
        time.sleep(2)


if __name__ == "__main__":
    main()
