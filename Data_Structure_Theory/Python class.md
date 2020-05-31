# 파이썬 클래스

 - 파이썬 method는 항상 첫 번째 파라미터로 self 사용
    - 인자가 필요없을 때에도 self는 사용
 - 클래스의 attribute는 내부에서 접근시, self.attribute명 으로 접근

```python
class Square():
    height = 0
    width = 0

    def set_attr(self, height, width):
        self.height = height
        self.width = width

    def get_attr(self):
        print('height : ', self.height)
        print('width : ', self.width)

test = Square()

test.set_attr(10,20)
test.get_attr()


print('------생성자-----')
# 클래스 생성자
# __init__ (self)

class Quadrangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

square = Quadrangle(10,20,'red')
print('width : ', square.width, ' height: ', square.height, ' color: ', square.color)

# 클래스 소멸자
# __del__(self)

print('-----소멸자-------')
class Quardangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def __del__(self):
        print('Quardangle object is deleted')

s = Quardangle(1,1,'aa')
print(s)
del s
print(s)
```