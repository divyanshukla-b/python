from ques import questionsclass

questionlist = [
    "blue is look like\n(a)blue\n(b)black\n(c)red",
    "\n black look like\n(a)blue\n(b)black\n(c)red",
    "\n red look like\n(a)blue\n(b)black\n(c)red",
]

questions = [
    questionsclass(questionlist[0], "a"),
    questionsclass(questionlist[1], "b"),
    questionsclass(questionlist[2], "c"),
]


def runtest(questionss):
    score = 0
    for q in questionss:
        ans = input(q.prompt)
        if ans == q.ans:
            score += 1
    print(score)


runtest(questions)
