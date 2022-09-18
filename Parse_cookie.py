def parse_cookie(query: str) -> dict:
    if len(query) > 1:
        query = query.split(';')
        dictionary = dict([parse.split('=', 1) for parse in query if parse])
        return dictionary
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
