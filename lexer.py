import sys
import re

token_exprs = [
    (r'[ \n\t]+', None),
    (r'#[^\n]*', None),
    (r'<?xml', 'XMLTAG'),
    (r'version', 'XMLVERSION'),
    (r'encdoing', 'XMLENCODING'),
    (r'<program', 'BEGINPROGRAM'),
    (r'</program', 'ENDPROGRAM'),
    (r'<tac', 'BEGINTAC'),
    (r'</tac>', 'ENDTAC'),
    (r'<dst', 'BEGINDST'),
    (r'</dst>', 'ENDDST'),
    (r'<src1', 'BEGINSRC1'),
    (r'</src1>', 'ENDSRC1'),
    (r'<src2', 'BEGINSRC2'),
    (r'</src2>', 'ENDSRC2'),
    (r'>', None),
    (r'[A-Za-z][A-Za-z0-9_]*', 'ATTRIBUTENAME'),
    (r'=', 'EQUALSIGN'),
    (r'"[^"]*"', 'ATTRIBUTEVALUE'),
    (r"'[^']*'", 'ATTRIBUTEVALUE'),
    (r'[^<>&]+', 'CONTENT'),
    (r'&[A-Za-z]+;', 'ENTITYINVOCATION'),
]

def lexer(characters):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens