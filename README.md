# 🦁[멋쟁이 사자처럼 첫 개인 프로젝트]🦁
- 주제 : Python기반의 도서관 출납 서비스 개발 프로젝트
- 기간 : 2024.07.22(월) ~ 2024.07.25(목)

## 1. 프로젝트 구현 데이터
### - ver 0.1
![image](https://github.com/user-attachments/assets/2e913e75-ca3a-4b89-b463-b68963746da4)

사실 데이터 간 연결이 되도록 만들고 싶었는데 아직 거기까지는 실력이 안되는듯하다.

많은 수정을 거쳐 ver 0.1에서는 단순한 동작이 실행 되도록 설정했다.

## 2. 프로젝트 소개
### - ver 0.1
- 도서관을 이용하는 회원, 도서관에서 소장하고 있는 도서와 카테고리를 설정할 수 있다.
- 함수를 이용하여 터미널에서 확인이 가능한 프로그램이다.
- 도서관을 이용하는 회원과 도서관에서 소장하고 있는 도서을 "추가, 삭제, 검색, 보기" 할 수 있다.
- 도서관에서 소장하고 있는 도서의 카테고리를 "추가, 삭제, 보기" 할 수 있다.

## 3. 코드소개
### - ver 0.1
사용한 파일은 2개다. 2개로 나눠서 한 이유는 코드가 많아지다보니 보기 불편했기 때문이다.
먼저, **bookmain,py**에 대한 설명이다.

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
    

    

## 4. 아쉬운 점
### - ver 0.1

**[회원정보관리, 도서정보관리, 카테고리관리]** 안에 있는 모든 기능들이 제대로 잘 작동한다.

그런데, 저장 후에 다시 그 데이터들을 불러오는 것이 안된다.

코딩이 잘못 짜여진 것 같은데 못찾겠다. 이 부분은 나중에 꼭 수정하여 제대로 구현이 되게 만들 예정이다.
