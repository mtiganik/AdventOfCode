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
# workflow = ["px", [5,2006,"qkq",[4,2090,"A","rfg"]]],
# ["pv",[5,1716,"R","A"]],
# ["lnx", [3,1548,"A","A"]],
# ["rfg",[8,537,"gd",[2,2440,"R","A"]]]

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

def getComand(str):
  str = str.replace("{","").replace("}","")
  res = []
  elems = str.split(",")
  for x in elems:
    val = x.split("=")[1]
    res.append(int(val))
  return res

workflows = []
cmnds = []
endOfWorkFlows = False
start =0 
for x in f:
  if x == "":
    endOfWorkFlows = True
    continue
  if not endOfWorkFlows:
    workflow = getWorkflow(x.replace("}",""))
    if workflow[0] == "in":
      start = workflow
    workflows.append(workflow)
  else:
    cmd = getComand(x)
    cmnds.append(cmd)

def getFlowById(flowId):
  for flow in workflows:
    if flow[0] == flowId: return flow
  raise TypeError("shouldnt get here")

cmdIdxs = ["x","m","a","s"]
def getRatingResult(workflow,cmd):
  valToCompare,comparator = workflow[1][0][0], workflow[1][0][1]
  indexOfElem =  cmdIdxs.index(valToCompare)
  if comparator == '<' and cmd[indexOfElem] < workflow[1][1]: inRating = True
  elif comparator == '<' and cmd[indexOfElem] > workflow[1][1]: inRating = False
  elif comparator == '>' and cmd[indexOfElem] > workflow[1][1]: inRating = True
  elif comparator == '>' and cmd[indexOfElem] < workflow[1][1]: inRating = False

  if inRating:
    if workflow[1][2] == "A": return True
    elif workflow[1][2] == "R": return False
    else:
      newWorkflow = getFlowById(workflow[1][2])
      return getRatingResult(newWorkflow, cmd)
  else:
    if workflow[1][3] == "A": return True
    elif workflow[1][3] == "R": return False
    else:
      falseWFlow = workflow[1][3]
      if isinstance(falseWFlow, str):
        newWorkflow = getFlowById(falseWFlow)
      else: newWorkflow = getFlowById(workflow[1][3][0])
      return getRatingResult(newWorkflow, cmd)


    print("a")

for cmd in cmnds:
  isAccepted = getRatingResult(start, cmd)
  print(isAccepted)