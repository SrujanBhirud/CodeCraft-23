import sys
import os

def run_brainfuck(bf_code,user_input):
    user_input = list(user_input)

    loop_stack = []
    loop_table = {}
    memory = [0]
    mem_pointer = 0
    output = ""
    
    for bf_pointer, bf_op in enumerate(bf_code):
        if bf_op == "[":
            loop_stack.append(bf_pointer)
        elif bf_op == "]":
            start = loop_stack.pop()
            loop_table[start] = bf_pointer
            loop_table[bf_pointer] = start

    bf_pointer = 0

    while (bf_pointer < len(bf_code)):
        bf_op = bf_code[bf_pointer]
        val = memory[mem_pointer]

        if bf_op == "+":
            val = (val + 1) %256
            memory[mem_pointer] = val

        elif bf_op == "-":
            val = (val - 1) %256
            memory[mem_pointer] = val

        elif bf_op == ">":
            if (mem_pointer == len(memory)-1):
                memory.append(0)
                
            mem_pointer += 1

        elif bf_op == "<":
            mem_pointer -= 1

        elif bf_op == ",":
            if(user_input == []):
                break
            val = ord(user_input.pop(0))
            memory[mem_pointer] = val
        
        elif bf_op == ".":
            output += chr(val)

        elif bf_op == "[":
            if(val == 0):
                bf_pointer = loop_table[bf_pointer]  

        elif bf_op == "]":
            if(val != 0):
                bf_pointer =loop_table[bf_pointer]

        
        bf_pointer += 1
    return output

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"Error: File '{filename}' not found.")
    except IndexError:
        print("Error: Please provide only the filename of the BrainFuck interpreter and your bf code")
        print("Usage: python <bf_interpreter.py> <filename.txt>")
    except:
        print("Usage: python <bf_interpreter.py> <filename.txt>")
    else:
        with open(filename, 'r') as file:
            bf_code = file.read()
            print(run_brainfuck(bf_code,input("Enter user input. Press Enter to skip: ")))

