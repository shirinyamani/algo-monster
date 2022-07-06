def smallestRegion(regions, reg1, reg2):
    dic = {}
    for reg in regions:
        parent = reg[0]
        for i in range(1, len(reg)):
            dic[reg[i]] = parent
    
    dic_reg1 = {}
    while reg1 in dic:
        dic_reg1[reg1] = 1
        reg1 = dic[reg1]

    while reg2 in dic:
        if reg2 in dic_reg1:
            return reg2
        reg2 = dic[reg2]

        
    return regions[0][0]
