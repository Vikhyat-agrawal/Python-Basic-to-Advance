# Override the __len__() method on vector of problem 5 to display the dimension of the vector.
class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension to add.")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for dot product.")
        result = sum(a * b for a, b in zip(self.components, other.components))
        return result

    def __len__(self):
        return len(self.components)

    def __repr__(self):
        return f"Vector({self.components})"
        
# Example usage:
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = v1 + v2
v4 = v1 * v2
print("Sum:", v3)          # Output: Vector([5, 7, 9])
print("Dot Product:", v4)  # Output: 32