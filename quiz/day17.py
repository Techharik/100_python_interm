''' Create our own classes '''

# class sytax
#first letter of the name is captialized.

# class User:
#      def __init__(self):
#          pass
     

# user_1 = User()

# user_1.id="001"
# user_1.name:'Employee-1'


# print(user_1.id)

#constructor: def __init__(self)
# Used to initialise the class



# attribute - variable
# methods - function


# class User:
#     def __init__(self,user_id,username) :
#         self.id=user_id
#         self.username=username
#         self.followers=0 #default value is setted.
#         self.followings=0 #default value is setted.

#     def follow(self,user):
#         user.followers +=1
#         self.followings +=1




# user_1 =User('001','Siva')
# user_2 =User('002','Jack')

# user_1.follow(user_2)  

# print(user_1.followers)
# print(user_1.followings)
# print(user_2.followers)
# print(user_2.followings)


from data import question_data



class Question:
    def __init__(self,question,answer):
        self.question_text   =question
        self.question_answer =answer
    


question_bank = []

for question in question_data:
    question_text =question['text']
    question_answer = question['answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


class Quiz:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list =q_list
        self.score = 0

    def still_has_a_question(self):
        return len(self.question_list) > self.question_number
        
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number +=1
        ans = input(f"Q:{self.question_number}:- {question.question_text } ? (True / False)")

        if(ans.lower() == question.question_answer.lower()):
            print("You got it correct")
            print(f"That's correct answer {self.score} / {self.question_number}")
            self.score += 1
        else:
            print("That's worng")
            print(f"That's correct answer {question.question_answer}")
            print(f"That's correct answer {self.score} / {self.question_number}")
            print("\n")


quiz = Quiz(question_bank)


while quiz.still_has_a_question():
    quiz.next_question()

print('You got the correct answer')
print(f"your final score was:{quiz.score} / {quiz.question_number}")