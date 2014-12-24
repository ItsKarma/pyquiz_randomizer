#-------------------------------------------------------------------------------
# Name:        QuizRandomizer.py
# Purpose:     Randomizes a multiple choice quiz.
# Author:      Matthew Karmazyn
# Created:     2014/05/13
#-------------------------------------------------------------------------------

import sys
import random

# Define some questions and answers here.
# Only supports multiple choice with 6 possible answers at this time.
#  of the 6 it will display 4 (a-d)
# Always place the correct answer to the question as a1
#  it will be randomized and always displayed.
q01 = "Which of the following commands will tell you the user name you are logged in as?"
q01a1 = "whoami"
q01a2 = "username"
q01a3 = "passwd"
q01a4 = "login"
q01a5 = "pwd"
q01a6 = "id"

q02 = "When running a command with elevated privileges, what file determines whether your account can be granted those elevated privileges or not?"
q02a1 = "/etc/sudoers"
q02a2 = "/etc/su.conf"
q02a3 = "/var/auth"
q02a4 = "/var/sudo.conf"
q02a5 = "/var/sudoers"
q02a6 = "/etc/sudo"

q03 = "The command \"mv file1 file2\" will have which of the following results?"
q03a1 = "rename file1 to file2"
q03a2 = "make a copy of file1 called file2 and then remove file1"
q03a3 = "move the contents of file1 to file2"
q03a4 = "remove file1 and file2"
q03a5 = "rename file2 to file1"
q03a6 = "Wrong Answer"

q04 = "When moving or copying directories, if you want to also move or copy subdirectories of the parent, you use which optional parameter?"
q04a1 = "-r"
q04a2 = "-recurse"
q04a3 = "-v"
q04a4 = "-sub"
q04a5 = "-x"
q04a6 = "-v"

q05 = "The \"special file\" called \"..\" is a shortcut for what?"
q05a1 = "The directory one level up"
q05a2 = "The current directory"
q05a3 = "The home directory"
q05a4 = "The root directory"
q05a5 = "The directory one level down"
q05a6 = "Show hidden files"

q06 = "Filtering output from a command or the content from a file can be accomplished by piping output to what command?"
q06a1 = "grep"
q06a2 = "filter"
q06a3 = "find"
q06a4 = "search"
q06a5 = "locate"
q06a6 = "nano"

q07 = "Changing read/write/execute permissions on a file or a directory can be accomplished using what command?"
q07a1 = "chmod"
q07a2 = "chown"
q07a3 = "chage"
q07a4 = "chpwd"
q07a5 = "chang"
q07a6 = "chnon"

q08 = "Executing the command \"chgrp -R /etc john\" would have what effect (other than hosing your system)?"
q08a1 = "Changing the group ownership of /etc and all files and subdirectories to group ?john?"
q08a2 = "Changing the group ownership of /etc to group ?john?"
q08a3 = "Removing the group ?john? from having access to the /etc directory"
q08a4 = "Changing the owner of /etc to the user 'john'"
q08a5 = "Changing the owner of all files and subdirectories to the user \"john\""
q08a6 = "loggs you off"

q09 = "Which of the following numbers would set a file permission to rwxr-xr-x"
q09a1 = "755"
q09a2 = "777"
q09a3 = "666"
q09a4 = "744"
q09a5 = "655"
q09a6 = "477"
q09a7 = "766"

q10 = "What does FHS stand for?"
q10a1 = "Filesystem Hierarchy Standard"
q10a2 = "Files Have Sizes"
q10a3 = "Free Home Software"
q10a4 = "Frame Height System"
q10a5 = "File Hardening System"
q10a6 = "File Hardening Security"
q10a7 = "Free Hardening Software"

# If you add more questions, you must add them to this q**Array block, and also to qArray line below
#  same if you remove questions, you must remove them from the array.
q01Array = [q01,q01a1,q01a2,q01a3,q01a4,q01a5,q01a6]
q02Array = [q02,q02a1,q02a2,q02a3,q02a4,q02a5,q02a6]
q03Array = [q03,q03a1,q03a2,q03a3,q03a4,q03a5,q03a6]
q04Array = [q04,q04a1,q04a2,q04a3,q04a4,q04a5,q04a6]
q05Array = [q05,q05a1,q05a2,q05a3,q05a4,q05a5,q05a6]
q06Array = [q06,q06a1,q06a2,q06a3,q06a4,q06a5,q06a6]
q07Array = [q07,q07a1,q07a2,q07a3,q07a4,q07a5,q07a6]
q08Array = [q08,q08a1,q08a2,q08a3,q08a4,q08a5,q08a6]
q09Array = [q09,q09a1,q09a2,q09a3,q09a4,q09a5,q09a6]
q10Array = [q10,q10a1,q10a2,q10a3,q10a4,q10a5,q10a6]

qArray = [q01Array,q02Array,q03Array,q04Array,q05Array,q06Array,q07Array,q08Array,q09Array,q10Array]
# Flip the comment below if you would like to not use ALL questions
#  and would like to use a specific ammount. (must be <= the length
#  of the array, otherwise will break!
qArrayLength = len(qArray)
#qArrayLength = 10

# Define some global variables
correct = 0.0
incorrect = 0.0
questionCounter = 1

def CalculateScore():
    percent = correct / (correct + incorrect)
    print "Correct:     " + "{0:.0f}".format(correct)
    print "Incorrect:   " + "{0:.0f}".format(incorrect)
    print "Your Score:  " + "{0:.0f}%".format(float(percent) * 100)

def GetInput(CorrAns,ans1,ans2,ans3,ans4):
    choice = None
    while not choice:
        ans = raw_input("Your Answer: ")
        print ans
        if ans == "a":
            choice = ans1
        elif ans == "b":
            choice = ans2
        elif ans == "c":
            choice = ans3
        elif ans == "d":
            choice = ans4
        else:
            print "You didnt choose a valid option... Try Again."
    if choice == CorrAns:
        global correct
        correct += 1
        print "Correct!"
    else:
        global incorrect
        incorrect += 1
        print "Incorrect!"
        print "Correct answer: " + CorrAns
    print


def DisplayAnswers(a1,a2,a3,a4):
    ansArr = [a1, a2, a3, a4]
    ans1 = random.choice(ansArr)
    ansArr.remove(ans1)
    ans2 = random.choice(ansArr)
    ansArr.remove(ans2)
    ans3 = random.choice(ansArr)
    ansArr.remove(ans3)
    ans4 = random.choice(ansArr)
    ansArr.remove(ans4)
    print "   a. " + ans1
    print "   b. " + ans2
    print "   c. " + ans3
    print "   d. " + ans4
    GetInput(a1,ans1,ans2,ans3,ans4)

def Display(question):
    print """____________________________________
    """
    q = question[0]
    question.remove(q)
    ans1 = question[0] #new position is 0 because we removed the question (0)
    question.remove(ans1)
    ans2 = random.choice(question)
    question.remove(ans2)
    ans3 = random.choice(question)
    question.remove(ans3)
    ans4 = random.choice(question)
    question.remove(ans4)
    global questionCounter
    print format(questionCounter) + ". " + q
    questionCounter += 1
    DisplayAnswers(ans1,ans2,ans3,ans4)

def FindAnswers(aArray):
    if question == q01:
        q01Array = [q01a1,q01a2,q01a3,q01a4,q01a5,q01a6]
        q01ArrayLength = q01Array.count
        for d in range(0,1):
           a1 = random.choice(q01Array)
           q01Array.remove(a1)
           a2 = random.choice(q01Array)
           q01Array.remove(a2)
           a3 = random.choice(q01Array)
           q01Array.remove(a3)
           a4 = random.choice(q01Array)
           q01Array.remove(a4)
    elif question == q02:
        a1 = q02a1
        a2 = q02a2
        a3 = q02a3
        a4 = q02a4
    else:
        a1 = q30a1
        a2 = q30a2
        a3 = q30a3
        a4 = q30a4
    print i+1,": ", question
    DisplayAnswers(a1, a2, a3, a4)

def GetQuestion(i):
    question = random.choice(qArray)
    Display(question)
#    FindAnswers(question)
    qArray.remove(question)
    #print(qArray)

for i in range(0,qArrayLength):
    GetQuestion(i)

CalculateScore()




