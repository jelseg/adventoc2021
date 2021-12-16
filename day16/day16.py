
#input = "C200B40A82"

input = "A20D74AFC6C80CEA7002D4009202C7C00A6830029400F500218080C3002D006CC2018658056E7002DC00C600E75002ED6008EDC00D4003E24A13995080513FA309482649458A054C6E00E6008CEF204BA00B080311B21F4101006E1F414846401A55002F53E9525B845AA7A789F089402997AE3AFB1E6264D772D7345C6008D8026200E41D83B19C001088CB04A294ADD64C0129D818F802727FFF3500793FFF9A801A801539F42200DC3801A39C659ACD3FC6E97B4B1E7E94FC1F440219DAFB5BB1648E8821A4FF051801079C379F119AC58ECC011A005567A6572324D9AE6CCD003639ED7F8D33B8840A666B3C67B51388440193E003413A3733B85F2712DEBB59002B930F32A7D0688010096019375300565146801A194844826BB7132008024C8E4C1A69E66108000D39BAD950802B19839F005A56D9A554E74C08028992E95D802D2764D93B27900501340528A7301F2E0D326F274BCAB00F5009A737540916D9A9D1EA7BD849100425D9E3A9802B800D24F669E7691E19CFFE3AF280803440086C318230DCC01E8BF19E33980331D631C593005E80330919D718EFA0E3233AE31DF41C67F5CB5CAC002758D7355DD57277F6BF1864E9BED0F18031A95DDF99EB7CD64626EF54987AE007CCC3C4AE0174CDAD88E65F9094BC4025FB2B82C6295F04100109263E800FA41792BCED1CC3A233C86600B48FFF5E522D780120C9C3D89D8466EFEA019009C9600A880310BE0C47A100761345E85F2D7E4769240287E80272D3CEFF1C693A5A79DFE38D27CCCA75E5D00803039BFF11F401095F714657DC56300574010936491FBEC1D8A4402234E1E68026200CC5B8FF094401C89D12E14B803325DED2B6EA34CA248F2748834D0E18021339D4F962AB005E78AE75D08050E10066114368EE0008542684F0B40010B8AB10630180272E83C01998803104E14415100623E469821160"


def gethexcondict():
    with open("hexcon.txt","r") as file:
        hexbindict = {}
        for line in file:
            line = line.strip("\n")
            d = line.split(" = ")
            hexbindict[d[0]] = d[1]
    return hexbindict

hexbin = gethexcondict()

def hex2bin(hexstr):
    res = ""
    for c in hexstr:
        res+=hexbin[c]
    return res

def decodeNumber(binstr):
    V = binstr[0:3]
    Vi = int(V,base=2)
    T = binstr[3:6]
    Ti = int(T,base=2)
    Nimportant = 6
    #Meaningfull = V+T
    if T == '100':
        s = binstr[6:]
        N = ""
        i = 0
        notend = True
        while notend:
            if s[5*i] == "0":
                notend = False
            N += s[5*i+1:5*i+5]
            i+=1
        Nimportant += 5*i
        #Meaningfull += s[0:5*i]
        return Vi,Nimportant, int(N,base=2)
    elif binstr[6]=='0':
        #Meaningfull += '0'
        Nimportant += 1
        L = binstr[7:22]
        #Meaningfull+=L
        Nimportant += 15
        L = int(L,base=2)
        a = 0
        Vtot = Vi
        S = binstr[22:]
        all_numbers = []
        while a < L:
            s = S[a:]
            Vpart,Nimppart,Npart = decodeNumber(s)
            a += Nimppart
            Vtot += Vpart
            all_numbers.append(Npart)
            #print(a)
            #print(L)
        #Meaningfull += S[0:L]
        Nimportant += L
        N = applyOperator(all_numbers,Ti)
        return Vtot,Nimportant,N
    else:
        #Meaningfull += '1'
        Nimportant += 1
        L = binstr[7:18]
        #Meaningfull += L
        Nimportant += 11
        L = int(L,base=2)
        a = 0
        S = binstr[18:]
        Vtot = Vi
        all_numbers = []
        for i in range(L):
            s = S[a:]
            Vpart,Nimppart,Npart = decodeNumber(s)
            a += Nimppart
            Vtot += Vpart
            all_numbers.append(Npart)
        #Meaningfull += S[0:a]
        Nimportant += a
        #print(Vi)
        N = applyOperator(all_numbers,Ti)
        return Vtot,Nimportant,N
        
        
def applyOperator(Numbers,typeidint):
    i = typeidint
    #print(Numbers)
    if i == 0:
        return sum(Numbers)
    if i == 1:
        a = 1
        for n in Numbers:
            a *= n
        return a
    if i == 2:
        return min(Numbers)
    if i == 3:
        return max(Numbers)
    if i == 5:
        if Numbers[0] > Numbers[1]:
            return 1
        else:
            return 0
    if i == 6:
        if Numbers[0] < Numbers[1]:
            return 1
        else:
            return 0
    if i == 7:
        if Numbers[0] == Numbers[1]:
            return 1
        else:
            return 0

inp = hex2bin(input)
Vi,M,D = decodeNumber(inp)
print(Vi)
print(M)
print(D)