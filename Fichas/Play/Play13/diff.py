import difflib
def diff(filename1, filename2):
    result = ''
    with open(filename1) as f1:
        f1_text = f1.readlines()
    with open(filename2) as f2:
        f2_text = f2.readlines()
    # Find and print the diff:
    for line in difflib.unified_diff(f1_text, f2_text,                 fromfile='f1', tofile='f2', lineterm=''):
        if line.startswith('-') or line.startswith('+'):
            result += line
    return result.replace('--- f1+++ f2', '').replace('-', '- ').replace('+', '+ ')

print(diff('file1d.txt', 'file2d.txt'))