class A:
    # 私有属性
    __attr = "attribute"

    def print_a(self):
        print("aaaaaaaaaaaa")

    def set_attr(self, attr):
        self.__attr = attr

    def get_attr(self):
        return self.__attr


class B:
    def print_b(self):
        print("bbbbbbbbbbbbb")


class C(A, B):
    def print_c(self):
        print("ccccccccccccc")

    # 重写父类的方法
    def print_a(self):
        print("aaaaaaa---cccccccccc")


c = C()
c.print_a()
c.print_b()
c.print_c()
c.set_attr("new attr")
print(c.get_attr())


# ------------多态-------------------------
class D(C):
    def print_c(self):
        print("dddddddddddd")


class F(C):
    def print_c(self):
        print("ffffffffffff")


def func(o):
    return o.print_c()


d = D()
f = F()
func(d)
func(f)
