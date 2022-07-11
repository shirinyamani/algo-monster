def smallestRegion(regions, reg1, reg2):
    dic = {}
    for region in regions:
        parent = region[0]
        for i in range(1,len(region)):
            dic[region[i]] = parent

    dic_region1 = {}
    while region1 in dic:
        dic_region1[region1] = 1
        region1 = dic[region1]

    while region2 in dic:
        if region2 in dic_region1:
            return region2
        region2 = dic[region2]
    return regions[0][0]
