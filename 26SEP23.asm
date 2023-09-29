.data 
prompt_str1: .asciiz "How many feet?: "
out_str: .asciiz "Converted to inches: "

.text 

# Prints the question
li $v0, 4
la $a0, prompt_str1
syscall

# Stores the feet entered by the user
li $v0, 5
syscall
move $t0, $v0

# Converts the enter feet into inches
jal FeetToInches

# Prints the number of inches
li $v0, 4
la $a0, out_str
syscall

li $v0, 1
add $a0, $zero, $t1
syscall

# Terminates the program
j Done

FeetToInches:
	mul  $t1, $t0, 12
	jr $ra

Done:
	# Dont change
	li $v0,10
	syscall
