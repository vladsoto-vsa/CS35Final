"""
This program opens the file students.txt and reads it in
to a list of lists
"""
def main():
    roster = readFile("students.txt")
    print(roster)
    print(len(roster), "students in the class")
    for i in range(2020,2024):
        n = countStudentsInYear(roster, i)
        print(n, "students graduating in", i)




def countStudentsInYear(roster, year):
    """
    Parameters:
    roster is a list of student lists containing lastname, firstname
    , and classyear
    year is an integer
    Returns:
    count for number of students with that classyear
    """
    count = 0
    for i in range(len(roster)):
        if roster[i][2] == year:
        count = count + 1
    return count


def readFile(filename):
    """
    Parameters:
    filename a string that gives the file's name
    Returns:
    List of lists of the files contents
    """
    ls = []
    fp = open(filename, "r")

    for line in fp:
        line = line.strip()
        studentData = line.split(",")
        studentData[2] = int(studentData[2])
        ls.append(studentData)

    fp.close()
    return ls

main()
