import random

questions = ["the process of extracting information that is essential, while ignoring what is not relevant, "
             "for the provision of a solution.", "the testing of a completed or nearly completed program in-house by "
             "the development team", "test data that is on the limit of that accepted by a program or data that is "
             "just outside the limit of that rejected by a program.", "a linear sequential program development cycle, "
             "in which each stage is completed before the next is begun.", "The development cycle is repeated with a "
             "different model made every repetition", "a type of program development cycle in which different parts of "
             "the requirements are developed in parallel, using prototyping to provide early user involvement in "
             "testing.", "(wireless) access point which allows a device to access a LAN without a wired connection.",
             "A general purpose register that stores a value before and after the execution of an instruction by the "
             "ALU", "carries the addresses throughout the computer system.", "software that quarantines and deletes "
             "files or programs infected by a virus (or other malware); it can be run in the background or initiated "
             "by the user.", "a computer program that translates programming code written in assembly language into "
             "machine code", "number of bits per second that can be transmitted over a network; it is a measure of the "
             "data transfer rate over a digital telecoms network", "image is made up of a grid of rows and columns "
             "where a specific cell is given a colour value.", "A data type that only has two values, true or false",
             "Cable made up of central copper core, insulation, copper mesh and outer insulation"]

answers = ["abstraction", "alphatesting", "boundarytestdata", "waterfallmodel", "iterativemodel",
           "rapidaccessdevelopment", "wirelessaccesspoint", "accumulator", "addressbus", "antivirussoftware",
           "assembler", "bitrate", "bitmap", "boolean", "coaxialcable"]
score = 0
lives = True

while lives:
    qnum = random.randrange(len(questions))
    print(answers[qnum])
    a = input(questions[qnum])
    a = a.lower()
    a = a.replace(" ", "")
    if a == answers[qnum]:
        print("That was correct")
        score = score + 1
    else:
        print("That was not correct")
        print("Score =", score)
        lives = False

with open("Highscores", "r") as check:
    for line in check:
        if score > int(line):
            print("New high score set!")
            with open("Highscores", "w") as highscore:
                highscore.write(str(score))
        else:
            print("Current high score is:", line)
