from nodes import *


def create_directories_structure():
    directories = LinkedList()
    
    directories.insert('none')
    directories.insert('program')
    directories.insert('tac')
    directories.insert('src')
    
    return directories


def create_src(src):
    SRC = Src()
    pointer = src.head
    SRC.type = pointer.data
    pointer = pointer.next
    SRC.value = pointer.data
    
    if pointer.next:
        pointer = pointer.next
        SRC.value += pointer.data
    
    return SRC


def create_tac(tac):
    TAC = Node()
    pointer = tac.head
    TAC.opcode = pointer.data
    pointer = pointer.next
    TAC.order = pointer.data
    pointer = pointer.next
    TAC.dst = pointer.data
    
    if pointer.next:
        pointer = pointer.next
        TAC.src1 = pointer.data
    
    if pointer.next:
        pointer = pointer.next
        TAC.src2 = pointer.data
    
    return TAC


def parser(tokens):    
    current_directory = create_directories_structure().head
    flag = False
    
    for token in tokens:
        if 'BEGIN' in token[1]:
            current_directory = current_directory.next
            
            if current_directory.data == 'program':
                rootnode = RootNode([])
                
            elif current_directory.data == 'tac':
                tac = LinkedList()
            
            else:
                src = LinkedList()
                
        elif 'END' in token[1]:
            if current_directory.data == 'tac':
                TAC = create_tac(tac)
                rootnode.tacs.append(TAC)
            
            elif current_directory.data == 'src':
                SRC = create_src(src)             
                tac.insert(SRC)
            
            current_directory = current_directory.prev
            
        else:
            if current_directory.data == 'program':
                if token[1] == 'ATTRIBUTEVALUE':
                    rootnode.name = token[0]
                    
            elif current_directory.data == 'tac':
                if token[1] == 'ATTRIBUTEVALUE':
                    tac.insert(token[0])
                    
            elif current_directory.data == 'src':
                if flag:
                    src.insert(token[0])
                    flag = False
                elif token[1] == 'ATTRIBUTEVALUE':
                    src.insert(token[0])   
                    if token[0] == '"variable"' or token[0] == '"string"': 
                        flag = True                                
                elif token[1] == 'CONTENT':
                    src.insert(token[0])
                    
    return rootnode
            
         
def main():    
    pass
    

if __name__ == '__main__':
    main()