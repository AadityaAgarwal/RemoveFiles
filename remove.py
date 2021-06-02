import time,shutil,os
path=input("Enter the path: ")
days=input("Enter the number of days: ")
timeCalc=time.time()
check=os.path.exists(path)
listFile=os.listdir(path)

for file in listFile:
    name,ext=os.path.splitext(file)

    if(check==True) :
      walk= os.walk(path)
      os.path.join(path)
      ctime=os.stat(path).st_ctime
      print(ctime)

      if(ext==' '):
          shutil.rmtree()
      else:
          os.remove(file)    
    else:
         print("Path not found!")