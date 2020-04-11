import os


# current directory of config.py
path = os.path.dirname(__file__)


#project parameters
options = {
    "port" : 8080
}

#project setting, default debug = false, whereas it should be switched to true in developing phase
settings = {
    "debug" : True,
    "template_path" : os.path.join(path,"template"),
    "static_path" : os.path.join(path,"static"),
    "model path" :os.path.join(path,"model")
}