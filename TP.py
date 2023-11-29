kantite_Note=int( input("antre vale not ou vle a: ")  )
List_note=[]
konte=0
while(konte<kantite_Note):
    note=int(input("antre not yo: "))
    List_note.append(note)
    konte=konte+1
mwayen=float(sum(List_note)/kantite_Note)
print("rezilta mwayen se: ",mwayen)
if (mwayen>=90):
    print("A")
elif(mwayen>=80 and mwayen<90):
    print("B")
elif(mwayen >=70 and mwayen<80):
    print("C")
elif(mwayen >=60 and mwayen<70):
    print("D")
elif(mwayen<60):
    print("F")

