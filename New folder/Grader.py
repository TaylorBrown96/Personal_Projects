# Taylor J. Brown
# 14NOV21
# This program takes in grades from txt files and calculates you actuall grade


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
    
    
# Apperds each average to overall
    overall = [ LTL_averages,
                QUIZ_averages,
                SAM_PROJ_averages,
                SAM_CAP_averages,
                SAM_TEXT_averages,
                SAM_EXAM_averages,
                TEST_averages]
    
    
# Calculates the overall grade
    OVERALL_averages = cal_average(overall)
    
    
# Changes back to str so it can write to file 
    S_LTL_averages = change_to_str(LTL_averages)
    S_QUIZ_averages = change_to_str(QUIZ_averages)
    S_SAM_PROJ_averages = change_to_str(SAM_PROJ_averages)
    S_SAM_CAP_averages = change_to_str(SAM_CAP_averages)
    S_SAM_TEXT_averages = change_to_str(SAM_TEXT_averages)
    S_SAM_EXAM_averages = change_to_str(SAM_EXAM_averages)
    S_TEST_averages = change_to_str(TEST_averages)
    S_OVERALL_averages = change_to_str(OVERALL_averages)
    
    
# Displays grade average for each category
    print("L2L",S_LTL_averages)
    print("Quiz",S_QUIZ_averages)
    print("SAM Proj",S_SAM_PROJ_averages)
    print("SAM Cap",S_SAM_CAP_averages)
    print("SAM Text",S_SAM_TEXT_averages)
    print("SAM Exam",S_SAM_EXAM_averages)
    print("Test",S_TEST_averages)
    print("OVERALL",S_OVERALL_averages)


# Creates a new files named grades.txt with all the print outs displayed
    with open("grades.txt","w+") as f:
        f.write("L2L" + "      " + S_LTL_averages + '\n')
        f.write("Quiz" + "     " + S_QUIZ_averages + '\n')
        f.write("SAM Proj" + " " + S_SAM_PROJ_averages + '\n')
        f.write("SAM Cap" + "  " + S_SAM_CAP_averages + '\n')
        f.write("SAM Text" + " " + S_SAM_TEXT_averages + '\n')
        f.write("SAM Exam" + " " + S_SAM_EXAM_averages + '\n')
        f.write("Test" + "     " + S_TEST_averages + '\n')
        f.write("OVERALL" + "  " + S_OVERALL_averages + '\n')
        
            
            
def change_to_str(var):
    """
        Takes the averages and changes it back to a string so the program can write to grades.txt
    """
    temp_var = ''
    temp_var += str(var)
    return temp_var
    
    
            
def change_to_int(lst):
    """
        Takes in a list and converts each object into a string
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