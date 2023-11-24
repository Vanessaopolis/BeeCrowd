# https://www.beecrowd.com.br/judge/pt/problems/view/1847
# Linguagem Python 3.11

temp1, temp2, temp3 = [int(t) for t in input().split(" ")]
    
if temp1 == temp2 < temp3:
    print(":)")

elif temp1 > temp2 <= temp3:
    print(":)")

elif temp1 < temp2 <= temp3 and temp3 - temp2 >= temp2 - temp1:
    print(":)")

elif temp1 > temp2 > temp3 and temp2 - temp3 < temp1 - temp2:
    print(":)")

else:
    print(":(")
