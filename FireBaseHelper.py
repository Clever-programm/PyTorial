import pyrebase
import random
from collections import OrderedDict

config = {
    'apiKey': "AIzaSyB6G4YjrKMSkJl_h58aE_eb307SPumSRyQ",
    'authDomain': "cleverproductionpytorial.firebaseapp.com",
    'projectId': "cleverproductionpytorial",
    'databaseURL': 'https://cleverproductionpytorial-default-rtdb.firebaseio.com/',
    'storageBucket': "cleverproductionpytorial.appspot.com",
    'messagingSenderId': "1078729198626",
    'appId': "1:1078729198626:web:707b3b1da05a4c8dd48e7b",
    'measurementId': "G-5RLJL76Y7V"
}

firebase = pyrebase.initialize_app(config)
pytorial_storage = firebase.database()


# print(pytorial_storage.child('PyTorialTables').child('Users').get().val().keys())


def NEW_USER(nickname, email, password):
    pass


def FIND_USER_BY_CID(CID):
    pass


def FIND_USER_BY_EMAIL(email):
    pass


def CHECK_USER_SIGN(email, password):
    pass