.data
# User input prompts
prompt_str1: .asciiz "Enter your weight: "
prompt_str2: .asciiz "Enter you height: "

# Result output string
output_str1: .asciiz "Your BMI is: "
newline: .asciiz "\n"

# Weight category prompts
Underweight: .asciiz "You are underweight"
Normal_weight: .asciiz "You are at a normal weight"
Overweight: .asciiz "You are overweight"
Obesity: .asciiz "You are obese"

# Sets constants
x: .float 703.0
UW: .float 18.5 # Underweight
NW: .float 24.9 # Normal weight
OW: .float 29.9 # Overweight

.text
# Asks the user to input their weight
li $v0, 4
la $a0, prompt_str1
syscall 

# Stores their input
li $v0, 6
syscall
mov.s $f2, $f0

# Asks the user to input their height
li $v0, 4
la $a0, prompt_str2
syscall 

# Stores their input
li $v0, 6
syscall
mov.s $f3, $f0

# Calculates the BMI
jal CalcBMI
# Prints the BMI
jal PrintResults
# Prints the BMI category
jal PrintCategory
# Terminates the program
j Done

CalcBMI:
	# Loads the constant into coproc 1
	la $a1, x
	l.s $f1, ($a1)
	
	# Square height
	mul.s $f3, $f3, $f3
	# Weight divided by (height^2)
	div.s $f4, $f2, $f3
	# Multiply (weight / height^2) by 703
	mul.s $f3, $f1, $f4
	
	# Return
	jr $ra
	

PrintResults:
	# Prints the final result string
	li $v0, 4
	la $a0, output_str1
	syscall 
	# Prints BMI
	li $v0, 2
	mov.s  $f12, $f3
	syscall 
	# Return
	jr $ra
	
	
PrintCategory:
	# Prints a new line
	li $v0, 4       
	la $a0, newline       
	syscall
	
	# Loads category values
	la $a1, UW
	l.s $f4, ($a1)
	la $a1, NW
	l.s $f5, ($a1)
	la $a1, OW
	l.s $f6, ($a1)
	
	# Prints your BMI Category
	c.le.s   $f3, $f4
	bc1t PrintUnder
	c.le.s  $f3, $f5
	bc1t  PrintNormal
	c.le.s  $f3, $f6
	bc1t  PrintOver
	bc1f  PrintObese
	
	PrintUnder:
		li $v0, 4
		la $a0, Underweight
		syscall 
		jr $ra
	PrintNormal:
		li $v0, 4
		la $a0, Normal_weight
		syscall 
		jr $ra
	PrintOver:
		li $v0, 4
		la $a0, Overweight
		syscall 
		jr $ra
	PrintObese:
		li $v0, 4
		la $a0, Obesity
		syscall 
		jr $ra

Done:
	# DO NOT CHANGE
	li $v0,10
	syscall
