from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn.metrics import mean_squared_error
import pickle

def download_data(what = 'train'):
    url_train = 'https://gist.githubusercontent.com/mahadirz/c1fed0d25c8db3a406a62fffd0560446/raw/bf2f5f75a90cc63daea119c9d415b262f5e16ac4/train.csv'
    url_test = 'https://gist.githubusercontent.com/mahadirz/c1fed0d25c8db3a406a62fffd0560446/raw/bf2f5f75a90cc63daea119c9d415b262f5e16ac4/test.csv'
    if what == 'train':
        df = pd.read_csv(url_train, index_col = 0)
        df.to_csv('data/train.csv')
    elif what == 'test':
        df = pd.read_csv(url_test, index_col = 0)
        df.to_csv('data/test.csv')
    else:
        df = pd.read_csv(url_train, index_col = 0)
        df.to_csv('data/train.csv')
        df = pd.read_csv(url_test, index_col = 0)
        df.to_csv('data/test.csv')
        
def RMSE(model, test):
    return np.sqrt(mean_squared_error(model, test))
        
def perform_training(path = 'data/train.csv'):
    train = pd.read_csv(path, index_col = 0)
    X_train, y_train = train[['x1', 'x2']], train['y']
    
    param_grid = {
        'C': [0.01, 0.1, 0.5, 1, 10],
        'gamma': ['auto', 'scale'],
        'nu': [0.05, 0.1, 0.5, 0.7]
    }
    optimizer = GridSearchCV(svm.NuSVR(kernel = 'poly'), param_grid, cv = 4)
    optimizer.fit(X_train, y_train)
    return optimizer

def save_model(model):
    filename = 'data/nusvm_model.sav'
    pickle.dump(model, open(filename, 'wb'))
    #load it later
    #loaded_model = pickle.load(open(filename, 'rb'))



        

class Command(BaseCommand):
    help = 'run ML model'
    def add_arguments(self, parser):
        #parser.add_argument('action', type = str, help = 'Indicates what action I should do')
        parser.add_argument('-p', '--download', type = str, help = 'should I download file or not: [yes, no]')
        #parser.add_argument('-p', '--what', type = str, help = 'what I have to download: [train, test, all]')


    def handle(self, *args, **kwargs):
        download = kwargs['download']
        #what = kwargs['what']
        #if what not in ['train', 'test', 'all']:
        #    what = 'train'
        what = 'train'
        if download == 'yes':
            download_data(what)
            self.stdout.write('Data downloaded from GitHub')
        else:
            self.stdout.write('Data downloading passed')
        model = perform_training(path = 'data/train.csv')
        self.stdout.write('Model was trained')
        save_model(model)
        self.stdout.write('Model was saved')