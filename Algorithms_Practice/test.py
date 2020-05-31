class Quardangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def __del__(self):
        print('Quardangle object is deleted')

s = Quardangle(1,1,'aa')
print(s.width)
del s
print(s)