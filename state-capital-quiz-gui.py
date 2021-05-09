import sys, random
try:
    import PySimpleGUI as sg
except:
    print("PySimpleGUI not present; exiting...")
    sys.exit(1)

def readCapitalDataFile():
    # data file has state, abbreviation, join year, captial, and other city; tab separation
    data = []
    """returns list of list [state, abbreviation, join year, capital, other city] for each state"""
    try:
        cdf = open("states-and-capitals.txt","r")
    except IOError:
        print("Unable to read data file!")
        return data
    for line in cdf.readlines():
        if len(line) > 0 and line[0] == "#":
            # skip comments
            continue
        statedata = line.strip().split(chr(9))
        data.append(statedata)
    cdf.close()
    return data

def getQuestionCount(maxQuestions):
    # initial layout
    questionCount = [
        [sg.Text("States and Capitals Quiz")],
        [sg.Text("How many questions to ask?")],
        [sg.Slider((1,maxQuestions),5,orientation='h',key='count')],
        [sg.OK(),sg.Cancel()]]
    # actual window
    window = sg.Window("Question Count",questionCount)
    while True:
        # read events from window
        event, values = window.read()
        if event in (sg.WIN_CLOSED,'OK','Cancel'):
            break
    # values of controls from window.read()
    questionCount = int(values['count'])
    return questionCount

def askStateCapitalQuestion(stateData):
    """ ask an either-or question about the state """
    state = stateData[0]
    if random.randint(0,1)==0:
        correct = "A"
        cityA = stateData[3]
        cityB = stateData[4]
    else:
        correct = "B"
        cityA = stateData[4]
        cityB = stateData[3]
    question = [
        [sg.Text("States and Capitals Quiz")],
        [sg.Text("Which is the capital of "+state+"?")],
        [sg.Button(cityA,key="A"),sg.Button(cityB,key="B")]]
    window = sg.Window("Question", question)
    while True:
        # read events from window
        event, values = window.read()
        if event in (sg.WIN_CLOSED,'A','B'):
            break
    if event == correct:
        return 1
    else:
        return 0

def showQuizResults(correct, count, feedback):
    results = [
        [sg.Text("States and Capitals Quiz")],
        [sg.Text("You answered "+str(correct)+" out of "+str(count)+" correct")],
        [sg.Text(feedback)],
        [sg.OK()]]
    window = sg.Window("Results", results)
    while True:
        # read events from window
        event, values = window.read()
        if event in (sg.WIN_CLOSED,'OK'):
            break

def main():
    """
        Read data file, ask for question count,
        loop through randomized questions, show stats
    """
    #sg.popup("States and Capitals Quiz")
    #sg.theme_previewer()
    sg.theme("DefaultNoMoreNagging")
    quizdata = readCapitalDataFile()
    if len(quizdata) == 0:
        sg.popup("Unable to read quiz data file!")
        sys.exit(1)

    questionCount = getQuestionCount(len(quizdata))
    correctCount = 0
    reordered = quizdata[:]
    random.shuffle(reordered)
    feedback = ""
    for i in range(questionCount):
        result = askStateCapitalQuestion(reordered[i])
        if result == 1:
            correctCount += 1
        else:
            feedback += "\nThe capital of "+reordered[i][0]+" is "+reordered[i][3]
    if feedback == "":
        feedback = "Good job! No incorrect answers!"
    showQuizResults(correctCount, questionCount, feedback)

if __name__ == "__main__":
    main()
