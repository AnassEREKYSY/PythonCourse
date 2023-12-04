
# exo1
if __name__ == '__main__':
    print("Hello, World!")

# exo2
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
    
# exo3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#exo4
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)

#exo5 
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))

year = int(input())
print(is_leap(year))

#exo6
if __name__ == '__main__':
    n = int(input())
    
    for i in range(1, n + 1):
        print(i, end='')

#exo7
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(coordinates)

#exo8
if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    unique_scores = sorted(set(scores), reverse=True)
    print(unique_scores[1])

#exo9
if __name__ == '__main__':
    n = int(input())
    
    students = []
    for _ in range(n):
        name = input()
        grade = float(input())
        students.append([name, grade])
    second_lowest_grade = sorted(set(grade for name, grade in students))[1]
    for name, grade in sorted(students):
        if grade == second_lowest_grade:
            print(name)

#exo10
if __name__ == '__main__':
    n = int(input())
    student_records = {}
    for _ in range(n):
        record = input().split()
        name, marks = record[0], list(map(float, record[1:]))
        student_records[name] = marks
    query_name = input()
    average_marks = sum(student_records[query_name]) / len(student_records[query_name])
    print("{:.2f}".format(average_marks))

#exo11
if __name__ == '__main__':
    my_list = []
    n = int(input())
    for _ in range(n):
        command = input().split()
        if command[0] == 'insert':
            i, e = map(int, command[1:])
            my_list.insert(i, e)
        elif command[0] == 'print':
            print(my_list)
        elif command[0] == 'remove':
            e = int(command[1])
            my_list.remove(e)
        elif command[0] == 'append':
            e = int(command[1])
            my_list.append(e)
        elif command[0] == 'sort':
            my_list.sort()
        elif command[0] == 'pop':
            my_list.pop()
        elif command[0] == 'reverse':
            my_list.reverse()
#exo12
if __name__ == '__main__':
    n = int(input())
    integer_tuple = tuple(map(int, input().split()))
    result = hash(integer_tuple)
    print(result)

#exo13 
def swap_case(s):
    return
def swap_case(s):
    return s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#exo14
def split_and_join(line):
    words = line.split(" ")
    result = "-".join(words)
    return result
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#exo15
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#exo16
def mutate_string(s, position, character):
    string_list = list(s)
    string_list[position] = character
    mutated_string = ''.join(string_list)
    
    return mutated_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
