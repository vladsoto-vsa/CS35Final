"""
This program will read in a CSV file of how a student did on a lab and
create one summary file per student that can be emailed to them.
"""

def main():
    title = "Lab6: Blobify"
    headers, students = readGrades("labData.csv")
    print("Read in data for", len(students), "students")
    for i in range(len(students)):
        processStudent(title, headers, students[i])

def readGrades(filename):
    """
    Purpose: Read in a file containing comma separated values representing
    a spreadsheet of data about students.
    Parameter: The filename containing the data.
    Returns: Two lists--the first contains strings representing the headers
    for each column of the spreadsheet and the second contains sublists
    representing the scores and comments for each student.
    """
    fp = open(filename, "r")
    headers = fp.readline().strip().split(",")
    students = []
    for line in fp:
        student = line.strip().split(",")
        print("STUDENT")
        students.append(student)
    fp.close()
    return headers, students

def processStudent(title, headers, student):
    """
    Purpose: Write a summary file for each student to be emailed to them.
    Parameters: string title, list of strings headers, lists of lists students
    Returns: None
    """
    username = student[0]
    print("processing", username)
    filename = username + "_lab"
    fp = open(filename, "w")
    fp.write(title+"\n\n")
    for i in range(len(headers)):
        fp.write("%s: %s\n" % (headers[i], student[i]))
    fp.write("\n")
    fp.close()
    email = username + "@swarthmore.edu"
    # can email each file to the appropriate student

main()
