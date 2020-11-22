#!/usr/local/bin/python3
####################################################
#

from multiprocessing import Pool, cpu_count
from timeit import default_timer as timer

cpu_cnt=cpu_count()
print("Ich nutze", cpu_cnt, "Prozesse")
prim_range = 1000000
chunk_size = 1000

# Funktionen

def primrechner(ps):
    pc=[]
    print(" Starte von", ps, "bis", ps+chunk_size-1)
    for z in range(ps, ps + chunk_size):
        pc.append(z)
        for z2 in range(2, z):
            if not z % z2:
                pc.remove(z)
                break
    # print(len(pc))
    return(len(pc))

def main():
    start = timer()

    with Pool(processes=cpu_cnt) as pool:
        start_values=list(range(1,prim_range, chunk_size))
        # print(start_values)
        res = pool.map(primrechner, start_values)

    # Abschluss
    print("Es wurden", sum(res), "Primzahlen gefunden")

    end = timer()
    print(end - start)

if __name__ == '__main__':
    main()
