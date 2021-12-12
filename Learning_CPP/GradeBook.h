#include <string> // Uses standard string class

/*
	GradeBook class definition presents the public interface of the class.
	Member-function definitions appear in GradeBook.cpp.
*/

class GradeBook
{
public:
	explicit GradeBook(std::string);    // Constructor initialize courseName
	void setCourseName(std::string);	// Sets the course name
	std::string getCourseName() const;  // Gets the course name
	void displayMessage() const;		// Displays a welcome message

private:
	std::string courseName;				// Course name for this GradeBook
};// END