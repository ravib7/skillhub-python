quiz = [
    {
        "question":"1] 2+2 = ?",
        "options":[
            "a. 22",
            "b. 4",
            "c. dell",
            "d. none",
        ],
        "answer":"b"
    },
    {
        "question":"2] 3**3 = ?",
        "options":[
            "a. 3",
            "b. 33",
            "c. 27",
            "d. none",
        ],
        "answer":"c"
    },
    {
        "question":"3] 10//3 = ?",
        "options":[
            "a. 3",
            "b. error",
            "c. 30",
            "d. none",
        ],
        "answer":"a"
    },
    {
        "question":"4] 5+7 = ?",
        "options":[
            "a. 3",
            "b. error",
            "c. 30",
            "d. 12",
        ],
        "answer":"d"
    },
    {
        "question":"5] 5 > 5 = ?",
        "options":[
            "a. True",
            "b. error",
            "c. False",
            "d. 5",
        ],
        "answer":"c"
    },
]

right = []
wrong = []
score = 0
print("welcome to quiz")

for item in quiz:
    print(item["question"])
    for op in item["options"]:
        print(op)
    choice = input("chooce option a/b/c/d ")
    if choice == item["answer"]:
        print("Correct Answer ✅")
        right.append(item["question"])
        score += 10
    else:
        print("Wrong Answer ❌")
        wrong.append({
            "q":item["question"],
            "answer":item["answer"],
            "you":choice
        })
        score -=5
    print("-------------------------------\n\n") # skip character

print(f"your score is {score}/50")

print(right)
print(wrong)


    