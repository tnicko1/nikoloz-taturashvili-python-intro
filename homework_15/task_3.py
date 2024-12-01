def output(friends_dict):
    for friend in friends_dict:
        if len(friends_dict[friend]) == 1:
            string_to_print = f'{friend} has 1 friend: {", ".join(friends_dict[friend])}'
        else:
            string_to_print = f'{friend} has {len(friends_dict[friend])} friends: {", ".join(friends_dict[friend])}'
        print(string_to_print)

def main():
    user_input = input('Who friended who (e.g. Harry - Hermione)? (type FINISH to exit): ')

    friends = {}

    while user_input.lower() != 'finish':
        friend1, friend2 = user_input.split(' - ')
        if friend1 in friends:
            friends[friend1].append(friend2)
        else:
            friends[friend1] = [friend2]

        if friend2 in friends:
            friends[friend2].append(friend1)
        else:
            friends[friend2] = [friend1]
        user_input = input('Who friended who (e.g. Harry - Hermione)? (type FINISH to exit): ')
    else:
        output(friends_dict=friends)
        return

if __name__ == '__main__':
    main()