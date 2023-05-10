#Successful Variant (Learnt and implemented from the Hackerrank Solution on Programmingoneonone)

#calculating the maximum number of steps that can be taken by the queen
moves = {'n':(n - r_q), 's':(r_q - 1), 'e':(n - c_q), 'w':(c_q - 1), 'ne':min(n - r_q, n - c_q), 
         'nw':min(n - r_q, c_q - 1), 'se':min(r_q - 1, n - c_q), 'sw':min(r_q - 1, c_q - 1)}

for i in range(k):
    r, c = map(int, input().split())
    if c == c_q:
        if r > r_q:
            moves['n'] = min(r - r_q - 1, moves['n'])
        else:
            moves['s'] = min(r_q - r - 1, moves['s'])
    elif r == r_q:
        if c > c_q:
            moves['e'] = min(c - c_q - 1, moves['e'])
        else:
            moves['w'] = min(c_q - c - 1, moves['w'])
    elif r - c == r_q - c_q:
        if r > r_q and c > c_q:
            moves['ne'] = min(r - r_q - 1, moves['ne'])
        elif r < r_q and c < c_q:
            moves['sw'] = min(r_q - r - 1, moves['sw'])
    elif r + c == r_q + c_q:
        if r > r_q and c < c_q:
            moves['nw'] = min(r - r_q - 1, moves['nw'])
        elif r < r_q and c > c_q:
            moves['se'] = min(r_q - r - 1, moves['se'])
        
print (sum(moves.values()))
