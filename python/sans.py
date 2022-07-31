import os

# 读取文件
if (os.path.isfile("www.txt")):
    f = open('www.txt', 'r')
    ls1 = f.readlines()
    www = [s.strip() for s in ls1]
    print(www)
else:
    print('文件不存在')
    www = []

if (os.path.isfile("name.txt")):
    f = open('name.txt', 'r',encoding='UTF-8')
    ls2 = f.readlines()
    name = [s.strip() for s in ls2]
    print(name)
else:
    print('文件不存在')
    name = []
if input('添加？（y/n）') == 'y':
    # 添加输入的内容
    a = int(input('循环次数：'))
    for i in range(a):
        name.append(input('输入名字：'))
        www.append(input('输入网址：'))
    print(name)
    print(www)

# 写入文件
f = open('html.txt', 'w')
for i in range(len(name)):
    f.write('<v-btn class="ma-2" color="primary" href="%s">%s</v-btn>' %
            (www[i], name[i]))
print('写入html.txt文件成功')
f.close()

f = open('name.txt', 'w')
for i in range(len(name)):
    f.write(name[i])
    f.write('\n')
print('写入name.txt文件成功')

f = open('www.txt', 'w')
for i in range(len(www)):
    f.write(www[i])
    f.write('\n')
print('写入www.txt文件成功')

print('写入完成')


#创建html文件
f = open('index.html', 'w')
