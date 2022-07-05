def ecode(strs): #O(n)
    res = ""
    for s in strs: #go through each string
        res += str(len(str)) + "#" + s

    return res


def decode(strs):
    res, i = [], 0 #i is gonna tell us where we are in the string
    while i < len(strs): #iterate chr by chr
         j = i #we wanna find the end of the string ~ delimiter ~ where the word ends # j is the second pointer
         while str[j]  != "#": #while we have chr left to iterate
             j += 1

         length = int(str[i:j]) #untill the point we reach end of the string #how far we gotta go inorder to get all of the chrs after j
         res.append(str[j + 1: j + 1 + length]) #get the word
         i = j + 1 + length #move up to the nxt word in the list ~ update i

    return res


        
