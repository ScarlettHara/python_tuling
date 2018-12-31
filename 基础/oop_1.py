"""
定义一个学生类，用来形容学生
"""


class PythonStudent:
    # 用python给不确定的之赋值
    name = None
    age = 18
    course = "python"

    # 需要注意
    # 1 def doHomework的缩进层级
    # 2 系统默认有一个self参数
    def homework(self):
        print("我正在写作业")

        return None

# 实例化一个脚yueyue的学生，使用具体的人



yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)

yueyue.homework()
print(yueyue.__dict__)
print(PythonStudent.__dict__)
