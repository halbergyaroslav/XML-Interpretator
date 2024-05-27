import sys
import lexer
import tree
import converter


def main():
    filename = sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    tokens = lexer.lexer(characters)
    '''for token in tokens:
        print(token)'''
        
    ac_tree = tree.parser(tokens)
    
    '''for tac in ac_tree.tacs:
        print(f'tac opcode: {tac.opcode}')
        print(f'tac order: {tac.order}')
        print(f'tac dst type: {tac.dst.type}, tac dst value: {tac.dst.value}')
        if tac.src1: print(f'tac src1 type: {tac.src1.type}, tac src1 value: {tac.src1.value}')
        else: print(f'tac src1: {tac.src1}')
        if tac.src2:print(f'tac src2 type: {tac.src2.type}, tac src2 value: {tac.src2.value}')
        else: print(f'tac src2: {tac.src2}')
        print()'''
        
    ac_tree = converter.create_order(ac_tree)
    filename = converter.create_file(ac_tree)
    converter.compile_file(filename)
    

if __name__ == '__main__':
    main()