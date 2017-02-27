#!/usr/local/bin/python
#!/usr/bin/env python
import random
import datetime
current_date = datetime.datetime.now()
print current_date
 
#end_date = current_date + datetime.timedelta(days=7)
#print end_date






afile = open("sample.txt", "w" )

for i in range(0,336):
    end_date = current_date + datetime.timedelta(days=7)
    current_date = end_date
    line =str(current_date) +str("      ")+str(random.randint(1,5))+ str("     ")+str(random.randint(1, 100))
    afile.write(line +" " )
    print(line)

afile.close()
#to hold the terminal
raw_input("Press enter to exit ;)")

