import os


def create_order(rootnode):
    dict_tacs = {}
    for tac in rootnode.tacs:
        dict_tacs[tac.order] = tac
    sorted_dict_tacs = dict(sorted(dict_tacs.items()))
    
    rootnode.tacs = []
    for key in sorted_dict_tacs.keys():
        rootnode.tacs.append(sorted_dict_tacs[key])
        
    return rootnode


def create_file(rootnode):
    filename = str(rootnode.name[1:-1:]).replace(' ', '_') + '.py'
    file = open(filename, 'w')
    
    for tac in rootnode.tacs:
        if tac.opcode == '"MOV"':
            file.write(f'{tac.dst.value} = {tac.src1.value}\n')
        
        elif tac.opcode == '"ADD"':
            file.write(f'{tac.dst.value} = {tac.src1.value} + {tac.src2.value}\n')
            
        elif tac.opcode == '"SUB"':
            file.write(f'{tac.dst.value} = {tac.src1.value} - {tac.src2.value}\n')
            
        elif tac.opcode == '"MUL"':
            file.write(f'{tac.dst.value} = {tac.src1.value} * {tac.src2.value}\n')
            
        elif tac.opcode == '"DIV"':
            file.write(f'{tac.dst.value} = {tac.src1.value} // {tac.src2.value}\n')
            
        elif tac.opcode == '"READINT"':
            file.write(f'{tac.dst.value} = int(input())\n')
            
        elif tac.opcode == '"READSTR"':
            file.write(f'{tac.dst.value} = input()\n')
            
        elif tac.opcode == '"PRINT"':
            if tac.dst.type == '"integer"' or tac.dst.type == '"variable"': file.write(f'print({tac.dst.value}, end=\'\')\n')
            else: file.write(f'print(\'{tac.dst.value}\', end=\'\')\n')
            
        elif tac.opcode == '"PRINTLN"':
            if tac.dst.type == '"integer"' or tac.dst.type == '"variable"': file.write(f'print({tac.dst.value})\n')
            else: file.write(f'print(\'{tac.dst.value}\')\n')
            
        elif tac.opcode == '"LABEL"':
            print(10)
            
        elif tac.opcode == '"JUMP"':
            print(11)
            
        elif tac.opcode == '"JUMPIFEQ"':
            print(12)
            
        elif tac.opcode == '"JUMPIFLT"':
            print(13)
            
        elif tac.opcode == '"CALL"':
            print(14)
            
        elif tac.opcode == '"RETURN"':
            print(15)
            
        elif tac.opcode == '"PUSH"':
            print(16)
            
        elif tac.opcode == '"POP"':
            print(17)
            
        elif tac.opcode == '"CONCAT"':
            pass
                 
    file.close()
    
    return filename     
    

def compile_file(filename):
    command = 'python ' + filename
    os.system(command)