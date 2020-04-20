import os

pymodules = {}
path = input("输入路径：")
pyfiles = [f for f in os.listdir(os.path.abspath(path)) if f.endswith('.py')]

for f in pyfiles:
    module = f[:-3]
    pymodules.setdefault(module, '')
    pyfile = os.path.join(path, f)
    file = open(pyfile)
    doc = False
    for line in file:
        if line.strip().startswith('"""') and line.strip().endswith('"""'):
            pymodules[module] += line
            file.close()
            break
        elif line.strip().startswith('"""') or line.strip().startswith('r"""') and len(line) > 3:
            doc = True
            pymodules[module] += line
            continue
        elif doc:
            if line == '"""':
                pymodules[module] += line
                file.close()
                doc = False
                break
            else:
                pymodules[module] += line
        else:
            continue
    file.close()

hasdoc = []
nodoc = []
for module in pymodules:
    if pymodules[module]:
        hasdoc.append(module)
    else:
        nodoc.append(module)

print('没有文档模块:')
for key in nodoc:
    print(key)

print("")

print("有文档模块:")
for key in hasdoc:
    print("%s：%s" % key, pymodules[key])
