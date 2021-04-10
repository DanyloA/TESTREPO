def count_str(str):
    answ=0
    for i in str:
        if i==',' or i=='.' or i=='!' or i=='?' or i=='-' or i==':' or i==';' or i=='/n' or i==' ':
            answ+=1
    return answ
print(count_str('wwdqwdwdqwdqwdqwdqwdqdw wqdqwdqwdqwd dqwdqwdqwdqwdqwdqwd;fefwefwefewfe:wefwefwef'))
