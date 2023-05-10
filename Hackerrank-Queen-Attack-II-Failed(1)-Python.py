#Failed Variant.
#Original solution to the problem, however failed due to time and problems regarding the rd variable

n, k = map(int, input().split())
r_q, c_q = map(int, input(). split())
obstacles = []
for _ in range(k):
    obstacles.append(tuple(map(int, input().rstrip().split())))

def queensAttack(n, k, r_q, c_q, obstacles):
    #converting n into a tuple (Redundant, but wrote the code before realising that n is a single integer, so this is a bandaid fix)
    n = (n, n)
    
    # Finding all possible positions that can be taken by the Queen
    ru = [(i, c_q) for i in range(r_q + 1, n[0] + 1)] #row_up aka north
    rd = [((i * -1), c_q) for i in range((r_q * -1) + 1, 0)] #row_down aka south

    cl = [(r_q, i) for i in range(c_q + 1, n[1] + 1)] #column_left aka west
    cr = [(r_q, (i * -1)) for i in range((c_q * -1) + 1, 0)] #column_left aka east

    dlu = [(i, j * -1) for i, j in zip(range(r_q + 1, n[0] + 1), range((c_q * -1) + 1, 0))] #diagonal_left_up aka north_west
    dld = [(i * -1, j * -1) for i, j in zip(range((r_q * -1) + 1, 0), range((c_q * -1) + 1, 0))] #diagonal_left_down aka south_west
    dru = [(i, j) for i, j in zip(range(r_q + 1, n[0] + 1), range(c_q + 1, n[1] + 1))] #diagonal_right_up aka north_east
    drd = [(i * -1, j) for i, j in zip(range((r_q * -1) + 1, 0), range(c_q + 1, n[1] + 1))] #diagonal_right_down aka south_east

    #function comparing obstacles to the positions queen can take, if obstacle position == queen position, stop appending to the temp array 
    def ru_count(): #north
        global ru
        for i in ru:
            ru_rand = []
            if i not in obstacles:
                continue
            else:
                for j in range(ru.index(i), len(ru)):
                    ru_rand.append(ru[j])
            ru = [i for i in ru if i not in ru_rand]
    def rd_count(): #south
        global rd
        for i in rd:
            rd_rand = []
            if i not in obstacles:
                continue
            else:
                for j in range(rd.index(i), len(rd)):
                    rd_rand.append(rd[j])
            rd = [i for i in rd if i not in rd_rand]
    def cl_count(): #west
        global cl
        for i in cl:
            cl_rand = []
            if i not in obstacles:
                continue
            else:
                for j in range(cl.index(i), len(cl)):
                    cl_rand.append(cl[j])
            cl = [i for i in cl if i not in cl_rand]
    def cr_count(): #east
        global cr
        for i in cr:
            cr_rand = []
            if i not in obstacles:
                continue
            else:
                for j in range(cr.index(i), len(cr)):
                    cr_rand.append(cr[j])
            cr = [i for i in cr if i not in cr_rand]
    def dlu_count(): #north_west
        global dlu
        for i in dlu:
            dlu_rand = []
            if i not in obstacles:
                continue
            else:
                for j in range(dlu.index(i), len(dlu)):
                    dlu_rand.append(dlu[j])
            dlu = [i for i in dlu if i not in dlu_rand]
    def dld_count(): #south_west
        global dld
        for i in dld:
            dld_rand = []
            if i not in obstacles:
                continue
            else:
                for j in range(dld.index(i), len(dld)):
                    dld_rand.append(dld[j])
            dld = [i for i in dld if i not in dld_rand]
    def dru_count(): #north_east
        global dru
        for i in dru:
            dru_rand = []
            if i not in obstacles:
                continue
            else:
                for j in range(dru.index(i), len(dru)):
                    dru_rand.append(dru[j])
            dru = [i for i in dru if i not in dru_rand]
    def drd_count(): #south_west
        global drd
        for i in drd:
            drd_rand = []
            if i not in obstacles:
                continue
            else:
                for j in range(drd.index(i), len(drd)):
                    drd_rand.append(drd[j])
            drd = [i for i in drd if i not in drd_rand]

    #calling function if an element is in the obstacles array
    for i in ru:
        if i in obstacles:
            ru_count()
    for i in rd:
        if i in obstacles:
            rd_count()
    for i in cl:
        if i in obstacles:
            cl_count()
    for i in cr:
        if i in obstacles:
            cr_count()
    for i in dlu:
        if i in obstacles:
            dlu_count()
    for i in dld:
        if i in obstacles:
            dld_count()
    for i in dru:
        if i in obstacles:
            dru_count()
    for i in drd:
        if i in obstacles:
            drd_count()
    
    #returning total steps that can be taken by the queen
    return (len(ru + rd + cl + cr + dlu + dld + dru + drd))

#Printing results
result = queensAttack(n, k, r_q, c_q, obstacles)
print (result)
