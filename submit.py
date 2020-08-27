import time
import os

def predict():
    '''
    TO DO: Contestant's code
    '''
    print ("Processing...")
    os.chdir("/opt/ai/submit/")
    os.system('sh todo.sh')

if __name__ == '__main__':
    predict()
    
