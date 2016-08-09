# Packet parser for C++ applications

Python scritp that convert e.g. wireshark output to C/C++ code that put packets to table in hex format.

## Usage

```bash
$ python3 packet_parser_cpp.py
```
## Example

```txt
$ python3 packet_parser_cpp.py 
Paste packet in hex format (e.g. from wireshark)  "|3d|f5|23|fg" :
|0a|fd|12|af|08|b4|fc|00|00|00|00|90|86|dd|60|00|00|00|04|28|3a|ff|fc|42|c6|b0|aa|06|85|96|4f|47|11|12|ec|ff|f9|55|fc|9d|e6|d3|bd|5b|2b|c4|13|74|0d|1a|ce|bc|22|4d|88|00|28|9d|e0|00|00|00|fc|42|c6|b0|a9|06|85|96|4f|47|11|12|ec|ff|f9|55|02|01|fc|00|00|00|00|00|01|01|00|ff|17|af|08|a4
C/C++ output:
pack[0]  = 0x0a; pack[1]  = 0xfd; pack[2]  = 0x12; pack[3]  = 0xaf; pack[4]  = 0x08; pack[5]  = 0xb4; pack[6]  = 0xfc; pack[7]  = 0x00; 
pack[8]  = 0x00; pack[9]  = 0x00; pack[10] = 0x00; pack[11] = 0x90; pack[12] = 0x86; pack[13] = 0xdd; pack[14] = 0x60; pack[15] = 0x00; 
pack[16] = 0x00; pack[17] = 0x00; pack[18] = 0x04; pack[19] = 0x28; pack[20] = 0x3a; pack[21] = 0xff; pack[22] = 0xfc; pack[23] = 0x42; 
pack[24] = 0xc6; pack[25] = 0xb0; pack[26] = 0xaa; pack[27] = 0x06; pack[28] = 0x85; pack[29] = 0x96; pack[30] = 0x4f; pack[31] = 0x47; 
pack[32] = 0x11; pack[33] = 0x12; pack[34] = 0xec; pack[35] = 0xff; pack[36] = 0xf9; pack[37] = 0x55; pack[38] = 0xfc; pack[39] = 0x9d; 
pack[40] = 0xe6; pack[41] = 0xd3; pack[42] = 0xbd; pack[43] = 0x5b; pack[44] = 0x2b; pack[45] = 0xc4; pack[46] = 0x13; pack[47] = 0x74; 
pack[48] = 0x0d; pack[49] = 0x1a; pack[50] = 0xce; pack[51] = 0xbc; pack[52] = 0x22; pack[53] = 0x4d; pack[54] = 0x88; pack[55] = 0x00; 
pack[56] = 0x28; pack[57] = 0x9d; pack[58] = 0xe0; pack[59] = 0x00; pack[60] = 0x00; pack[61] = 0x00; pack[62] = 0xfc; pack[63] = 0x42; 
pack[64] = 0xc6; pack[65] = 0xb0; pack[66] = 0xa9; pack[67] = 0x06; pack[68] = 0x85; pack[69] = 0x96; pack[70] = 0x4f; pack[71] = 0x47; 
pack[72] = 0x11; pack[73] = 0x12; pack[74] = 0xec; pack[75] = 0xff; pack[76] = 0xf9; pack[77] = 0x55; pack[78] = 0x02; pack[79] = 0x01; 
pack[80] = 0xfc; pack[81] = 0x00; pack[82] = 0x00; pack[83] = 0x00; pack[84] = 0x00; pack[85] = 0x00; pack[86] = 0x01; pack[87] = 0x01; 
pack[88] = 0x00; pack[89] = 0xff; pack[90] = 0x17; pack[91] = 0xaf; pack[92] = 0x08; pack[93] = 0xa4; 
```
