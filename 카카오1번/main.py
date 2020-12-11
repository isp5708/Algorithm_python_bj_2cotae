def solution(new_id):
    specialCharacter = ['~', '!','@','#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', '{', ']', '}', ':', '?',
                        ',', '<', '>']
    #1단계
    new_id = new_id.lower()

    #2단계
    end=len(new_id)
    i=0
    while i<end:
        if new_id[i] in specialCharacter:
            new_id=new_id.replace(new_id[i],'',1)
            end-=1
            continue
        i+=1

    #3단계
    while '...' in new_id :
        if '...'in new_id:
            new_id=new_id.replace('...','.')

    if '..'in new_id:
        new_id=new_id.replace('..','.')

    #4단계
    if new_id.startswith('.'):
        new_id=new_id[1:len(new_id)]

    if new_id.endswith('.'):
        new_id=new_id[:len(new_id)-1]

    #5단계
    if new_id=='':
        new_id='a'

    #6단계
    if len(new_id)>=16:
        new_id=new_id[:15]

        if new_id.endswith('.'):
            new_id = new_id[:len(new_id) - 1]

    #7단계
    if len(new_id)<=2:
        tmp=new_id[len(new_id)-1]
        while len(new_id)!=3:
            new_id=new_id+tmp
    return new_id


