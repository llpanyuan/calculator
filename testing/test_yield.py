# 生成器
def provider():
    for i in range(5):
        print("before")
        yield i
        print("after")
p = provider()
print(next(p))
print(next(p))