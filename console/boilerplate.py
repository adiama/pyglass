# -*- coding: utf-8 -*-

import os
import sys
import re

DIRECTORIES = {
    "Model": "..{0}app{0}models{0}".format(os.sep),
    "View": "..{0}app{0}views{0}".format(os.sep),
    "Controller": "..{0}app{0}controllers{0}".format(os.sep)
}

PARAMETERS = {
    "-h": (lambda: show_help()),
    "-m": (lambda: create(["Model"], fname)),
    "-v": (lambda: create(["View"], fname)),
    "-c": (lambda: create(["Controller"], fname)),
    "-d": (lambda: create(["View", "Controller"], fname)),
    "-a": (lambda: create(["Model", "View", "Controller"], fname))
}

HELP_MESSAGE = """
  Description:
    Run with any of the following parameters followed by <Name>
    to generate the boilerplate code for custom classes

  File Name:
    <Name> should always be the last parameter
    <Name> format should be CamelCase without any symbols like <> or -

  Parameters:
    -h\t      help:  Show help message
    -m\t     model:  Create <Name>Model
    -v\t      view:  Create <Name>View
    -c\tcontroller:  Create <Name>Controller
    -d\t   default:  Create <Name>View and <Name>Controller
    -a\t       all:  Create <Name>Model and <Name>View and <Name>Controller"""

fname = None

def check_permissions():
    #check for permission to write files
    pass

def validate(parameters):
    global fname
    fname = parameters[-1]


    if len(parameters) > 2:
        #Sanitize fname
        if fname[0] == "-":
            if fname in PARAMETERS:
                error("Please provide a name", True)
            else:
                error("Unknown parameter \"%s\"" % fname, True)
        else:
            parameters = parameters[1:-1]
    else:
        parameters = [fname]

    #Find and replace Model/Controller/View in name
    regex = re.compile(r"Model|View|Controller|[0-9$-/:-?{-~!\"^_`\[\]\\#@]")
    find = regex.findall(fname)
    for f in find:
        for f in find:
            fname = fname.replace(f, "")

    if fname == "":
        error("Please provide a valid name", True)

    #Validate
    unique = []
    for p in parameters:
        if p not in PARAMETERS:
            error("Unknown parameter \"%s\"" % p, True)
        elif p not in unique:
            unique.append(p)

    parameters = unique

    #Execute
    for p in parameters:
        PARAMETERS[p]()

def get_boilerplate(type_):
    try:
        with open("boilerplates%s%s" % (os.sep, type_.lower()), 'r') as file:
            boilerplate = file.read()
        return boilerplate
    except FileNotFoundError:
        error("Could not find boilerplate file")
        return False

def create(types, name):
    for type_ in types:
        try:
            boilerplate = get_boilerplate(type_)
            boilerplate = boilerplate.replace("<Name>", name)
            with open("%s%s%s.py" % (DIRECTORIES[type_], name, type_),
                      'x') as file:
                file.write(boilerplate)
                success("%s%s.py created" % (name, type_))
        except FileExistsError:
            error("%s%s.py already exists." % (name, type_))
        except AttributeError:
            error("%s%s.py was not created" % (name, type_))

def error(message, kill = False):
    print("ERROR: %s" % message)
    if kill:
        sys.exit("Run -h for help")

def success(message):
    print("SUCCESS: %s" % message)

def show_help():
    print(HELP_MESSAGE)

def main():
    if len(sys.argv) < 2:
        error("Please provide parameters", True)
    check_permissions()
    validate(sys.argv)
    sys.exit(0)

if __name__ == "__main__":
    main()
