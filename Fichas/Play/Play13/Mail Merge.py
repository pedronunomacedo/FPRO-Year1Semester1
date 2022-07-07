def mail_merge(names, mail_template):
    nf = open(names, "r", encoding='utf-8')
    mf = open(mail_template, "r", encoding='utf-8')
    txt = mf.read()
    s = []
    
    for i in nf.readlines():
        s.append(txt.replace("<name>",i.rstrip("\n")))
        
    return s

print(mail_merge('names.txt', 'template.txt'))