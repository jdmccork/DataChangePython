#for number inputs only
from math import ceil
asciilist=['NUL', 'SOH', 'STX', 'ETX', 'EOT', 'ENQ', 'ACK', 'BEL', 'BS', 'HT', 'LF', 'VT', 'FF', 'CR', 'SO', 'SI', 'DLE', 'DC1', 'DC2', 'DC3', 'DC4', 'NAK', 'SYN', 'ETB', 'CAN', 'EM', 'SUB', 'ESC', 'FS', 'GS', 'RS', 'US', 'SP', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'DEL','Ç', 'ü', 'é', 'â', 'ä', 'à', 'å', 'ç', 'ê', 'ë', 'è', 'ï', 'î', 'ì', 'Ä', 'Å', 'É', 'æ', 'Æ', 'ô', 'ö', 'ò', 'û', 'ù', 'ÿ', 'Ö', 'Ü', '¢', '£', '¥', '₧', 'ƒ', 'á', 'í', 'ó', 'ú', 'ñ', 'Ñ', 'ª', 'º', '¿', '⌐', '¬', '½', '¼', '¡', '«', '»', '░', '▒', '▓', '│', '┤', '╡', '╢', '╖', '╕', '╣', '║', '╗', '╝', '╜', '╛', '┐', '└', '┴', '┬', '├', '─', '┼', '╞', '╟', '╚', '╔', '╩', '╦', '╠', '═', '╬', '╧', '╨', '╤', '╥', '╙', '╘', '╒', '╓', '╫', '╪', '┘', '┌', '█', '▄', '▌', '▐', '▀', 'α', 'ß', 'Γ', 'π', 'Σ', 'σ', 'µ', 'τ', 'Φ', 'Θ', 'Ω', 'δ', '∞', 'φ', 'ε', '∩', '≡', '±', '≥', '≤', '⌠', '⌡', '÷', '≈', '°', '∙', '·', '√', 'ⁿ', '²', '■']
#binary converter
def binconvert():
    z=decimal
    binary=''
    while z>0:
        if z%2 == 1:
            binary=str(1)+binary
            z=(z-1)/2
        else:
            binary=str(0)+binary
            z/=2
    while len(binary)%4!=0:
        binary='0'+binary
    print(str(decimal)+' in binary is '+binary)
    return(binary)

def decconvert(binary):
    decimal=0
    for p in range(int(len(binary)/4)):
        x=binary[4*p:4*p+4]
        for i in range(len(x)):
            if int(x[i]) == 1:
                decimal+=2**((len(x)-1-i)+(4*(int(len(binary)/4)-p-1)))
    return int(decimal)

    #hex converter
def hexconvert(binary):
    hexadecimal=''
    while True:
        for i in range(int(len(binary)/4)):
           t=decconvert(binary[4*i:4*i+4])
           hexadecimal+=hexlist[t]
        print(str(decimal)+' in hex is '+hexadecimal)
        return hexadecimal

def octconvert(decimal):
    octal=''
    z=decimal
    while z>0:
        octal=str(z%8)+octal
        z=z//8
    print(str(decimal)+' in octal is ' +octal)

def asciiconvert(binary):
    asc=''
    for i in range(ceil(len(binary)/8)):
        t=decconvert(binary[(8*i)+1:8*i+8])
        if t<=127:
            print(binary[8*i:8*i+8])
            asc+=asciilist[t]
    print(ord(str(decimal)))
    print(str(decimal)+' in ascii is '+asc)

while True:
    decimal=int(input())#input of decimal number
    print(bin(decimal))
    hexlist=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    binary=binconvert()
    print(hex(decimal))
    hexadecimal=hexconvert(binary)
    print(oct(decimal))
    octal=octconvert(decimal)
    #print(ord(str(decimal)))
    ASCII=asciiconvert(binary)
