
# This program is written to match students with the alumni for mentorship
# We need to download the data of each survey from qualtrics as xml file and name the student data as student.xml.xml and the alumni data as mentor.xml.xml

# The BeautifulSoup package parses the xml files
from bs4 import BeautifulSoup

# We have coded the experience value from 0-1 in the below code
experienceValues = {"":0,"less than 10 years" : 1, "10 to less than 15 years" :2, "15 to less than 20 years":3,"20 to less than 25 years":4,"25 years or more":5}

# bookedMentor is the variable that stores the first output for the below loop
bookedMentor = []

# We now parse the xml files and save it respectively as mentorXml and studentXml
mentorXml = BeautifulSoup(open("mentor.xml.xml"),'html.parser')
studentXml = BeautifulSoup(open("student.xml.xml"),'html.parser')

# The below is a simple loop command that matches the student with the alumni and prints the student and the respective mentors name
for student in studentXml.responses.find_all('response'):
    print(student.qid4_text.string)
    for mentor in mentorXml.responses.find_all('response'):
            if(mentor.qid10.string != None and mentor.qid7.string == "Yes" and experienceValues[mentor.qid10.string.lower()] > experienceValues[student.qid7.string.lower()] and student.qid10_1.string == mentor.qid6.string) and student.qid11_1.string == mentor.qid5.string:
                if not mentor.recipientemail.string in bookedMentor:
                    print("     " + mentor.recipientfirstname.string + " " + mentor.recipientlastname.string)
                    bookedMentor.append(mentor.recipientemail.string)
                    break
exitCode = input("thank you")



