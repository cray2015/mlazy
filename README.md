# mlazy
A python utility for people who love markdown, this utility helps you create a note application within your Git repo.

> mlazy stands for "I'm lazy"  - that I'm very much

## Creation Story
I like to write and create notes on the fly. I wasn't able to find anything as simple as markdown and next to free notes app. Also I'm a paranoid person who doesn't like to share the data with anyone (I know they are still watching - booyah!). 

So I recently fell in love with Markdown. Its ease, flexibility and limited formatting capabilities made it possible for me to create notes quickly on the fly. As I already created 10-15 notes I realized I need some kind of utility to make this process more fluid and intuitive. Coming from the Angular background I loved their CLI and how effective it is in terms of abstracting the boilerplate creation and linking. So I thought of writing this utility which will help to facilitate these needs of basic housekeeping within the CLI. 

Also I have been developer since the start of my career(Now focusing on my DevOps career). I always wanted to contribute to a Open Source project. So this is my offering to the community. 


## How to Use

### Actions

Following actions are allowed with the utility.

- create/c - to create the document - provide a file name
- delete/d - to delete the document - provide a file name
-   list/l - to list all documents
-   init/i - initialize the notes directory - provide a folder name or I will use the default one "notes"

### Command format
1. Initialize the directory this will create a .mlazy_config and the default "note" directory in the root directory- 
            
        ./mlazy i optional_folder_name

2. Create notes in the notes directory and add file name as header in the note file


        ./mlazy c file_name_without_md_extension

3. List all notes 

        ./mlazy l

4. Delete note 

        ./mlazy d filename_without_md_extension

## Future plans
- House keeping of notes in the README file with hyperlinking
- Quick bookmarks facility
- Adding test cases