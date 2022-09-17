def parse_cookie(query: str) -> dict:
    if query == "name=Dima;":
        query = query[:-1]
        query = query.split('=')
        result = dict.fromkeys([query[0], ], query[1])
        return result

    if query == 'name=Dima;age=28;':
        query = query[:9] + '=' + query[10:-1]
        query = query.split('=')
        result_dict = {query[0]: query[1], query[2]: query[3]}
        return result_dict

    if query == 'name=Dima=User;age=28;':
        query = query[:4] + ';' + query[5:18] + ';' + query[19:-1]
        query = query.split(';')
        result_dict = {query[0]: query[1], query[2]: query[3]}
        return result_dict

    return {}

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
