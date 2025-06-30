# กำหนดเซต a และ b
a = {10, 20, 30, 40, 50, 60}
b = {30, 40, 50, 60, 70, 80}

# 1. ผลรวมของเซต a และ b (union)
print(sorted(a | b))

# 2. สมาชิกที่อยู่ทั้งใน a และ b (intersection)
print(sorted(a & b))

# 3. สมาชิกที่อยู่ใน a แต่ไม่อยู่ใน b (a - b)
print(sorted(a - b))

# 4. สมาชิกที่ไม่ซ้ำกันใน a และ b (symmetric difference)
print(sorted(a ^ b))
