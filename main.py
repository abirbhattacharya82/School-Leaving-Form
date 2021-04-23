import docx
doc=docx.Document()
print("School Details: ")
school1=input("Enter the Name of the School ")
school2=input("Enter the name of the ROAD ")
school3=input("Enter the name of City/District ")
school4=input("Enter the pincode ")
print("-------------------------------------------------------------------")
print("Students Detail ")
student1=input("Enter the Full Name of the Student ")
student2=input("Enter the Admission Number of the Student ")
student3=input("Enter the Gender of the Student ")
student4=input("Enter the Nationality of the Student ")
student5=input("Enter the Date of Birth of the Student in DD/MM/YYYY ")
student6=input("Date of Leaving School ")
print("-------------------------------------------------------------------")
print("Teacher's Section ")
teacher1=input("Enter the Remarks ")
print("-------------------------------------------------------------------")

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
