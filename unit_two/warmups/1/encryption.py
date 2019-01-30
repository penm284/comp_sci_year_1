import b_hash

binary_hash = b_hash.b_bash
#print(binary_hash)

#create a function that takes in string and returns binary
#def encrypt(str):
#    output
#    ans = []
#    for x in str:
#        # to get value from key in hash
#        temp = binary_hash[x]
#        #add binary to ans arr
#        ans.append(temp)
#        #add delimiter
#    ans = '-'.join(ans)
#    return(ans)
#call and print out method for debugging
#my_mess = encrypt('hello')
#print(my_mess)









def decrypt(binary):
    ans = []
    binary = binary.split("-")
    for x in binary:
        for key, value in binary_hash.items():
            if value == x:
                x = key
                ans.append(key)
    key = ''.join(ans)
    print(key)

message = '1110100-1101111- -1100111-1100101-1110100- -1100101-1111000-1110100-1110010-1100001- -1100011-1110010-1100101-1100100-1101001-1110100- -1111001-1101111-1110101- -1101101-1110101-1110011-1110100- -1100011-1101111-1101101-1100101--1110100-1101111- -1100011-1101100-1100001-1110011-1110011- -1100001-1101110-1100100- -1110100-1100101-1101100-1101100- -1101101-1100101- -1110111-1101000-1101111- -1111001-1101111-1110101-1110010- -1100110-1100001-1110110-1101111-1110010-1101001-1110100-1100101- -1110000-1110010-1101111-1100111-1110010-1100001-1101101-1101101-1100101-1110010- -1101001-1110011- -1100001-1101110-1100100- -1110111-1101000-1111001'

decrypt(message)
