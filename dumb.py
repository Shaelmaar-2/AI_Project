def calc(l):
    newb = round(0.72*l[0] + 0.18*l[1], 2)
    newc = round(0.72*l[1] + 0.18*l[2],2)
    newd = round(0.9*l[0],2)
    newe = max(round(0.72*l[3] + 0.18*l[4],2),round(0.9*l[1],2))
    newf = max(round(0.72*l[4] + 0.18*l[5],2),round(0.9*l[2],2))
    return [10,newb,newc,newd,newe,newf]

