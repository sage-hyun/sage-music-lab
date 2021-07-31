import sys
import os

if len(sys.argv) != 2:
    print("wrong argument")
    sys.exit(1)

filename = sys.argv[1]

f1 = open(filename, 'r', encoding="UTF8")

base = os.path.basename(filename)
f2 = open("./lyrics/"+ os.path.splitext(base)[0] + "_ENG.txt", 'w', encoding="UTF8")
f3 = open("./lyrics/"+ os.path.splitext(base)[0] + "_KOR.txt", 'w', encoding="UTF8")

while True:
    line = f1.readline()

    if not line: break
    
    if ord('가') <= ord(line[0]) <= ord('힣'):
        f3.write(line.lstrip().rstrip() +"\n")  # 좌우 양끝 whitespace 있으면 제거
    elif ord('a') <= ord(line[0].lower()) <= ord('z'): 
        f2.write(line.lstrip().rstrip() +"\n")
    elif line[0] == '[':
        None
    # 원래 line[0]으로 했는데 'Cause가 많아서 두번째로 또확인...
    elif len(line) > 1:
        if ord('a') <= ord(line[1].lower()) <= ord('z'): 
            f2.write(line.lstrip().rstrip() +"\n")
    
    # 공백
    else:
        f2.write(" \n")
        f3.write(" \n")


f1.close()
f2.close()
f3.close()
