task =[]

def tasks():
    tas = input("please insert the task: ")
    task.append({'task': tas, 'complete': False})

def view():
    if not task:
        print("not task")
        return
    print("\n ===to do-list:===")
    for elem, item in enumerate(task,1):
        status = 'complete' if item['complete'] else 'not completed'
        print(f"{elem}. [{status}] : {item['task']}")

def delete():
    view()
    num = int(input("enter the task to be removed: "))
    if 1 <= num <= len(task):
        print(f"Deleted task: {task.pop(num-1)['task']}")
    else:
        print("invalid")

def mark():
    view()
    num = int(input("enter the task to be marked: "))
    if 1 <= num <= len(task):
        task[num-1]['complete'] = True
    else:
        print("invalid")

def main():
    while True:
        print("===to do list===")
        print("1.add task")
        print("2.view")
        print("3.delete")
        print("4.mark")
        print("5.exit")

        choice = input("choose your option: ")

        if choice == '1':
            tasks()
        elif  choice == '2':
            view()
        elif choice == '3':
            delete()
        elif choice == '4':
            mark()
        else:
            print("good bye")
            break

if __name__ == "__main__":
    main()