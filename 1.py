def groupAnagrams(strs):
    groups = {}
    for s in strs:
        key = "".join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    result = []
    for value in groups.values():
        result.append(value)

    return result
    
print(groupAnagrams(["eat", "tea"]))

