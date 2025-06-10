def split(paren:str):
    left = 0
    right = 0
    output=[]
    lastIdx = 0
    for p in paren:
        if p =='(':
            left+=1
        else:
            right+=1
        if left ==right:
            output.append(paren[lastIdx:right+left])
            lastIdx= right+left
    return output

def main():
    print(split("((())())(()(()()))"))

main()
        