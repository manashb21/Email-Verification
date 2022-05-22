'''Simple Email Verifier'''
def at_checker(email):
    """to check for @"""
    position = [] #to track the position of @
    for i in enumerate(email):
        if(i[1]) == "@":
            position.append(i[0])
    if len(position)!=0:
        final_check(position, email)
    else:
        print("@ not present. Invalid Email!")

def first_half(pre_):
    """to check the half before @"""
    for i in pre_:
        if (i=="@" or i=="!" or i=="#"):
            print("Invalid Characters in First Half!")
            return 0
        else:
            return 1

def second_half(post_):
    """to check the half after @"""
    for i in post_:
        if (i.isalpha()) ^ (i.isnumeric()) ^ (i=="."):
            if len(post_) > 4:
                if (post_[-4]==".") ^ (post_[-3]=="."):
                    return 1
                else:
                    print("Invalid Email!")
                    return 0
            else:
                print("Invalid Email!")
                return 0
        else:
            print("Invalid Cahracters in Second Half!")
            return 0

def final_check(position, email):
    """to sum up all the checks"""
    if len(position) > 1:
        print("Invalid Email")
    else:
        print("position of @: {}".format(position))
    pre_ = email[0:position[0]]
    post_ = email[position[0]+1:]
    print(pre_)
    print(post_)
    if first_half(pre_)==1 and second_half(post_)==1:
        print("Valid Email")
    else:
        print("Invalid Email!")




email_ = input("Enter the Email: ")
if len(email_) >= 6:
    if email_[0].isalpha() ^ email_[0].isnumeric():
        at_checker(email_)
    else:
        print("Should start with alphabet or number. Invalid!")
else:
    print("Email too short. Invalid!")
