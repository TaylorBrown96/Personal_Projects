# Author: Taylor J. Brown
# Date: 13OCT23

.data 

initalize_balance: .asciiz "Please indicate how much money you're staring with (Whole dollar amount no cents): "
init_error: .asciiz "You've entered an invalid amount!\n\n"

menu_str: .asciiz "\nMENU\n1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit\n"
user_menu_choice: .asciiz ":>"
option_error: .asciiz "\nInvalid option!\n"

withdrawal_str: .asciiz "\nHow much would you like to withdraw?\n:>"
withdraw_error: .asciiz "Insufficient funds! Please enter a valid amount.\n"
deposit_str: .asciiz "\nHow much would you like to deposit?\n:>"
new_balance_str: .asciiz "\nYour new balance is: $"
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
	
	blez $t0, mainError
	j menu
	
	
mainError:
	# Prints the error and sends the pointer back to the main subroutine
	li $v0,4
	la $a0, init_error
	syscall
	
	j main
	
	
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
	beq $t5, $t1, withdraw
	beq $t5, $t2, deposit
	beq $t5, $t3, balanceProbe
	beq $t5, $t4, end
	
	# No valid option
	li $v0, 4
	la $a0, option_error
	syscall
	# Reloads the menu
	j menu


withdraw:
	# Display the withdrawal prompt
	li $v0, 4
	la $a0, withdrawal_str
	syscall  
	
	# Store user's input
	li $v0, 5 
	syscall 
	move $t5, $v0
	
	# Checks to see if the entered withdraw amount would sent the account into the negatives
	sub $t6, $t0, $t5
	addi $t6, $t6, 1
	blez $t6, withdrawError
	
	# Subtract the amount from the users balance and prints the new balance
	sub $t0, $t0, $t5
	jal newBalance

	# Returns to menu loop
	j menu
	
	
withdrawError:
	# Prints the error and sends the pointer back to the withdraw subrutine
	li $v0,4
	la $a0, withdraw_error
	syscall
	
	j withdraw
	
deposit:
	# Display the deposit prompt
	li $v0, 4
	la $a0, deposit_str
	syscall  
	
	# Store user's input
	li $v0, 5 
	syscall 
	move $t5, $v0
	
	# Add the amount to the users balance and prints the new balance
	add $t0, $t0, $t5 
	jal newBalance

	# Returns to menu loop
	j menu
	

newBalance:
	# Prints the new balance
	li $v0, 4
	la $a0, new_balance_str
	syscall
	li $v0, 1
	add $a0, $zero, $t0
	syscall
	
	# Return to caller
	jr $ra
	
	
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
