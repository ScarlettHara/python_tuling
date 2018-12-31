class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性 name age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        """模拟小狗被命令是打滚"""
        print(self.name.title() + ' rolled over!')


if __name__ == "__main__":
    '创建实例'
    hashiqi = Dog("yy", 2)

    '访问属性'
    print(hashiqi.name, hashiqi.age)
    '调用方法'
    hashiqi.roll_over()
    hashiqi.sit()

    your_dog = Dog("lucy", 3)
    print("\n"+your_dog.name,your_dog.age)
    your_dog.roll_over()
    your_dog.sit()

