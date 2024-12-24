
import graphviz

dot = graphviz.Digraph(comment='d24')

# dot.node('A', 'King Arthur')  # doctest: +NO_EXE
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')
# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')


# doctest_mark_exe()

unknw = []
known = []
xvals,yvals = "",""
haveInitialized = False
for k in open("input.txt"):
    if k == "\n":
        haveInitialized = True
        continue
    if not haveInitialized:
        el1,el2 = k.strip().split()
        known.append([el1.replace(":",""), int(el2)])
        # dot.node(el1,el1)
        if el1[0] == "x": xvals = el2 + xvals
        else: yvals = el2 + yvals
    else:
        k = k.strip().replace("-> ","")
        in1,cmd,in2,out = k.split(" ")
        dot.node(in1,in1)
        dot.node(in2,in2)
        dot.node(out,out + "\n" + cmd)
        dot.edge(in1,out)
        dot.edge(in2,out)
        unknw.append([in1,in2,cmd,out])

dot.render('graphwiz1').replace('\\', '/')


currStackElms = []
while True:
    if len(currStackElms) > 0:
        known = known + currStackElms
    currStackElms = []
    for el in unknw:
        in1,in2,cmd,out = el[0],el[1],el[2],el[3]
        first,sec = 0,0
        for ce in known:
            # print(cmd)
            c = ce[0]
            if c == in1: first = ce
            elif c == in2: sec = ce
            if first != 0 and sec != 0: break
        if first == 0 or sec == 0: 
            continue
        res = None
        c1,c2 = first[1],sec[1]
        if cmd == "XOR":
            res = c1 ^ c2
        elif cmd == "OR":
            res = c1 | c2
        elif cmd == "AND":
            res = c1 & c2
        else: raise Exception("!")
        currStackElms.append([out, res])
    if len(currStackElms) == 0:
        break
    for el in currStackElms:
        idxToRemove = 0
        for i,k in enumerate(unknw):
            if k[3] == el[0]:
                idxToRemove = i
                break
        unknw.pop(idxToRemove)
digits = ""
known.sort()
for el in known:
    if el[0][0] == "z":
        el1 = el[1]
        digits = str(el1) +digits
print("x:", xvals)
print("y:",yvals)
print("z:",digits)
res = int(digits,2)
print(res)
