
num = 0
hex_start = True
str = "|00|ff|17|af|08|a4|fc|00|00|00|00|00|86|dd|60|00|00|00|00|28|3a|ff|fc|42|c6|b0|a9|06|85|96|4f|47|11|12|ec|ff|f9|55|fc|9d|e6|d3|bd|5b|2b|c4|13|74|0d|1a|ce|bc|22|4d|88|00|28|9d|e0|00|00|00|fc|42|c6|b0|a9|06|85|96|4f|47|11|12|ec|ff|f9|55|02|01|fc|00|00|00|00|00|01|01|00|ff|17|af|08|a4"

for x in str:
    if x == '|':
        print("pack[", num, "] = ",sep="",end="")
        num +=1
        hex_start = True
    else:
        if hex_start:
            print("0x",x,sep="",end="")
            hex_start = False
        else:
            print(x,";",sep="",end=" ")
            hex_start = True

        if not (num) % 10 and hex_start:
            print("")

