## Python 기초 복습

""" #2 Variables and functions - 0. Print something great(?) """ 
# print("Hello world!")

# """ 2. Variable (변수) """ 
# a = 2
# b = 3
# c = a + b
# print(c) # print variable
# '''파이썬은 위에서 아래로 코드를 읽기 때문에 같은 이름의 변수더라도 더 아래 위치하는 값이 그 변수에 반영된다.'''

""" #2 Variables and functions - 1. How to create name of Variable """
# # Wrong way
# '''my Age = 123''' # 변수 이름에 있어서 공백은 허용되지 않는다.
# # 고로 변수선언은
# myAge = 123 # 이런 식으로 하거나(Camel Case)
# my_age = 123 # 이런 식으로 Snake Case를 활용해 쓸 수 있음.
# # 두가지 케이스중에 뭐 쓸지는 본인이 알아서

""" #2 Variables and functions - 2. Booleans and Strings """
# # 만약 변수안에 숫자(int)가 아닌 다른 값을 넣고 싶다면
# # String(문자형)
# my_name = "Daniel"
# my_age = "123"
# print(type(my_age))
# '''
# 변수에는 여러가지 "자료형"이란게 들어갈 수 있는데
# 만약 숫자를 넣고 싶다면 그냥 12 이런식으로 정의할 수 있다.
# 그러나 문자(string)을 넣고 싶다면 우리가 평상시 글 쓸때 인물의 대사를
# 쌍따옴표("")처리 하는 것처럼 쌍따옴표를 붙여주면 된다. 이렇게 되면 따옴표안에
# 숫자를 쓰더라도 문자형으로 인식한다.
# '''
# # Boolean(참 or 거짓) 2진법으론 1 또는 0
# dead = False # 0, off, not True
# live = True # 1, on, True
# # 꼭 맨 앞글자는 대문자여야 함.

""" #2 Variables and functions - 3. Recap """
# my_name = "Daniel"
# age = 20
# dead = False
# print("Hello my name is", my_name)
# print("and I'm", age, "years old")

""" #2 Variables and functions - 4. Functions (함수) """
# print(True) # Print라는 함수를 이용해 우리는 여러가지를 출력할 수 있다.
# print("Hello.")
# print(123) # 이런식으로 우리는 함수를 재활용 할 수 있다.
# '''
# Function. 즉 함수란 일종의 코드 조각(?)같아서 한번 작성하면 그걸 계속 불러와서 쓸 수 있다.
# 대표적인 함수가 바로 파이썬 자체에 내장되어 있는 print().
# 이 함수라는 것을 우리가 직접 정의할 수도 있다.
# '''

# # 그렇다면 Function(함수)는 어떻게 만드는가?
# # 우리가 변수를 선언하는 방법은
# My_name = "blabla" # 이런식으로 이름을 처음으로 선언 그 다음 값을 지정한다.
# # 함수를 선언하는 방법은 def("define"이라는 정의하다의 약자)라는 것이 필요하다.
# def say_hello(): # def 다음에는 함수의 이름을 정해주고 괄호와 콜론을 작성
#     print("Hello how r u?") # 함수의 이름처럼 내가 이 함수를 쓸때마다 hello라고 말하게 하고 싶다면
#     # 이렇게 함수안에 특정 기능을 하는 코드를 넣는다.
# # 그리고 그냥 이렇게만 두면 우리가 함수를 부르지 않았기 때문에 아무런 기능도 하지 않는다.
# say_hello() # 라고 불러줘야지 작동한다. 일종의 실행버튼인 셈.

""" #2 Variables and functions - 5. Indentation (들여쓰기) """
# # 파이썬에선 보통 함수나 if, for문 등등... 여러 함수를 써먹을 때 안에 코드가 들어갈 경우
# def something():
#     print("Why it's important to use Indentation") # 이런식으로 들여쓰기가 된다.
#     # 그 이유는 이 코드가 위에 있는 함수의 소속됬다는 것을 알리기 위해서다.
#     # 들여쓰기는 두칸 띄워야함. (tab 한번)
# # 하지만 이러한 규칙은 Python에서만 적용된다.
# # 나머지 언어들(Java, JS, C#, TS, Rust, Go)같은 언어들은 중괄호"{}"를 써서 함수 영역을 표시하기 때문.
    
# """ #2 Variables and functions - 6. Parameters & Arguments (매개변수와 인수) 이거 중요 """
# def say_hello2(name):
#     print("Hello", name,"how are you?")

# say_hello2("C언어가 씨불씨불") # 우리가 함수를 부를 때 특정값을 그 함수에 보내고 싶을 때
# # 괄호안에 쓰는게 바로 Argument(인수)다. 그리고 그 인수를 저 함수의 name이라는 Parameter(매개변수)가 받아서 그 값을 쓰는 것이다.
# # 이 두 개념은 헷갈리기 때문에 확실히 기억해둘것.

# --2023.12.28 파이썬복습 End -- #

""" #2 Variables and functions - 7. Multiple Parameters """
# # 여러개의 Parameters(매개변수들)은 위에 있는 매개변수와 인수의 확장개념
# # 말 그대로 여러개의 매개변수들을 받을 수 있다.
# # 쓰는 방법은 print()에서 여러 값을 출력할 때처럼 콤마(,)를 쓰면 됨.
# # 주의 할점은 반드시 순서를 지킬 것. 잘못 써서 name에 나이가 들어가면 안되니까
# # 또한 매개변수의 갯수와 인수의 갯수는 반드시 일치시켜야 한다. 안그럼 에러남.
# def say_hello3(user_name, user_age):
#     print("hello", user_name)
#     print("You are", user_age, "years old") 

# say_hello3("Daniel", 20)

# """ #2 Variables and functions - 8. Functions Recap """
# '''
# 함수란 일종의 기계적 장치로 어떠한 목적을 가지고 기능하는 장치를 만들면
# 같은 목적의 동작을 요할 때 그 기계를 재활용 하는 것처럼
# 함수또한 같은 목적의 기능을 수행하기 위해 만든 재활용 기계다.

# 함수안에 특정값을 주고싶을 때 매개변수를 지정해 값을 받을 수 있다.
# 매개변수에 넣는 값을 인수라고 한다.
# '''
# def tax_calculator(money):
#     print(money * 0.35) # 0.35은 세금비율

# tax_calculator(15000000000000)
# tax_calculator(150)

# # --2023.12.29 파이썬복습 End -- #

# """ #2 Variables and functions - 9. Default Parameters (기본 매개변수) """
# def say_hello4(user_name):
#     print("Hello", user_name)

# # 기본적으로 매개변수를 만들면 그 갯수에 맞게 인수를 넣어줘야 한다.
# say_hello4("daniel")
# # say_hello4() # 그렇지 않고 아무런 인수도 넣지 않는다면 에러가 나게 될 것이다.
# # 그러나 서비스를 사용하는 유저 입장에선 이렇게 에러가 나고 프로그램이 종료되어버린다면
# # 그 경험이 그닥 좋지는 않을 것이다. 그러므로 아무런 인수가 들어오지 않았을 경우,
# # 그 상황마저도 그것에 맞게 동작하는 코드를 짜면 유저의 경험은 더욱 향상될 것이다.
# # say_hello4 함수의 경우 아무런 이름도 입력하지 않을 경우, Anonymous로 이름을 자동 대체하게 만들어보자.
# def say_hello5(user_name="Anonymous"): # 이런식으로 매개변수에 기본값을 설정 해주는 것이 바로 Default parameter(기본 매개변수)이다!
#     print("Hello", user_name)

# say_hello5()

# # --2023.12.31 파이썬복습 End -- #

# """ #2 Variables and functions - 10. Return value (반환값) """
# # 반환값이란 함수 안에 있는 값을 다른함수에서도 쓸 수 있게 만들어준다.
# # return 을 쓴다.
# def tax_calculator2(money):
#     return money * 0.35

# def pay_tax(tax):
#     print("thank you for payiong", tax)

# pay_tax(tax_calculator2(150000000))
# # 이런식으로 함수 안에서 나오는 결과값을 return을 사용해 다른 함수에 전달할 수 있게 되는 것이다.

""" #2 Variables and functions - 11. Return recap """
# # 외전으로 문자열안에 변수 넣는 법 근데 엄청 유용함.
# My_name2 = "daniel"
# My_age2 = 21
# My_color_eyes = "black" # 이 3개의 변수를 전부 String안에 넣고 싶다면?

# print(f"Hello I'm {My_name2}, I have {My_age2} years in the earth, {My_color_eyes} is my eye color") # 맨 앞의 "f"는 "format"의 앞글자를 따서 만든 거임.
# # 이렇게 쌍따옴표 앞에 f를 붙이면 굳이 콤마를 쓸 필요도 없이 중괄호를 활용, 한번에 출력이 가능하다.

# # make juice 만들어보기
# def make_juice(fruit):
#     return f"{fruit}+🧃"

# def add_ice(juice):
#     return f"{juice}+🧊"

# def add_sugar(iced_juice):
#     return f"{iced_juice}+◽"

# juice = make_juice("🍎")
# cold_juice = add_ice(juice)
# perfect_juice = add_sugar(cold_juice)

# print(perfect_juice)

# # 한가지 주의해야 할 점은 함수 안에서 return을 쓰는 순간 그 함수는 return이 적힌 코드를 기점으로 기능을 종료시켜버린다.
# # 반드시 return은 맨 마지막에 쓸 것.

""" #3 Control Flow - 0. If(조건문) """
# # ATM에 카드를 넣으면 비밀번호를 요구한다.
# # 우리가 비밀번호를 입력했을 때 ATM기계는 그 기번이 맞는지(If) 알아본다. 그것이 바로 if(조건문)이다.
# # if의 기본적인 작성방법: 
# condition = 123
# if condition:
#     print("bla bla")
# # if 문에선 저 condition이라는 이름의 변수가 참이라면 아래 종속되있는 print(예시)를 실행할 것이고,
# # 거짓이라면 실행하지 않을 것이다.
# if 10>5:
#     print("Correct!") # 10은 5보다 큰게 맞으므로 이 조건문은 참.
# # 주의해아 할 점은 같다(=)라는 등호를 두번반복 한 더블등호(?)"=="를 쓴다.
# # 이유인 즉슨 =이란 등호는 이미 파이썬에서 변수를 선언할 때 쓰고 있기 때문.
# a = 10
# if a == 10:
#     print("True!") # 숫자 뿐만 아니라 문자열도 조건문 사용이 가능하다.

# -- 2024.01.01 파이썬 복습 종료 -- #

""" #3 Control Flow - 1. Else & Elif """
# # if문의 확장형이다. Else 와 Elif는 선행된 if문이 거짓일때의 경우를 대비한 조건문이다. 
# password_correct = False

# if password_correct:
#     print("Here is your money.")
# else: # 이렇게 if 문 아래 써주면 됨.
#     print("Password is incorrect:(")
# # 단 저 else는 다른 조건을 걸 수 없기 때문에 가정해야 하는 상황이 2가지 이상인경우
# # elif를 통해 2+a의 상황에서의 조건을 정해준다.
# if password_correct:
#     print("password is incorrect:(")
# elif password_correct==True:
#     print("Here is your money")

# """ #3 Control Flow - 2. Recap """
# winner = 5

# if winner < 10:
#     print("Run!")
# else:
#     print("Else")

# # 참고로 같지 않다는 파이썬에서 "!="로 표현한다.
# if winner != 10:
#     print("that's true!")

# """ #3 Control Flow - 3. And&Or """
# # input이란 함수는 변수안에 들어갈 값을 사용자가 직접 입력할 수 있도록
# # 입력값을 받는 함수이다.
# Age = int(input("How old are you?"))
# if Age < 18:
#     print("You can't drink yet.")
# elif age >= 18 and age <= 35: # and은 두개 이상의 명제가 둘다 참이야 성립한다.
#     print("You can drink.")
# elif age == 60 or age == 70: # or은 두개 이상의 명제중 하나만 참이여도 참이다.
#     print("Birthday party!")
# else:
#     print("Go ahead!")

# # 간단하게 And 과 or의 차이를 설명
# True and True == True
# False and True == False
# True and False == False
# False and False == False

# True or True == True
# False or True == True
# True or False == True
# False or False == False

""" #3 Control Flow - 4. Python Standard Library(파이썬 표준 라이브러리) """
# https://docs.python.org/ko/3/library/index.html
# 파이썬을 사용해서 카지노를 만들어보자
# from random import randint

# user_choice = int(input("Choose number."))
# pc_choice = randint(1,50)

# if user_choice == pc_choice:
#     print("You won!")
# elif user_choice > pc_choice:
#     print("Lower! computer chose:",pc_choice)
# elif user_choice < pc_choice:
#     print("Higher! computer chose:",pc_choice)
# 저 코드에서 pc_choice라는 함수에 들어가는 숫자를 랜덤하게 정하고 싶다면
# random 함수를 쓰면 된다. random함수는 파이썬애 내장되어있는 내장함수다.
# default function(내장함수)란 파이썬에 기본적으로 탑재가 되어있어
# 파이썬을 설치만 하면 바로 쓸 수 있는 함수를 뜻한다.
# 위 링크참고.
    
""" #3 Control Flow - 5. While(조건 반복문) """
# While은 함수로써 코드가 동작을 반복하도록 만들어준다.
# if가 조건이 성립할때 특정동작을 하고 종료된다면
# while은 조건이 성립할때 그 동작을 반복하게 한다.
# while True:
#     print("hello") # hello 무한반복

# distance = 0

# while distance <= 20:
#     print("I'm running: ", distance,"km")
#     distance = distance + 1

# """ #3 Control Flow - 6. Python Casino """
# from random import randint

# print("Welcome to python casino")
# pc_choice = randint(1,100)

# playing = True

# while playing:
#     user_choice = int(input("Choose number (1-100):"))
#     if user_choice == pc_choice:
#         print("you won!")
#         playing = False
#     elif user_choice > pc_choice:
#         print("Lower!")
#     elif user_choice < pc_choice:
#         print("Higher!")

""" #3 Control Flow - 7. Recap """
# from random import randint -> 이 코드는 random이라는 모듈에서 randint라는 함수를 가져오기 위한 코드이다.
# 나머지 코드는 위에 있는 6. 파이썬 카지노 파트의 코드를 다 이해하면 끝. 쓰기 귀찮음...

""" #4 Data Structures(자료구조) = 0. Methods """
# 함수와 메소드의 차이점
'''
우선 함수는 여러문자들이 하나의 기능을 구현하도록 구성한 것이라고 할 수 있다.
그 함수 중에서 내부에 정의한 함수를 메소드라고 부르는 것이다. 또한 메소드는 객체의 속성을
다루기 위한 행위를 정의한 것이라는 의미도 포함하고 있다.

즉, 독립적으로 존재하는 함수이냐, *클래스 내부에 종속되어 있느냐의 구분으로 함수와 메소드를 구분할 수 있다.

*클래스 : 파이썬에서의 클래스란 객체를 표현하기 위한 문법으로
체크박스, 스크롤바 같은 특정한 개념이나 모양을 존재하는 것을 객체(object)라고 부른다.
'''
# name = "nico"

# print(name.upper()) #의 upper를 메소드라 한다. 즉 독자적인 함수가 아닌 함수 안에 종속되어 다양한 기능을 수행할 수 있는 함수가 바로 메소드다.
# # upper라는 메소드는 해당 함수안에 있는 str(문자, 영어)의 소문자롤 대문자로 바꿔준다.
# # 여러 메소드 시험
# print(name.title)
# print(name.capitalize)

""" #5 OOP(Object Oriented Programming) """

'''
객체지향 프로그래밍이란 코드를 구성하는 방법에 대한 규칙이다.
좀 더 쉽게 말하자면 코드에 존재하는 모든 객체를 각각의 상태와 행위,
즉 동작을 가지는 객체로 만들어 그 객체들끼리 상호작용함으로써 기능을 완성하는 프로그래밍 방법이다.
'''

# 별로 좋지 않은 코드의 예시
'''daniel = {
	"name": "Daniel",
    "XP": 100,
    "team": "Team Red",
}

def introduce_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! my name is {name}. and I play for {team}")
    
introduce_player(daniel)'''

# OOP의 예시