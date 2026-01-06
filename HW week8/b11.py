import math
def vector(p, q):
    return (q[0] - p[0], q[1] - p[1], q[2] - p[2])

def cross(u, v):
    return (
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0]
    )
def dot(u, v):
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
def magnitude(v):
    return math.sqrt(dot(v, v))
A = tuple(map(float, input().split()))
B = tuple(map(float, input().split()))
C = tuple(map(float, input().split()))
D = tuple(map(float, input().split()))
# Vector pháp tuyến
n1 = cross(vector(A, B), vector(A, C))
n2 = cross(vector(B, C), vector(B, D))
# Góc giữa hai mặt phẳng
cos_phi = dot(n1, n2) / (magnitude(n1) * magnitude(n2))
cos_phi = max(-1, min(1, cos_phi))  # tránh lỗi số học
phi = math.degrees(math.acos(cos_phi))
print(f"{phi:.2f}")