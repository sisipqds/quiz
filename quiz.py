print("Seja muito bem vindo ao quiz da Sisi!")
answer_user = input("Quer começar? (S/N)")
print(answer_user)
if answer_user != "S":
    quit()

score = 0

print("Começando...")
print("Qual foi o primeiro álbum de Michael Jackson? \n (A) Off the Wall \n (B) Leave Me Alone\n (C) Thriller \n (D) Bad \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")


print("Quando Thriller foi lançado? \n (A) 2001 \n (B) 1991\n (C) 1982 \n (D) 1979\n")
answer_2 = input("Resposta: ")
if answer_2 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")


print("Combine os álbuns com seus anos de lançamento: \n (A) Thriller - 1987 \n (B) Invencible - 1982\n (C) Bad - 2001 \n (D) Dangerous - 1991 \n")
answer_3 = input("Resposta: ")

if answer_3 == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")


print("A qual álbum essas músicas pertencem? Speed ​​Demon, Liberian Girl, Dirty Diana. \n (A) Dangerous \n (B) Bad\n (C) Thriller \n (D) Immortal \n")
answer_4 = input("Resposta: ")

if answer_4 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")


print("Quem foi a primeira esposa de Michael Jackson? \n (A) Tatum O'Neal \n (B) Lisa Maria Presley\n (C) Diana Ross\n (D)  Debbie Rowe\n")
answer_5 = input("Resposta: ")

if answer_5 == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")



print("Qual era o nome de seu chimpanzé de estimação que Jackson levaria em turnê? \n (A) Skip  \n (B) Bubbles \n (C) Akira \n (D)  Ben \n")
answer_6 = input("Resposta: ")

if answer_6 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

    print(f"Quiz acabou...  Pontuação: {score}/6")