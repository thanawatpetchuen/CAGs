import string
xt = int(input("n: "))
name_list = string.ascii_uppercase[string.ascii_uppercase.index("X"):]
name_list += string.ascii_uppercase[:string.ascii_uppercase.index("X")]
# print(name_list)
label_list = []
d_list = []
for n in name_list:
    for i in range(1, xt+1):
        # d_list.append("D{}".format(i))
        if n != 'D':

            label_list.append("{}{}".format(n, i))

for i in range(1, xt+1):
    d_list.append("D{}".format(i))
            # print("{}{}".format(n, i))

label_list = label_list[:xt*xt]
varlist = []
for y in range(xt):
    for x in range(y, len(label_list), xt):
        varlist.append(label_list[x])
    # varlist.append(d_list[y])

test = list(list(zip(*varlist))[0])
# for i in range(1, 4):
#     jip = '{}+ '.format(i).join(test[:4])+'{}'.format("1")
print(d_list)
sd = [1,2,3,4]
jip = '{}'+' + {}'.join(test[:4])
print(jip.format(*sd))
print(jip)
