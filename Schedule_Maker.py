class Section():
    def __init__(self, name, date, days, time, location, instructor):
        self.name = name
        self.date = date
        self.days = days
        self.time = time
        self.location = location
        self.instructor = instructor

def main():
    semester = []
    
    semesterName = input("What is the semester you are attending?: ")
    iterations = int(input("How many classes do you want to enter?: "))
    for _ in range(iterations):
        name = input("What is the classes name?: ")
        date = input("What is the date range for this class?: ")
        days = input("What days does this class meet?: ")
        time = input("What are the meeting times?: ")
        location = input("Where does the class take place?: ")
        instructor = input("Who is the instructor for this class?: ")

        section = Section(name, date, days, time, location, instructor)
        semester.append(section)
        
    file = open("Schedule.txt", "w")
    file.write(f'{semesterName: ^134}' + '\n')
    file.write(f'{"Class Name": <44}| {"Date Range": <17}| {"Meeting days": <17}| {"Meeting Times": <18}| {"Meeting Location": <18}| {"Instructor": <17}' + '\n')
    file.write("-" * 144 + "\n")
    
    for x in range(iterations):
        file.write(f'{semester[x].name: <44}| {semester[x].date: <17}| {semester[x].days: <17}| {semester[x].time: <18}| {semester[x].location: <18}| {semester[x].instructor: <17}' + "\n")
    file.close()

main()