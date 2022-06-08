from main import parser


def test_parser():
    assert parser('asdflj (kla (inner) asd) port (another ))(unclosed') == 'asdflj port )(unclosed'
    assert parser('text (text(text)) tex(t)') == 'text tex'
    assert parser('(((()())))') == ''
    assert parser('((sad(()w(dsa))fwa))') == ''
    assert parser('((sad(()w(dsa))fwa)) text') == 'text'
    assert parser('(((') == '((('
    assert parser('()((') == '(('
    assert parser('((()') == '(('
    assert parser(')())()') == '))'
    assert parser(' asd(f)lj (kla ((inner)) asd) p()or(t) (another ))(unclosed') == 'asdlj por )(unclosed'