data = open("sample.txt", "r").readlines()
data = [d.replace("\n","") for d in data]
print(data)

stack_data = data
print(stack_data)
stack_data = [l.replace("    ","-") for l in stack_data]
