print("привіт давай зіграємо в гру,введи ім'я!")
name=str(input(""))
print("введи число (1=гра вгадай число,2=гра вгадай слово)")
h=int(input(""))
if h<2 and h>0:
    import random
    input_number=0
    print("давай починати", name ,"я загадав число від 1 до 20")
    number=random.randint(1,20)
    while input_number<5:
        play=int(input("ану вгадай:"))
        input_number=input_number+1
        if play<number:
            print("моє число більше!")
        if play>number:
            print("моє число менше!")
        if play==number:
            print("вітаю!ти вгадав!!!")
            break
    print("число було",number)
if h>1 and h<3:
    k=[]
    k="ABOVE","BELOW","BEFORE","BEHIND","UNDER","OVER","AT","IN","ON"

    import random
    input_number=0
    print("давай починати", name ,"я загадав прийменники Above ,Below ,Before,Behind,Under,Over,At,in,on")
    number=random.randint(0,8)
    numblen=len(k[number])
    while input_number<5:
        play=input("ану вгадай:")
        play=play.upper()
        input_number=input_number+1
        if len(play)<len(k[number]):
            print("моє слово більше!")
        if len(play)>len(k[number]):
            print("моє слово менше!")
        if len(play)==len(k[number]):
            print("вітаю!ти вгадав!!!")
            break
