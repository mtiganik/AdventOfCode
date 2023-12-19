f = open("input.txt").read().splitlines()


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

workflows = []
start =0 
for x in f:
  if x == "":
    break
  workflow = getWorkflow(x.replace("}",""))
  if workflow[0] == "in":
    start = workflow
  workflows.append(workflow)


def getFlowById(flowId):
  for flow in workflows:
    if flow[0] == flowId: return flow
  raise TypeError("shouldnt get here")
cmdIdxs = ["x","m","a","s"]
resRanges = []

def getRes(currCoord, flow):
  letter, gt, valToCmp =cmdIdxs.index(flow[0][0]), flow[0][1], flow[1]
  currRange = currCoord[letter]
  if valToCmp in currRange:
    if flow[2] == 'A': return resRanges.append(currCoord)
    elif flow[2] == 'R': return
    range1,range2 = currCoord,currCoord
    range1[letter], range2[letter] = range(currRange[0],valToCmp), range(valToCmp, currRange[-1])
    if gt == '<':
        getRes(range1,getFlowById(flow[2])[1])
        if isinstance(flow[3], str): getRes(range2,getFlowById(flow[3]))
        else: getRes(range2, flow[3])
    elif gt == '>':
        getRes(range2,getFlowById(flow[2])[1])
        if isinstance(flow[3], str): getRes(range1,getFlowById(flow[3]))
        else: getRes(range2, flow[3])
  else:
    if isinstance(flow[3], str):
      if flow[3] == "A": return resRanges.append(currCoord)
      elif flow[3] == "R": return
      else: getRes(currCoord, getFlowById(flow[3])[1])
    else: getRes(currCoord, flow[3])

#   if gt == '<':
  
  
startRange = [range(1,4000), range(1,4000), range(1,4000), range(1,4000)]
getRes(startRange, getFlowById("in")[1])
# getRes([1,1,1,1],getFlowById("in"))

