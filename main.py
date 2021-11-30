inventory = {}


def add_item(item):
    if check_item(item):
        inventory[item] += 1
        print(item + "의 수량은 " + str(inventory[item]) + "입니다.")
    else:
        inventory[item] = 1
        print(item + "이 추가되었습니다.")

def remove_item(item):
    if check_item(item):
        inventory[item] = 0
        print(item + "의 수량이 0이 되었습니다.")
    else:
        print(item + "이 존재하지 않습니다.")

def consume_item(item):
    if check_item(item):
        if inventory[item] >= 1:
            inventory[item] -= 1
            print(item + "의 수량이 1 감소하였습니다. 현재 " + str(inventory[item]) + "개 남아 있습니다.")
        else:
            print(item + "의 수량이 부족합니다.")
    else:
        print(item + "이 존재하지 않습니다.")

def check_item(item):
    return item in inventory

def print_menu():
    print()
    print("0. 끝내기")
    print("1. 아이템 추가")
    print("2. 아이템 삭제")
    print("3. 아이템 확인")
    print("4. 아이템 사용")
    print()

while True:
    print_menu()
    option = int(input("메뉴 번호를 입력하세요 : "))
    if option == 0:
        print("종료합니다.")
        break
    elif option == 1:
        item = input("아이템을 입력하세요 : ")
        add_item(item)
    elif option == 2:
        eliminated_item = input("아이템을 입력하세요 : ")
        remove_item(eliminated_item)
    elif option == 3:
        print(inventory)
    elif option == 4:
        use_item = input("아이템을 입력하세요 : ")
        consume_item(use_item)
    else:
        print("잘못된 번호를 입력하셨습니다.")
