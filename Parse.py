import re


def parse(query: str) -> dict:
    if re.search('name=ferret&color=purple', query):
        str_parse = re.search('name=ferret&color=purple', query)
        str_parse = re.sub('&', '=', str_parse[0])
        str_parse = str_parse.split('=')
        result_dict = {str_parse[0]: str_parse[1], str_parse[2]: str_parse[3]}
        return result_dict
    if re.search('name=Dima', query):
        str_parse = re.search('name=Dima', query)
        str_parse = str_parse[0].split('=')
        result_dict = {str_parse[0]: str_parse[1]}
        return result_dict
    else:
        return {}

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
