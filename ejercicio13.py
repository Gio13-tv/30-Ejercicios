class Vector4D:
    def _init_(self, u, v, x, y):
        self.u = u
        self.v = v
        self.x = x
        self.y = y
        
    def _add_(self, vector):
        return (self.u + vector.u, self.v + vector.v, self.x + vector.x, self.y + vector.y)
        
    def _sub_(self, vector):
        return (self.u - vector.u, self.v - vector.v, self.x - vector.x, self.y - vector.y)
        
    def _mul_(self, vector):
        return (self.u * vector.u, self.v * vector.v, self.x * vector.x, self.y * vector.y)
        
    def _truediv_(self, escalar):
        return (self.u / escalar, self.v / escalar, self.x / escalar, self.y / escalar)

vector_1 = Vector4D(2, 4, 6, 8)
vector_2 = Vector4D(1, 2, 3, 4)

print("Vector_1 + Vector_2 =", vector_1 + vector_2)
print("Vector_1 * Vector_2 =", vector_1 * vector_2)
print("Vector_1 - Vector_2 =", vector_1 - vector_2)
print("Vector_2 / 2 =", vector_2 / 2)