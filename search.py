
import wong


def menu():
    '''
        Menu of commands for the user
    '''

    print()
    print("1. s - Search for a Book(result upto 15)\n2. l - Want Long results , Search for Book(result upto 40)\n3.q or Q- for exit from the program\n")
    choice=input()

    if(choice=='s'):
        query=input("Search for a Book.. ")
        print("\nsearching for all the books similar to your query............\n")
        wong.search_book(query,15)

    elif(choice=='q' or choice=='Q'):
        exit()

    elif(choice=='l'):
        query=input("Search for a Book.. ")
        print("\nsearching for all the books similar to your query............\n")
        wong.search_book(query,40)


    else:
        print("It look like you did not read the command right or press something else by mistake.\n Don't worry try again no one is judging ")
        menu()


def main():
    '''
        The main() funtion
    '''
    print()
    print("------------------------------------------Wong The Librarian------------------------------------------")
    print("  Your personal Librarian for searching PDF and epub of Books and give you direct download link  ")

    menu() #calling menu


if __name__ == '__main__':
    main()
