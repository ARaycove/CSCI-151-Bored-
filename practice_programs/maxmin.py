import sys
import stdio

values = []
while not stdio.isEmpty():
    try:
        value = stdio.readFloat()
        values.append(value)
    except:
        value = stdio.readString()
        if value.lower() == "exit":
            break
    maximum = max(values)
    minimum = min(values)
    


stdio.writeln(f"Max value: {maximum}")
stdio.writeln(f"Min value: {minimum}")