import os

def SelectMenu():
    os.system("clear")

    print("==============================")
    print("  도서 관리 프로그램 ver.0.1")
    print("==============================")
    print("1: 회원정보 관리")
    print("2: 도서정보 관리")
    print("3: 카테고리 관리")
    print("4: 전체 보기")
    print("0: 프로그램 종료")
    return input("==> 번호 입력 : ")

def Users(users):
    print("======= 회원정보 관리 =======")
    print("1. 회원 추가 ")
    print("2. 회원 삭제 ")
    print("3. 회원 검색 ")
    print("4. 회원 보기 ")

    u = int(input("==> 번호 입력 : "))
    if u == 1:
        AddUsers(users)
    elif u == 2:
        RemoveUsers(users)
    elif u == 3:
        SearchUsers(users)
    elif u == 4:
        ViewUsers(users)
    else:
        print("다시 입력하세요")

def AddUsers(users):
    print("====== 회원 추가 ======")
    name = input("- 이름 : ")
    id = input("- ID : ")
    number = input("- 휴대전화번호 : ")
    user = [name, id, number]
    users.append(user)
    ViewUsers(users)
    print("*** 추가완료 되었습니다 ***")

def Find(users, id):
    for i in range(0, len(users)):
        user = users[i]

        if user[1] == id:
            return i
    return -1    

def RemoveUsers(users):
    print("====== 회원 삭제 ======")
    id = input("- 삭제할 회원의 ID : ")
    ri = Find(users, id)

    if ri == -1:
        print("존재하지 않는 ID입니다.")
        return
    
    user = users.pop(ri)
    print(user)
    print("삭제하였습니다.")
    
def SearchUsers(users):
    print("====== 회원 검색 ======")
    id = input("- 검색할 회원의 ID : ")
    ri = Find(users, id)
    

    if ri == -1:
        print("존재하지 않는 ID입니다.")
        return
    
    user = users[ri]   
    print(user)
    
def ViewUsers(users):
    print("====== 회원 보기 ======")
    print("[등록된 회원: {}명]".format(len(users)))
    print(users)




def Books(books):
    print("======= 도서정보 관리 =======")
    print("1. 도서 추가 ")
    print("2. 도서 삭제 ")
    print("3. 도서 검색 ")
    print("4. 도서 보기 ")

    b = int(input("==> 번호 입력 : "))
    if b == 1:
        AddBooks(books)
    elif b == 2:
        RemoveBooks(books)
    elif b == 3:
        SerachBooks(books)
    elif b == 4:
        ViewBooks(books)
    else:
        print("다시 입력하세요")   


def AddBooks(books):
    print("====== 도서 추가 ======")
    title = input("- 도서명 : ")
    isbn = input("- ISBN : ")
    author = input("- 저자 : ")
    publisher = input("- 출판사 : ")
    price = input("- 가격 : ")
    book = [title, isbn, author, publisher, price]
    books.append(book)
    ViewBooks(books)
    print("*** 추가완료 되었습니다 ***")

def FindBooks(books, isbn):
    for i in range(0, len(books)):
        book = books[i]

        if book[1] == isbn:
            return i
    return -1    

def RemoveBooks(books):
    print("====== 도서 삭제 ======")
    isbn = input("- 삭제할 도서의 ISBN : ")
    bi = FindBooks(books, isbn)

    if bi == -1:
        print("존재하지 않는 ISBN입니다.")
        return
    
    books.pop(bi)
    print(books)
    print("삭제하였습니다.")

def SerachBooks(books):
    print("====== 도서 검색 ======")
    isbn = input("- 검색할 도서의 ISBN : ")
    bi = FindBooks(books, isbn)
    book = books[bi]

    if bi == -1:
        print("존재하지 않는 ISBN입니다.")
        return   
    book = books[bi]
    print(book)

def ViewBooks(books):
    print("====== 도서 보기 ======")
    print("[등록된 도서: {}개]".format(len(books)))
    print(books)


def category(genres):
    print("======= 카테고리 관리 =======")
    print("1. 카테고리 추가 ")
    print("2. 카테고리 삭제 ")
    print("3. 카테고리 보기 ")

    c = int(input("==> 번호 입력 : "))
    if c == 1:
        AddCategory(genres)
    elif c == 2:
        RemoveCategory(genres)
    elif c == 3:
        ViewCategory(genres)
    else:
        print("다시 입력하세요")   


def AddCategory(genres):
    print("====== 카테고리 추가 ======")
    genre = input("- 카테고리명 : ")
    genres.append(genre)
    ViewCategory(genres)
    print("*** 추가완료 되었습니다 ***")


def FindCategory(genres, delcategory):
    for i in range(0, len(genres)):
        genre = genres[i]

        if genre[1] == delcategory:
            return i
    return -1   

def RemoveCategory(genres):
    print("====== 카테고리 삭제 ======")
    delcategory = input("- 삭제할 카테고리명 : ")
    dc = FindCategory(genres, delcategory)

    if dc == -1:
        print("존재하지 않는 카테고리입니다.")
        return
    
    genres.pop(dc)
    print(genres)
    print("삭제하였습니다.")

def ViewCategory(genres):
    print("====== 카테고리 보기 ======")
    print("[등록된 카테고리: {}개]".format(len(genres)))
    print(genres)

def ViewAll(users, books, genres):
    ViewUsers(users)
    print()
    ViewBooks(books)
    print()
    ViewCategory(genres)

def Save(users, books, genres):
    print("====== 저장 ======")

    ufs = open("uesrs.csv", "w")

    for user in users:
        u_str = ""

        for uelem in user:
            u_str += str(uelem) +","     

        u_str = u_str[:-1] + "\n"   
        ufs.write(u_str)

    ufs.close()


    bfs = open("books.csv", "w")

    for book in books:
        b_str = ""                      

        for elem in book:               
            b_str += str(elem) +","     

        b_str = b_str[:-1] + "\n"       
        bfs.write(b_str)                

    bfs.close()

    gfs = open("genres.csv", "w")

    for genre in genres:
        gfs.write(genre + "\n")

    gfs.close()


def Load(users, books, genres):
    print("---------------- 로딩 ----------------")

    try:
        ufs = open("users.csv", "r")
        userdata = ufs.read()
        ufs.close()
        ud_us = userdata.split("\n")

        for user in ud_us:
            ues = user.split(",")

            if len(ues) < 4:
                break

            name, id, number = ues[0], ues[1], ues[2]
            user = [name, id, number]
            users.append(user)


        gfs = open("genres.csv", "r")
        datas = gfs.read()
        gfs.close()
        
        ds_gs = datas.split("\n")

        for genre in ds_gs:
            if(genre == ""):
                break
            genres.append(genre)

        bfs = open("books.csv", "r")
        bs = bfs.read()
        bfs.close()
        bs_bs = bs.split("\n")

        for bstr in bs_bs:
            bes = bstr.split(",")

            if len(bes) < 6:
                break

            title,isbn = bes[0], bes[1]
            gn = int(bes[2])
            author, publisher,price = bes[3], bes[4], bes[5]
            book = [title, isbn, gn, author, publisher, price]
            books.append(book)

    except:
        print("환영합니다.")
        return