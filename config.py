import os

# current directory of config.py
path = os.path.dirname(__file__)


#parameters
options = {
    "port" : 8080
}

#set static path and template_path
#default debug = false, whereas it should be switched to true in developing mode
#set XSRF protection
settings = {
    "debug" : True,
    "autoreload":True,
    "xsrf_cookies" :True,
    "cookie_secret":"586610e97b5142838e51ff6cd2cc73dc",
    "template_path" : os.path.join(path,"template"),
    "static_path" : os.path.join(path,"static"),
    "model path" :os.path.join(path,"model")
}