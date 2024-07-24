from func import SelectMenu
from func import Users
from func import Books
from func import ViewAll
from func import category
from func import Save
from func import Load


def main():
    users = list()
    books = list()
    genres = list()

    while True:
        key = SelectMenu()      

        if key == "0":
            break

        elif key == "1":
            Users(users)

        elif key == "2":
            Books(books)

        elif key == "3":
            category(genres)

        elif key == "4":
            ViewAll(users, books, genres) 

        else:
            print("잘못 선택하였으니 다른 번호를 선택해주세요. : ")   

        input("엔터를 누르세요. : ")

    Save(users, books ,genres)  
    print("프로그램을 종료합니다.")  


if __name__ == "__main__":
    main()