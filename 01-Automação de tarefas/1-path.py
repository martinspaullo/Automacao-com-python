from pathlib import Path

p1 = Path('dados','teste.txt')  
print(p1)
print(type(p1)) 
print(p1.name)
print(f"{p1.stem} valor anterior ao arquivo") # 
print(p1.suffix)
print(p1.exists())
if p1.exists():
    with open(p1, 'r', encoding='utf-8') as file:
        print(file.read())
        
p2 = Path('dados')
print(list(p2.iterdir()))
