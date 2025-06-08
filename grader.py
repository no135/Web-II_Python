def grades(average):
    if 90 <= average <= 100:
        return 'a'
    elif 80 <= average < 90:
        return 'b'
    elif 70 <= average < 80:
        return 'c'
    elif 60 <= average < 70:
        return 'd'
    else:
        return 'f'
    
def main():
    marks = []
    for i in range(1,6):
        mark = float(input(f"please enter the {i} subject: "))
        while True:
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                    print("Mark must be between 0 and 100.")
                    break
    
    average = sum(marks) / len(marks)
    grade = grades(average)

    print(f"average score: {average:.2f}")
    print(f"grade:{grade}")

if __name__ == "__main__":
    main()