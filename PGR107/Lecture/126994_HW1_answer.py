#Answer 1.1
#==================================================
str1 = "hello"
str2 = "WORLD"
str3 = str1 + str2
print(str1.upper())
print(str2.lower())
print(str1.upper() + ", " + str2.lower())


#Answer 1.2
#==================================================
def check_grade(score: int) -> tuple:
    grade = ""
    text = ""

    match score:
        case _ if score >= 90:
            grade = "A"
        case _ if score >= 80:
            grade = "B"
        case _ if score >= 70:
            grade = "C"
        case _ if score >= 60:
            grade = "D"
        case _:
            grade = "F"

    if score > 95:
        text = "Outstanding Achievement"

    return grade, text

def main():
    score = int(input("Enter Score: "))
    grade, text = check_grade(score)

    print("GRADE : ", grade)
    print(text)

if __name__ == "__main__":
    main()


#Answer 1.3
#==================================================
def check_value(start: int, end: int) -> tuple:
    result = []
    num = start

    while num <= end:
        if(num % 2 == 0 and num % 3 == 0):
            result.append(f"{num}: Multiple of 2 and 3")
        elif num % 2 == 0:
            result.append(f"{num}: Multiple of 2")
        elif num % 3 == 0:
            result.append(f"{num}: Multiple of 3")
        else:
            result.append(f"{num}: Not a multiple of 2 of 3")
        num += 1
    
    return result
        
def main():
    start =int(input("Start Value: "))
    end = int(input("End Value: "))

    results = check_value(start, end)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
