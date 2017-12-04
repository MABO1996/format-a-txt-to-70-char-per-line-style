
# coding: utf-8
# author Bo Ma
#  2017/12/3
# 做一个小的程序，将一个txt文档里的文字进行规范的输出
# 具体要求见 CS2310-2017-2018-Ass2 (New).pdf 第三题

# In[1]:
# 读取数据
import re
file1 = open('G:\桌面\input.txt')
#raw = " ".join(file1.readlines())
#按照行读取
raw = file1.read().replace("\n","\n ")
pat = re.compile(' [0-9]+.')
regresult = pat.findall(raw)
for i in range(len(regresult)):
    raw = raw.replace(regresult[i],'\n' + regresult[i])
# print(raw)
# 将[0-9].前面加上换行符
# 在换行符后面加一个空格方便进行分词
file1.close()
raw = raw.split(" ")
# 按照空格将所有的词分开，每个词作为一个字符串，形成一个字符串列表，(如果不规定使用空格分行，换行符不见了)

# In[2]
# 上面是获取数据初步处理，下面构造该函数完成要求



# 先将数据去掉重复的单词 - done
# 分段：原来的分段加上新的分段---应该不需要单独分，分行弄个好就行 -done
# 将文件分行，写一个函数写出空格分布均匀的行-done
def uniqueword(list):
    '删除连续出现的重复的单词'
    for i in reversed(range(len(list)-1)):
        # 反过来索引就不会改变之前的位置
            if list[i].lower() == list[i+1].lower():
                # 比较每个单词后面一个，如果相同删除后面一个
                list.pop(i+1)
    return list

def splitline(raw,maxnum = 70):
    '将文件按照每行字符数的要求进行分行，每一行一个list'
    line = []
    # 作为每一行的容器
    output = []
    # 作为输出的容器
    for i in range(len(raw)):
        if "\n" in raw[i]: 
            #如果存在换行符号那么需要特别对待
            line.append(raw[i])
            # 给目前的行加上一个单词
            if len(" ".join(line)) <= (maxnum):
                # 如果以换行符结尾且少于70个字符则为一行
                output.append(line)
                #print(line)
                line = []
            else:
                # 如果大于70则要分为两行
                output.append(line[:-1])
                output.append(raw[i])
                #print(line)
                line = []
        else:
            # 结尾不为换行符的单词
            line.append(raw[i])
            if len(" ".join(line)) > (maxnum):
                output.append(line[:-1])
                #print(line)
                line = []
                line.append(raw[i])
        if i == len(raw)-1:
            #最后一行由于没有满70要单独处理
            output.append(line)
            #print(line)
        #print(i,raw[i])
    return output
    
def disspace(list , maxnum = 70):
    '将一行内的单词整理为包含空格的样子，输入是一行里面所有单词作为元素的列表，输出为一个字符串'
    if len(list) != 1: 
        # 只有一个单词的行要单独处理，number-1=0不能作为除数
        number = len(list)
        if '\n' in list[-1]:
            # 结尾单词有换行的直接连接即可
            line = " ".join(list)
            return line
        else:
            line = [0]*(number)
            line[-1] = list[-1]
            charofword = len(''.join(list))
            avers = (maxnum-charofword)//(number - 1) #单词之间平均间隔
            lefts = (maxnum-charofword)%(number - 1)  #均分后剩下的空格，准备按照顺序依次分给前n个
            space = [" "*avers]*(number-1)
            for i in range(lefts):
                space[i] = space[i]+" "
            for i in range(number-1):
                line[i] = list[i]+space[i]
                # 空格和单词对应连接
            return "".join(line)
    else:
        return list[0] #输出为字符串而不能为列表

def add_n(list):
    '给每一行加上换行符使之可以完整的写入'
    for i, line in enumerate(list):
        if not ("\n" in line):
            list[i] = line + "\n"
    return list
# In[3]
# 用上面的函数进行处理            
uniqu_raw = uniqueword(raw)
# print(uniqu_raw)

output = splitline(uniqu_raw)
#print(output)


for i , line in enumerate(output):
    output[i] = disspace(line)
#每一行加上空格    
#print(output)                     
        
output_n = add_n(output)
print(output_n)


        


# In[4]:

# 写入文件
f = open('G:\桌面\output.txt',"w")
f.writelines(output)
f.close()

