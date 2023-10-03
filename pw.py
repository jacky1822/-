path = "pw.txt"
pw = []
with open(path, "w") as f:
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                for l in range(0, 10):
                    for a in range(0, 2):
                        for b in range(1, 10):
                            for c in range(0, 4):
                                for d in range(0, 10):
                                    if a == 1 and b >= 3:
                                        break
                                    elif c == 0 and d == 0:
                                        continue
                                    elif c == 3 and d >= 2:
                                        break
                                    else:
                                        pw = "%x%x%x%x%x%x%x%x"%(i,j,k,l,a,b,c,d)
                                        f.write(pw + "\n")
