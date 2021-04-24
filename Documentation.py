import docx

def submit(a,b,c,d,e,f,g,h,i,j,k):
    doc=docx.Document()
    school1=a
    school2=b
    school3=c
    school4=d
    student1=e
    student2=f
    student3=g
    student4=h
    student5=i
    student6=j
    teacher1=k
    s="School Details\n"
    s=s+"School: "+school1+"\n"
    s=s+"Address: "+school2+", "+school3+": "+school4+"\n"
    s=s+"\nStudent Details\n"
    s=s+"Name: "+student1+"\n"
    s=s+"Admission Number: "+student2+"\n"
    s=s+"Gender: "+student3+"\n"
    s=s+"Nationality: "+student4+"\n"
    s=s+"DOB: "+student5+"\n"
    s=s+"Date of Leaving School: "+student6+"\n"
    s=s+"Remarks: "+teacher1+"\n\n"
    s=s+"Date\tSignature"
    doc.add_paragraph(s)
    doc.save("Doc.docx")
