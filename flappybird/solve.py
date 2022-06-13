### Author: bluetickwarrior

key2 = [0x7caa42eb, 0xcd53fda8, 0xf7420557, 0x5267eec4, 0x793e70ed, 
    0x68d1aec0, 0x38da23eb, 0x6f1d6fb1, 0x39489b7b, 0xf4f87516, 
    0xed67bc18, 0x8ad36ba0, 0xaf2a684f, 0x80883171, 0x86ce7d28, 
    0x438cb016, 0x5784988c, 0x4bb5278b, 0xbfdcd0c6, 0x6dda7789, 
    0xb0f09aa3, 0x557478be, 0xc372aee8, 0x40a28470, 0xa855383a]

key1 = [0xAA, 0x7A, 0xE1, 0xBB, 0x9A, 0xE7, 0xFF, 0x7C, 0x35, 0x01, 
    0x06, 0x09, 0xC2, 0x50, 0x62, 0x38, 0xDB, 0x76, 0xD5, 0xE1, 
    0x68, 0xA9, 0xBF, 0xB4, 0x52, 0x8F, 0xC0, 0x17, 0x0E, 0x2F, 
    0xDA, 0xEA, 0x8A, 0xCF, 0xA2, 0x90, 0xE7, 0x08, 0xEB, 0x0E, 
    0x3B, 0x14, 0x72, 0xBE, 0x9A, 0xDE, 0xD5, 0x51, 0x97, 0x2C, 
    0xBC, 0xF3, 0x35, 0xB6, 0x21, 0x29, 0x7D, 0xA8, 0xD7, 0x2B, 
    0xED, 0xFE, 0xF0, 0x00]

lfsr2_seed = 0x1A2B3C4D

def genFlag1(n):
    v1 = key1[n]
    return v1 ^ lfsr1(n)

def sar1(num):

    msb = num & (2**31)
    num >>= 1
    if msb:
        num += (2**31)

    return num

def lfsr2(n):
    
    global lfsr2_seed
    for i in range(n):
        lsb = lfsr2_seed & 1
        lfsr2_seed = sar1(lfsr2_seed)
        if lsb:
            
            lfsr2_seed ^= 0x80000DD7

    return lfsr2_seed

def lfsr1(n):

    seed = 43981
    for i in range(n):
        lsb = seed & 1
        seed = (seed >> 1)
        if lsb:
            seed ^= 0x82ee
            
    return seed

def genFlag2(i):

    v1 = lfsr1(i) & 0xffff
    
    return (lfsr2(v1) ^ key2[int(i / 10000)]).to_bytes(4, 'little')

def main():
    
    flag1 = []
    flag2 = b''
    for actualScore in range(1, 250001):
        if actualScore <= 0x3f:
            flag1.append(chr(genFlag1(actualScore - 1) & 0xff))
            
        lfsr2(1)
        if (((actualScore % 10000) == 0) and ((actualScore /10000) <= 0x19)):
            flag2 += (genFlag2(actualScore - 10000))
     
    print(''.join(flag1))
    print(flag2)
    
    
if __name__ == "__main__":
    main()
