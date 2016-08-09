def packet_bytes(str):
    number_of = 0
    for x in str:
        if x == '|':
            number_of += 1;
    return number_of

def digits(num):
    if num < 0:
        return 0
    digits = 1
    while num > 10:
        num /= 10
        digits += 1
    return digits

if __name__ == "__main__":

    num = 0
    hex_start = True
    str = input("Paste packet in hex format (e.g. from wireshark)  \"|3d|f5|23|fg|\" :\n")

    # EXAMPLES OF INPUTS
        #str = "|00|ff|17|af|08|a4|fc|00|00|00|00|00|86|dd|60|00|00|00|00|28|3a|ff|fc|42|c6|b0|a9|06|85|96|4f|47|11|12|ec|ff|f9|55|fc|9d|e6|d3|bd|5b|2b|c4|13|74|0d|1a|ce|bc|22|4d|88|00|28|9d|e0|00|00|00|fc|42|c6|b0|a9|06|85|96|4f|47|11|12|ec|ff|f9|55|02|01|fc|00|00|00|00|00|01|01|00|ff|17|af|08|a4"
        #str = "|00|ff|17|af|08|a4|fc|00|00|00|00|00|86|dd|60|00|00|00|00|28|3a|ff|fc|00|c6|b0|a9|06|85|96|4f|47|11|12|ec|ff|f9|55|fc|9d|e6|d3|bd|5b|2b|c4|13|74|0d|1a|ce|bc|22|4d|88|00|29|21|e0|00|00|00|fc|00|c6|b0|a9|06|85|96|4f|47|11|12|ec|ff|f9|55|02|01|fc|00|00|00|00|00|01|01|00|ff|17|af|08|a4"

    number_of_bytes = packet_bytes(str);

    print("C/C++ output:");

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
                print(x,(digits(number_of_bytes)-digits(num))*" ",";",sep="",end=" ")
                hex_start = True

            if not (num) % 8 and hex_start:
                print("")
    print()
