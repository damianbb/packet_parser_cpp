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
    str = input("Paste packet in hex format (e.g. from wireshark)  \"|3d|f5|23|fg\" :\n")

    number_of_bytes = packet_bytes(str);

    print("C/C++ output:");

    for x in str:
        if x == '|':
            print("pack[", num, "] ",(digits(number_of_bytes)-digits(num+1))*" ","= ",sep="",end="")
            num +=1
            hex_start = True
        else:
            if hex_start:
                print("0x",x,sep="",end="")
                hex_start = False
            else:
                print(x,";",sep="",end=" ")
                hex_start = True

            if not (num) % 8 and hex_start:
                print("")
    print()
