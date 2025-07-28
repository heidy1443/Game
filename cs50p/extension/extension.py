type={".gif":"image/gif.",
        ".jpg":"image/jpeg",
        ".jpeg":"image/jpeg",
        ".png":"image/png",
        ".pdf":"application/pdf",
        ".txt":"text/plain",
        ".zip":"application/zip"}

file=input().lower()

for e in type:
    if file.endswith(e):
        print (type[e])
        break
    
else:
        print("application/octet-stream")