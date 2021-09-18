import random
import string
import argparse


dictionary = {
    'u': string.ascii_uppercase,
    'l': string.ascii_lowercase,
    'd': string.digits,
    's': '.!?#$%&*-+'
}


def get_args():
    parser = argparse.ArgumentParser(description='Generate a random password')
    parser.add_argument('-l',
                        default=8,
                        type=int,
                        help='password length (default 8)',
                        metavar='password_length',
                        dest='length')
    parser.add_argument('-c',
                        default=1,
                        type=int,
                        help='capitals letters amount (default 1)',
                        metavar='capitals_amount',
                        dest='capitals')
    parser.add_argument('-d',
                        default=1,
                        type=int,
                        help='digits amount (default 1)',
                        metavar='digits_amount',
                        dest='digits')
    parser.add_argument('-s',
                        default=1,
                        type=int,
                        help='symbols amount (default 1)',
                        metavar='symbols_amount',
                        dest='symbols')
    return vars(parser.parse_args())


def valid_args(args):
    n = args['length'] - (args['capitals'] + args['digits'] + args['symbols'])
    if n >= 0:
        return True
    return False


def generate_random_base(length, capitals, digits, symbols):
    base = ['l']*length
    base_indx = [i for i in range(0, length)]

    to_paste = 'u'*capitals + 'd'*digits + 's'*symbols
    for p in to_paste:
        indx = random.choice(base_indx)
        base_indx.remove(indx)
        base[indx] = p
    return base


def get_random_element(seq):
    return random.choice(seq)


def fill_base(base):
    result = ''
    for element in base:
        result += random.choice(dictionary[element])
    return result


def main():
    args = get_args()
    if valid_args(args):
        password_base = generate_random_base(args['length'], args['capitals'], args['digits'], args['symbols'])
        password = fill_base(password_base)
        print(password)
    else:
        print('Error. Password length is too small to fit all special symbols')


if __name__ == '__main__':
    main()
