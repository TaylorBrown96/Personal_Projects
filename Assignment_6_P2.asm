# Author: Taylor J. Brown
# Date: 12OCT23

.data 
initalize_balance: .asciiz "Please indicate how much money you're staring with (Whole dollar amount no cents): "

menu_str: .asciiz "\nMENU\n1. Credit\n2. Debit\n3. Check Balance\n4. Exit\n"
user_menu_choice: .asciiz ":>"
option_error: .asciiz "\nInvalid option!\n"

credit_str: .asciiz "\n"
debit_str: .asciiz "\n"
balance_str: .asciiz "\nYour current balance is: $"
exit_prompt: .asciiz "Thank you for banking with us!\n"

.text 
.globl main # Makes a symbol globally visible to the linker.  

main:
	# Ask the user for an initalization dollar amount
	li $v0,4
	la $a0, initalize_balance
	syscall

	# Store users input
	li $v0, 5
	syscall 
	move $t0, $v0
	
	
menu:
	# Display the menu and the input prompt line decorator 
	li $v0, 4
	la $a0, menu_str
	syscall 
	la $a0, user_menu_choice
	syscall 
	
	# Store user choice
	li $v0, 5 
	syscall 
	move $t5, $v0
	
	# Initalize menu choice values
	addi $t1, $zero, 1
	addi $t2, $zero, 2
	addi $t3, $zero, 3
	addi $t4, $zero, 4
	
	# Decision processing
	beq $t5, $t1, credit
	beq $t5, $t2, debit
	beq $t5, $t3, balanceProbe
	beq $t5, $t4, end
	
	# No valid option
	li $v0, 4
	la $a0, option_error
	syscall
	# Reloads the menu
	j menu


credit:
	# Returns to menu loop
	j menu
	
	
debit:
	# Returns to menu loop
	j menu
	
	
balanceProbe:
	# Prints the balance prompt and the total inside "Bank account" ($t0)
	li $v0, 4
	la $a0, balance_str
	syscall
	li $v0, 1
	add $a0, $zero, $t0
	syscall 

	# Returns to menu loop
	j menu
	
	
# DO NOT CHANGE	
end:
	# Displays exit prompt
	li $v0,4
	la $a0, exit_prompt 
	syscall

	# Terminates the program
	li $v0, 10
	syscall  
