# Alfred-To-MD
A script to convert [Alfred](https://www.alfredapp.com/) snippets to markdown format.

## Summary
In my opinion, Alfred has to be one of the most useful desktop applications for Mac OS and I use it hundreds of times daily to pull out 'snippets'. My snippets contain information that's very useful and time-saving in my daily work, however I loose access to those snippets when not in the office.
I use [Gitbook](https://github.com/GitbookIO/gitbook) to keep track of my notes and documentation, but the glaring omission was access to my Alfred snippets when off-site or working remotely.

This Python script will convert a directory full of Alfred snippets, into one markdown file that can be then easily imported into any documentation collation tool (such as Gitbook).

## Installation
1. Set up Alfred so that you have your preferences synced to a directory on your computer. You can extract the snippets directly from the application itself but this method is cleaner.
2. Clone this repository onto your computer

## Usage

Run the script in this format:
`python3 alfred-to-md.py /Users/dw/Sync/Alfred/Alfred.alfredpreferences/snippets/`

By default it will output all content into a new (or newly emptied) file named `alfred.md` in the script directory.
