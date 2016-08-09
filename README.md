## Packet parser for C++ applications

Python scritp that convert e.g wireshark output of packets to C/C++ code that put this packets to table in hex format.

# Usage

```bash
$ python3 cpp_packet_parser.py
```

# Example

```bash
$ python3 cpp_packet_parser.py 
Paste packet in hex format (e.g. from wireshark)  "|3d|f5|23|fg|" :
|00|ff|17|af|08|a4|fc|00|00|00|00|00|86|dd|60|00|00|00|00|28|3a|ff|fc|42|c6|b0|a9|06|85|96|4f|47|11|12|ec|ff|f9|55|fc|9d|e6|d3|bd|5b|2b|c4|13|74|0d|1a|ce|bc|22|4d|88|00|28|9d|e0|00|00|00|fc|42|c6|b0|a9|06|85|96|4f|47|11|12|ec|ff|f9|55|02|01|fc|00|00|00|00|00|01|01|00|ff|17|af|08|a4
C/C++ output:
pack3[0] = 0x00 ; pack3[1] = 0xff ; pack3[2] = 0x17 ; pack3[3] = 0xaf ; pack3[4] = 0x08 ; pack3[5] = 0xa4 ; pack3[6] = 0xfc ; pack3[7] = 0x00 ; 
pack3[8] = 0x00 ; pack3[9] = 0x00 ; pack3[10] = 0x00; pack3[11] = 0x00; pack3[12] = 0x86; pack3[13] = 0xdd; pack3[14] = 0x60; pack3[15] = 0x00; 
pack3[16] = 0x00; pack3[17] = 0x00; pack3[18] = 0x00; pack3[19] = 0x28; pack3[20] = 0x3a; pack3[21] = 0xff; pack3[22] = 0xfc; pack3[23] = 0x42; 
pack3[24] = 0xc6; pack3[25] = 0xb0; pack3[26] = 0xa9; pack3[27] = 0x06; pack3[28] = 0x85; pack3[29] = 0x96; pack3[30] = 0x4f; pack3[31] = 0x47; 
pack3[32] = 0x11; pack3[33] = 0x12; pack3[34] = 0xec; pack3[35] = 0xff; pack3[36] = 0xf9; pack3[37] = 0x55; pack3[38] = 0xfc; pack3[39] = 0x9d; 
pack3[40] = 0xe6; pack3[41] = 0xd3; pack3[42] = 0xbd; pack3[43] = 0x5b; pack3[44] = 0x2b; pack3[45] = 0xc4; pack3[46] = 0x13; pack3[47] = 0x74; 
pack3[48] = 0x0d; pack3[49] = 0x1a; pack3[50] = 0xce; pack3[51] = 0xbc; pack3[52] = 0x22; pack3[53] = 0x4d; pack3[54] = 0x88; pack3[55] = 0x00; 
pack3[56] = 0x28; pack3[57] = 0x9d; pack3[58] = 0xe0; pack3[59] = 0x00; pack3[60] = 0x00; pack3[61] = 0x00; pack3[62] = 0xfc; pack3[63] = 0x42; 
pack3[64] = 0xc6; pack3[65] = 0xb0; pack3[66] = 0xa9; pack3[67] = 0x06; pack3[68] = 0x85; pack3[69] = 0x96; pack3[70] = 0x4f; pack3[71] = 0x47; 
pack3[72] = 0x11; pack3[73] = 0x12; pack3[74] = 0xec; pack3[75] = 0xff; pack3[76] = 0xf9; pack3[77] = 0x55; pack3[78] = 0x02; pack3[79] = 0x01; 
pack3[80] = 0xfc; pack3[81] = 0x00; pack3[82] = 0x00; pack3[83] = 0x00; pack3[84] = 0x00; pack3[85] = 0x00; pack3[86] = 0x01; pack3[87] = 0x01; 
pack3[88] = 0x00; pack3[89] = 0xff; pack3[90] = 0x17; pack3[91] = 0xaf; pack3[92] = 0x08; pack3[93] = 0xa4;
```
