def maximum(s):
    if len(s) == 0:
        return None
    max = s[0]
    for e in s[1:]:
        if e > max:
            max = e
    return max

def compute_modes(l):
    freq = dict()
    for e in l:
        freq[e] = freq.get(e,0)+1
    max_freq = maximum(list(freq.values())) # maximum of a list
    modes = []
    for e in freq:
        if freq[e] == max_freq:
            modes.append(e)
    return modes