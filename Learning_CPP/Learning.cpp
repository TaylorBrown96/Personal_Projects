// This program is for learning C++

#include <iostream>
#include "GradeBook.h"
using namespace std;

GradeBook::GradeBook(string name) : courseName(name)
{
	setCourseName(name);
}

void GradeBook::setCourseName(string name)
{
	if (name.size() <= 25)
		courseName = name;
	if (name.size() > 25)
	{
		courseName = name.substr(0, 25);
		cerr << "Name \"" << name << "\" exceeds maximum length (25).\n" << "Limiting courseName to first 25 characters.\n" << endl;
	}
}

string GradeBook::getCourseName() const
{
	return courseName;
}

void GradeBook::displayMessage() const
{
	cout << "Welcome to the grade book for\n" << getCourseName() << "!" << endl;
}


int main()
{
	GradeBook gradeBook1("CS101 C++ Programming");
	GradeBook gradeBook2("CS102 C++ Data Structures");

	cout << "gradeBook1 created for course: " << gradeBook1.getCourseName()
		<< "\ngradeBook2 created for course: " << gradeBook2.getCourseName()
		<< endl;
}
