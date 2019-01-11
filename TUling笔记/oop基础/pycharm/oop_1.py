class Person:
    name = "yy"
    __age = 18              # 私有变量


person = Person()

print(Person.name)
print(Person.__dict__)      # 查看__age
print(person._Person__age)  # 变成_Person__age    可以用_classname_attributename访问


