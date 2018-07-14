def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    
    inputList = L[:]
    tempRunInc = [inputList[0]]
    runInc = []

    tempRunDec = [inputList[0]]
    runDec = []

    sumLongestRun = 0
    
    for i in range(len(inputList)-1):
        
        if inputList[i] <= inputList[i+1]:
            tempRunInc.append(inputList[i+1])
            
            if len(tempRunInc) > len(runInc):
                runInc = tempRunInc[:]
        
        elif inputList[i] > inputList[i+1]:
            tempRunInc = [inputList[i+1]]

     
    
    for i in range(len(inputList)-1):
        if inputList[i] >= inputList[i+1]:
            tempRunDec.append(inputList[i+1])
            
            if len(tempRunDec) > len(runDec):
                runDec = tempRunDec[:]
        
        elif inputList[i] < inputList[i+1]:
            tempRunDec = [inputList[i+1]]
    
    
    if len(runInc) > len(runDec) :
        for ele in runInc:
            sumLongestRun += ele
            
    elif len(runInc) < len(runDec):
        for ele in runDec:
            sumLongestRun += ele
    else :
        for ele in L:
            if sum(runInc) == sum(runDec):
                for i in runInc:
                    sumLongestRun += i
                break
            if ele in runInc and ele not in runDec:
                for j in runInc:
                    sumLongestRun += j
                break
            elif ele in runDec and ele not in runInc:
                for k in runDec:
                    sumLongestRun += k
                break

        
    return sumLongestRun

    
    
    
    