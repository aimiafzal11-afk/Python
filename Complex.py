class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show(self):
        if self.img >= 0:
            print(self.real, "i +", self.img, "j")
        else:
            print(self.real, "i", self.img, "j")
 
    def __add__(self, obj):
        new_real = self.real + obj.real
        new_img = self.img + obj.img
        return Complex(new_real, new_img)

    def __sub__(self, obj):
            new_real = self.real - obj.real
            new_img = self.img - obj.img
            return Complex(new_real, new_img)

c1 = Complex(3, 6)
c1.show()
c2 = Complex(7, 9)
c2.show()
add = c1 + c2
add.show()
sub = c1 - c2
sub.show()