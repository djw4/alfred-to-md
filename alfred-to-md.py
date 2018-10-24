import os, json, sys, glob


try:
    file_dir = sys.argv[1]
except:
    print('No directory supplied!')
    exit()

output_file = 'alfred.md'

# Create, or empty the output file
open(output_file, 'w').close()

with open(output_file, 'a') as output:
    for f in glob.iglob(file_dir + "/*/*", recursive=True):
        f = os.path.abspath(f)
        if os.path.isfile(f):
            if f.endswith('.json'):
                with open(os.path.join(file_dir, f)) as r:
                    data = json.load(r)
                    snippet_header = data['alfredsnippet']['name']
                    snippet_text = data['alfredsnippet']['snippet']
                    
                    output.write('#### ' + snippet_header + '\n')
                    output.write('```' + '\n' + snippet_text + '\n' + '```' + '\n\n')
        else:
            pass
