# hello world in assembly!

.data

str:
	.ascii "hello world\n"

.text

.globl _start

_start:
	# write() sys call description (code 4):
	# ssize_t write(int FD, const void *BUF, size_t COUNT)

	# Load arguments for write() system call:
	movl $4, %eax
	movl $1, %ebx
	movl $str, %ecx
	movl $12, %edx
	int $0x80

	# Close program with exit() system call (code 1):
	movl $1, %eax
	movl $0, %ebx
	int $0x80

	# --------------------------------------------------------------
	# Compilation steps:

	# Assemble source .s file:
	# as -o <assembled.o> <source.s>

	# Link assembled *.o file to executable:
	# ld -o <executable_file> <assembled.o>

