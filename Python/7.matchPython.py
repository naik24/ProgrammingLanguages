http_status = 404
"""
The _ case is like the default switch case used in C, C++, etc.
"""
match http_status:
    case 400:
        print("bad request")
    case 404:
        print("not found")
    case _:
        print('bruh!')
