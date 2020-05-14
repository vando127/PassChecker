import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the API and try again')
    return res


def get_pass_leaks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    # print(response)
    return get_pass_leaks(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            return f"{password} was found {count} times.\nChange your password."

        else:
            return f"The force is strong with {password}!!\nYou can use it as your secret password!!."

    return 'DONE!'


if __name__ == '__main__':
    print(sys.argv)
    sys.exit(main(sys.argv[1:]))
