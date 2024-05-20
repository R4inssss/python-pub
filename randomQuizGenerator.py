#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along with the answer key.
import random

# The quiz data
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# our dictionary with states and capitals as key and values respectively

for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
    # open close w
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')
    # Here, we create 2 variables
    # the quizfile variable creates a filename for the quizzes, then adds a number + 1 for each instance
    # the answerkeyfile does the same, but for the answers
    # each variable assigns it 35 times, and opens it with the 'w' method to open the file in write mode
    # the for loop initially made will let us iterate this variable 35 times when called

    # TODO: Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum + 1})')
    quizFile.write('\n\n')
    # Here, we run our initial quizFile variable with the .write method.
    # the initial .write gives us a header for name/date/period
    # the second writes our quiz title with the Form (number), with the '' * 20 used for indentation
    # the \n\n are line breaks

    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    # states variable is assigned to a list of our capital keys using the keys method
    # we then randomize the variable states using the random.shuffle method

    # TODO: Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        # here, we make another function with the range of 50
        # we assign correct answer to iterate through the range of 50 through the value of the keys as a list
        # we then iterate wrong answers as a list of the values of the capitals, deleting the correct answer, then selecting 3 random
        # values from the list. as seen by wrong answers = random.sample(wrongAnswers, 3)
        # we then create the full list, but using a combination of the 2 variables wrong answer and correct answer
        # after, we randomize it with the random.shuffle method and pass (answerOptions) through it.

        # TODO: Write the question and answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. {answerOptions[i]}\n")
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")
        # Our quizfile.write creates the number for us, which passes the questionNum variable + 1 for the current number
        # because we start at 0
        # Then, we iterate the dictionary of states passing through our variable as a list of numbers, where our list is
        # the range of questionNum, which is 50.
        # we then create a for loop, passing through each iteration 4 times
        # this is because it treats the string 'abcd' as an array and will evaluate it to 'A' 'B' 'C' and 'D'. on each iteration
        # and it writes a line break
        # the answerkey can be thought of the same way, except a cool index method is used!
    
    quizFile.close()
    answerKeyFile.close()
    # then we close the files

# Todo
# Creates 35 different quizzes 
# Creates 50 multiple-choice questions for each quiz, in random order
# Provides the correct answer and three random wrong answers for each question, in random order
# Writes the quizzes to 35 text files 
# Writes the answer keys to 35 text files
