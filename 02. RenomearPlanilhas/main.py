from os import chdir, listdir, rename

cores = {
    "azul":"\033[4;34m",
    "verde_bg":"\033[1;32m",
    "amarelo":"\033[4;33m",
    "limpa":"\033[0;0;0m"
}

path = chdir("C:\\Users\\christiansouza\\Documents\\Ocyan\\05. CODE\\02. RenomearPlanilhas\\pasta01")

list_name = []
list_last_item = []
for file in listdir(path):
    file_name = file.split()
    last_item = file_name[len(file_name)-1].split(".")
    temp = last_item[len(last_item)-1]
    last_item[len(last_item)-1] = last_item[len(last_item)-2]
    last_item[len(last_item)-2] = temp
    list_last_item.append(last_item)
    list_name.append(file_name)

for i in range(len(list_last_item)):
    a = ""
    c = 0
    for j in list_last_item[i]:
        if c != 2:
            a = a + j + "."
        else:
            a = a + j
        c = c + 1
        list_last_item[i]=a
for t in range(len(list_name)):
    list_name[t][len(list_name[t])-1] = list_last_item[t]

for i in range(len(list_name)):
    a = ""
    c = 0
    for j in list_name[i]:
        a = a + j + " "
        c = c + 1
        list_name[i]=a.strip()

c = 0
for file in listdir(path):
    rename(file, list_name[c])
    if c%2==0:
        print("{}{}{}".format(cores["azul"],list_name[c], cores["limpa"]))
    else:
        print("{}{}{}".format(cores["amarelo"],list_name[c], cores["limpa"]))
    c += 1
print("{}------------ {} arquivos renomeados ------------{}".format(cores["verde_bg"], c, cores["limpa"]))