bf_code = ""
while True:
    line = input()
    if not line:
        break
    bf_code += line


user_input = []

loop_stack = []
memory = [0]
mem_pointer = 0
bf_pointer = 0

while (bf_pointer < len(bf_code)):
    bf_op = bf_code[bf_pointer]
    val = memory[mem_pointer]

    if bf_op == "+":
        if val == 255:
            val = 0
        else:
            val += 1
        memory[mem_pointer] = val

    elif bf_op == "-":
        if val == 0:
            val = 255
        else:
            val -= 1
        memory[mem_pointer] = val

    elif bf_op == ">":
        if (mem_pointer == len(memory)-1):
            memory.append(0)
            
        mem_pointer += 1

    elif bf_op == "<":
        mem_pointer -= 1

    elif bf_op == ",":
        if(user_input == []):
            user_input = list(input())
        val = ord(user_input.pop(0))
    
    elif bf_op == ".":
        print(chr(val), end = "")

    elif bf_op == "[":
        loop_stack.append(bf_pointer)
        if(val == 0):
            while(len(loop_stack) != 0):
                bf_pointer += 1
                if bf_code[bf_pointer] == "]":
                    loop_stack.pop()
                elif bf_code[bf_pointer] == "[":
                    loop_stack.append(bf_pointer)   

    elif bf_op == "]":
        if(val != 0):
            bf_pointer = loop_stack[-1]
        else:
            loop_stack.pop()

    
    bf_pointer += 1
