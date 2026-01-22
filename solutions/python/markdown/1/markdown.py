import re

def parse(markdown):
    print(markdown)
    lines = markdown.split('\n')
    output = ''
    list_started = False

    for i, line in enumerate(lines):
        if line[:8] == '####### ': line = '<7h>' + line[8:]
        if line[:7] == '###### ': line = '<h6>' + line[7:] + '</h6>'
        if line[:6] == '##### ': line = '<h5>' + line[6:] + '</h5>'
        if line[:5] == '#### ': line = '<h4>' + line[5:] + '</h4>'
        if line[:4] == '### ': line = '<h3>' + line[4:] + '</h3>'
        if line[:3] == '## ': line = '<h2>' + line[3:] + '</h2>'
        if line[:2] == '# ': line = '<h1>' + line[2:] + '</h1>'
        if line[:2] == '* ':
            if list_started == False:
                line = re.sub("(\* )(.+)", lambda m: '<ul><li>' + m.group(2) + '</li>', line)
                list_started = True
            else:
                line = re.sub("(\* )(.+)", lambda m: '<li>' + m.group(2) + '</li>', line)
                if i == len(lines)-1: line += '</ul>'
        else:
            if list_started == True:
                output += '</ul>'
                list_started = False

        if all([line[:2] != '<h', line[:4] != '<ul>', line[:4] != '<li>']): line = '<p>' + line + '</p>'
        line = re.sub("(<7h>)(.+)", lambda m: '####### ' + m.group(2), line)
        line = re.sub("(__)(.+)(__)", lambda m: '<strong>' + m.group(2) + '</strong>', line)
        line = re.sub("(_)(.+)(_)", lambda m: '<em>' + m.group(2) + '</em>', line)
        output += line

    return output
