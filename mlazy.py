#! /usr/bin/python

import sys
import os
import json

from os import listdir, remove
from os.path import isfile, join

# handle python version specific issues
from sys import version_info
if version_info.major == 3:
    pass
elif version_info.major == 2:
    try:
        input = raw_input
    except NameError:
        pass
else:
    print("Unknown python version - input function not safe")


ALLOWED_ACTIONS = ['create', 'c', 'delete', 'd', 'list', 'l', "init", "i"]
NOTES_PATH = './notes/'  # TODO read this from the config file
MLAZY_CONFIG_NAME = '.mlazy_config'

# TODO: handle mlazy actions from the calling directory


def failed():
    sys.exit(1)


def get_file_name(document_name):
    return document_name.replace(' ', '_') + '.md'


def get_file_path(file_name):
    return NOTES_PATH + file_name


def print_sample_command_format():
    # TODO
    pass


def create_new_document():
    load_mlazy_config()
    document_name = ''
    document_name = check_if_filename_provided()

    file_name = get_file_name(document_name)
    file_path = get_file_path(file_name)

    # if the directory does not exists then create
    # if not os.path.isfile(NOTES_PATH):
    #     print('Notes directory not found! creating')
    #     os.mkdir(NOTES_PATH)

    if document_name != '':
        if os.path.isfile(file_path):
            print('Cant create the specified file, as ' +
                  file_name + ' already exists')
            failed()
        with open(file_path, 'w') as fp:
            fp.write('# ' + document_name.replace('_', ' '))
            pass
        print(file_name + ' created successfully!')


def check_if_filename_provided():
    try:
        document_name = sys.argv[2]
    except:
        print('Oops document name not supplied')
        failed()
    return document_name


def delete_document():
    load_mlazy_config()
    # [x] if file exists?
    # [x] confirm and delete
    # TODO: update README list
    document_name = ''
    document_name = check_if_filename_provided()

    file_name = get_file_name(document_name)
    file_path = get_file_path(file_name)

    if document_name != '':
        if os.path.isfile(file_path):
            print('**Are you sure you want to delete ' + file_name + '?**')
            confirm_and_delete(file_path)
        else:
            print('Sorry the file ' + file_name+' was not found')


def confirm_and_delete(file_path):
    confirmation = input("Enter y/n: ")
    if confirmation.lower().__eq__('y') or confirmation.lower().__eq__('n'):
        if confirmation.lower().__eq__('y'):
            remove(file_path)
    else:
        print('The input is in incorrect format')
        confirm_and_delete(file_path)


def list_all_documents():
    load_mlazy_config()
    notes_files = [f for f in listdir(
        NOTES_PATH) if isfile(join(NOTES_PATH, f))]
    for file in notes_files:
        print(file)


def initialize_notes_directory():
    # create mlazy config for storing directory info
    # take folder_name from user or else use the default "notes"
    # check if directory exists
    # create a README in root for bookkeeping
    folder_name = 'notes'
    if sys.argv.__len__() > 2:
        # TODO folder names cant contains system values ., /,\ etc
        folder_name = sys.argv[2]
    if os.path.isfile(MLAZY_CONFIG_NAME):
        print('**The config already exists, has this directory been already initialized?**')
        print('Do you want to override?')
        print('Enter y/n: ')
    else:
        with open(MLAZY_CONFIG_NAME, 'w') as fp:
            fp.write('{"notes_directory": "' + folder_name + '" }')
            pass
        try:
            os.mkdir(folder_name)
        except:
            pass
        print('Folder initialized for mlazy notes')

    pass


def load_mlazy_config():
    global NOTES_PATH
    if os.path.isfile(MLAZY_CONFIG_NAME):
        mlazy_config = json.load(open(MLAZY_CONFIG_NAME))
        NOTES_PATH = './' + mlazy_config['notes_directory']+'/'
    else:
        print('This directory does not contains .mlazy_config file. Are you sure you initialized this directory with init action?')
        print('init/i - initialize the notes directory - provide a folder name or I will use the default one "notes"')
        failed()


def main():
    # TODO check if the mlazy config exists if not suggest to init
    action = ''
    if sys.argv.__len__() > 1:
        action = sys.argv[1]
    if action not in ALLOWED_ACTIONS:
        print('**Action not found**\nUse the below allowed actions:')
        print('create/c - to create the document - provide a file name')
        print('delete/d - to delete the document - provide a file name')
        print('  list/l - to list all documents')
        print('  init/i - initialize the notes directory - provide a folder name or I will use the default one "notes"')
        failed()
    else:
        if action.__eq__('create') or action.__eq__('c'):
            create_new_document()
        elif action.__eq__('delete') or action.__eq__('d'):
            delete_document()
        elif action.__eq__('list') or action.__eq__('l'):
            list_all_documents()
        elif action.__eq__('init') or action.__eq__('i'):
            initialize_notes_directory()


main()

print("I have reached at end")
