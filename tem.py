# อ่านค่าอุณหภูมิ (องศาเซลเซียส)
celsius = float(input())

# คำนวณองศาฟาเรนไฮต์และเคลวิน
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# แสดงผลลัพธ์: ฟาเรนไฮต์ และ เคลวิน คั่นด้วยเว้นวรรค
print(f"{fahrenheit:.2f} {kelvin:.2f}")
