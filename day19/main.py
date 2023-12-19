f = open("input.txt").read().splitlines()

#x< : 1
#x> : 2
#m> : 3
#m< : 4
#a< : 5
#a> : 6
#s< : 7
#s> : 8
ratings = []
workflow = ["px", [5,2006,"qkq",[4,2090,"A","rfg"]]],
["pv",[5,1716,"R","A"]],
["lnx", [3,1548,"A","A"]],
["rfg",[8,537,"gd",[2,2440,"R","A"]]]
workflows = []

def getWorkflowElement(str):
  cat = str[:2:]
  num = int(str.split(":")[0].split(cat)[1])
  str = str[str.find(":")+1:]
  ifTrue =str.split(",")[0]
  ifFalse = str[str.find(",")+1:]
  if  not [ele for ele in ["<",">"] if(ele in ifFalse)]:
    return [cat,num,ifTrue,ifFalse]
  else:
    return [cat, num, ifTrue,getWorkflowElement(ifFalse)]
def getWorkflow(str):
  name,cmd = str.split("{")
  return [name, getWorkflowElement(cmd)]


endOfWorkFlows = False
for x in f:
  if x == "":
    endOfWorkFlows = True
  if not endOfWorkFlows:
    workflow = getWorkflow(x.replace("}",""))
    print(workflow)
