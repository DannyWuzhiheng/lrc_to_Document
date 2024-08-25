import ffmpeg
p1=r"D:\烤羊.lrc"
p2=r"D:\yjg.docx"
c=[]
with open(p1,"r",encoding='utf-8') as f:
    b = []
    a=f.read()
    a=a.split('\n')
iter = 0 
for i in a:
    i1 = i[11:]
    c.append(i1)
with open(p2,"w",encoding='utf-8') as f1:
    for i in c:
        f1.write(f'{i}\n')


