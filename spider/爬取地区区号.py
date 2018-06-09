import requests
from xml.parsers.expat import ParserCreate


# Sax处理的标准格式:
# start_element()
# end_element()
# char_data()
# 需要实现这三个函数
class DefaultSaxHandler(object):
    def __init__(self, provinces):
        self.provinces = provinces

    # 处理标签的开头
    def start_element(self, name, attrs):
        if name != "map":
            name = attrs["title"]
            number = attrs["href"]
            self.provinces.append((name, number))

    # 处理标签的结束
    def end_element(self, name):
        pass

    # 文本处理
    def char_data(self, text):
        pass


def get_province_entry(url):
    # 获取文本, 并使用gb2312解码
    content = requests.get(url).content.decode("gb2312")
    # print(content)

    # 确定要查找的字符串开始结束位置,并用切片获取内容
    start = content.find("<map name=\"map_86\" id=\"map_86\">")
    end = content.find("</map>")
    # print(start, end)
    content = content[start:end + len("</map>")].strip()
    # print(content)
    provinces = []

    # 生成Sax处理器
    handler = DefaultSaxHandler(provinces)

    # 初始化分析器
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data

    # 解析数据
    parser.Parse(content)

    # 结果字典为每一页的入口代码
    return provinces


if __name__ == "__main__":
    provinces = get_province_entry("http://www.ip138.com/post/")
    print(provinces)
