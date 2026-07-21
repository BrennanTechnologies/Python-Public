'''
pip freeze > requirements.txt
    pip install --upgrade -r requirements.txt
'''
### Install additional libraries:
# pip install numpy pandas matplotlib
# pip install scikit-learn tensorflow torch
# pip install nltk scikit-learn

### Standard Libraries:
import sys
import os
import random
import array as arr
import CB_Module as cb
from datetime import date
from datetime import datetime

#2 Import NLTK and scikit-learn:
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
nltk.download('vader_lexicon')


#3 Create and configure your dataset
texts = ["I love this!", "This is terrible.", "What a fantastic day!", "I hate this."]
labels = ["positive", "negative", "positive", "negative"]
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.25, random_state=1)



# from sklearn.metrics import recall_score
# recall = recall_score(y_true, y_pred, average='macro', zero_division=1)

#4 Transform the text data
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

#5 Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_counts, y_train)

#6 Evaluate the model
predicted = classifier.predict(X_test_counts)
print(metrics.classification_report(y_test, predicted))

#7 Test sentiment analysis
sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores("I absolutely love this!"))

############
exit()
############

class bcolors:
    HEADER  = '\033[95m'
    OKBLUE  = '\033[94m'
    OKCYAN  = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL    = '\033[91m'
    ENDC    = '\033[0m'
    BOLD    = '\033[1m'
    UNDERLINE = '\033[4m'

# ----------------------------------------
# MAIN:
# ----------------------------------------
def main():
    os.system('cls')

    func_name = sys._getframe().f_code.co_name 	# print(" *** __main__ ***")
    print(bcolors.HEADER + "\n\t EXECUTING: ==> \t ***** " + func_name + " *****" + bcolors.ENDC)

    #####################################
    ### Start: -- MAIN -- 
    #####################################
    
    string_var = "Hello World"
    print(string_var)

    string_var = "New Log"
    cb.write_log(string_var)

    #cb.lazygit() # See def end()

    #cb.show_colors()

    #print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

    #####################################
    ### End: -- MAIN --
    #####################################

    try:
        print("Try")
    except NameError:
        print ("Name Error")
    except TypeError: 
        print("Error: cannot add an int and a str")
    except ZeroDivisionError:
        print("Div by Zero")
    except:
        print("Other Error")
    else:
        print("Else")
    finally:
        print("Finally")

def begin():
    pass

def end():
    pass
    #cb.lazygit()

def module():
    pass

# ---------------------------------------- 
# Runtime Execution Mode:
# ----------------------------------------
# Run at Runtime
if __name__=="__main__": 
    begin()
    main() 
    end()
# Run on Import
if __name__!="__main__": 
    module()

