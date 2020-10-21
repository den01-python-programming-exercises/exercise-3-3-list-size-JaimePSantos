def main():
    #write your code below this line
    strList = []
    while(True):
      str = input()
      if(str==""):
        break
      strList.append(str)
    print("In total: %s"%len(strList))

if __name__ == '__main__':
    main()
