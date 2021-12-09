
def open_input(filename):
    with open(filename,'r') as file:
        result = []
        for line in file:
            line = line.strip("\n")
            res = line.split(" | ")
            result.append(note_entry(res[0].split(" "),res[1].split(" ")))
    return result

all_wires = "abcdefg"

original_numbers = ["abcefg","cf","acdeg","acdfg","bcdf","abdfg","abdefg","acf","abcdefg","abcdfg"]

def get_allcombos():
    combos = []
    for a in all_wires:
        a_wire = all_wires.replace(a,'')
        for b in a_wire:
            b_wire = a_wire.replace(b,'')
            for c in b_wire:
                c_wire = b_wire.replace(c,'')
                for d in c_wire:
                    d_wire = c_wire.replace(d,'')
                    for e in d_wire:
                        e_wire = d_wire.replace(e,'')
                        for f in e_wire:
                            g = e_wire.replace(f,'')
                            combos.append({'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g})
    return combos
        


class note_entry:
    def __init__(self,leftside_array,rightside_array):
        self.signalpattern = leftside_array
        self.outputvalues = rightside_array

        for i in self.outputvalues:
            self.signalpattern.append(i)

    def makes_sense(self,replace_dic):
        for numb in self.signalpattern:
            decrypted = replace_letters(numb,replace_dic)
            if not decrypted in original_numbers:
                return False
        return True
    
    def find_good_dict(self,combos):
        for combo in combos:
            if self.makes_sense(combo):
                return combo
    
    def find_output(self,combos):
        dict = self.find_good_dict(combos)

        x = 0
        for i,numb in enumerate(self.outputvalues):
            decrypt = replace_letters(numb,dict)
            n = get_num_from_string(decrypt)
            x += n * 10**(3-i)
        return x



        

def replace_letters(original,replace_dic):
    result = ""
    for i in original:
        result+=replace_dic[i]
    result = sortString(result)
    return result

def sortString(str):
    return ''.join(sorted(str))

def get_num_from_string(numb_str):
    for i,s in enumerate(original_numbers):
        if numb_str == s:
            return i

def sum_all_outputs(input,combos):
    x = 0
    for i in input:
        x += i.find_output(combos)
    return x


input = open_input("input.txt")

combos = get_allcombos()

print(sum_all_outputs(input,combos))