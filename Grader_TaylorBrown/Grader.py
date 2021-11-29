# Taylor J. Brown
# 14NOV21
# This program takes in grades from txt files and calculates you actuall grade


"""
CHANGES
_____________________________________________________________
- Took out string conversion and used the .2f format to print averages and for writing to .txt file
- Calculated Overall grade with weighted totals for better accuracy when calculating grade
- Shortened displayed numbers to the hundredth decimal place for better readability
"""


def main():
# Declares all category lists for files to write to
    LTL = []
    QUIZ = []
    SAM_PROJ = []
    SAM_CAP = []
    SAM_TEXT = []
    SAM_EXAM = []
    TEST = []
    
      
# LTL
    with open('LTL.txt', 'r') as FILE:
        for line in FILE:
            LTL.append(line.rstrip('\n'))
             
    
# QUIZ
    with open('QUIZ.txt', 'r') as FILE:
        for line in FILE:
            QUIZ.append(line.rstrip('\n'))
             
         
# SAM_PROJ     
    with open('SAM_PROJ.txt', 'r') as FILE:
        for line in FILE:
            SAM_PROJ.append(line.rstrip('\n'))
                        
        
# SAM_CAP    
    with open('SAM_CAP.txt', 'r') as FILE:
        for line in FILE:
            SAM_CAP.append(line.rstrip('\n'))
             
    
# SAM_TEXT            
    with open('SAM_TEXT.txt', 'r') as FILE:
        for line in FILE:
            SAM_TEXT.append(line.rstrip('\n'))
             
    
# SAM_EXAM
    with open('SAM_EXAM.txt', 'r') as FILE:
        for line in FILE:
            SAM_EXAM.append(line.rstrip('\n'))
             
    
# TEST
    with open('TEST.txt', 'r') as FILE:
        for line in FILE:
            TEST.append(line.rstrip('\n'))
                
    
# Pops lowest grade from quizes
    QUIZ.sort(reverse=False)
    QUIZ.pop(0)
    
    
# Converts lists from string objects to integers
    i_LTL = change_to_int(LTL)
    i_QUIZ = change_to_int(QUIZ) 
    i_SAM_PROJ = change_to_int(SAM_PROJ)
    i_SAM_CAP = change_to_int(SAM_CAP)
    i_SAM_TEXT = change_to_int(SAM_TEXT)
    i_SAM_EXAM = change_to_int(SAM_EXAM)
    i_TEST = change_to_int(TEST)
    
    
# Gets the average for each list category
    LTL_averages = cal_average(i_LTL)
    QUIZ_averages = cal_average(i_QUIZ)
    SAM_PROJ_averages = cal_average(i_SAM_PROJ)
    SAM_CAP_averages = cal_average(i_SAM_CAP)
    SAM_TEXT_averages = cal_average(i_SAM_TEXT)
    SAM_EXAM_averages = cal_average(i_SAM_EXAM)
    TEST_averages = cal_average(i_TEST)
   
    
# Gets the weighted total for each grade (Weighted Average of Learner to Learner Assignments(10.00%), 
# Quizzes(20.00%), SAM Projects(20.00%), SAM Capstone Projects(10.00%), SAM Textbook Projects(10.00%), SAM Exams(15.00%), Tests(15.00%))
    W_LTL_averages = LTL_averages            * .1  #10%
    W_QUIZ_averages = QUIZ_averages          * .2  #20%
    W_SAM_PROJ_averages = SAM_PROJ_averages  * .2  #20%
    W_SAM_CAP_averages = SAM_CAP_averages    * .1  #10%
    W_SAM_TEXT_averages = SAM_TEXT_averages  * .1  #10%
    W_SAM_EXAM_averages = SAM_EXAM_averages  * .15 #15%
    W_TEST_averages = TEST_averages          * .15 #15%
    
    
# Calculates the overall grade with the weighted totals
    OVERALL_averages = W_LTL_averages + W_QUIZ_averages + W_SAM_PROJ_averages + W_SAM_CAP_averages + W_SAM_TEXT_averages + W_SAM_EXAM_averages + W_TEST_averages
    

# Displays grade average for each category
    print("L2L {0:.2f}".format(LTL_averages))
    print("Quiz {0:.2f}".format(QUIZ_averages))
    print("SAM Proj {0:.2f}".format(SAM_PROJ_averages))
    print("SAM Cap {0:.2f}".format(SAM_CAP_averages))
    print("SAM Text {0:.2f}".format(SAM_TEXT_averages))
    print("SAM Exam {0:.2f}".format(SAM_EXAM_averages))
    print("Test {0:.2f}".format(TEST_averages))
    print("OVERALL {0:.2f}".format(OVERALL_averages))
    

# Creates a new files named grades.txt with all the print outs displayed
    with open("grades.txt","w+") as f:
        f.write("L2L" + "      " + "{0:.2f}".format(LTL_averages) + '\n')
        f.write("Quiz" + "     " + "{0:.2f}".format(QUIZ_averages) + '\n')
        f.write("SAM Proj" + " " + "{0:.2f}".format(SAM_PROJ_averages) + '\n')
        f.write("SAM Cap" + "  " + "{0:.2f}".format(SAM_CAP_averages) + '\n')
        f.write("SAM Text" + " " + "{0:.2f}".format(SAM_TEXT_averages) + '\n')
        f.write("SAM Exam" + " " + "{0:.2f}".format(SAM_EXAM_averages) + '\n')
        f.write("Test" + "     " + "{0:.2f}".format(TEST_averages) + '\n')
        f.write("OVERALL" + "  " + "{0:.2f}".format(OVERALL_averages) + '\n')
                  
            
def change_to_int(lst):
    """
        Takes in a list and converts each object into a Integer
    """
    tmp_lst = []
    for element in lst:
        tmp_lst.append(int(element))
    return tmp_lst

         
def cal_average(lst):
    """
        Calculates the average of a given list
    """
    return sum(lst) / len(lst)

    
main()
