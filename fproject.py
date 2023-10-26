length = float(input("Введите длину стены: ").replace(",", "."))
width = float(input("Введите ширину стены:").replace(",", "."))
height = float(input("Введите высоту стены: ").replace(",", "."))
square = 2 * (length + width) * height
print(square)