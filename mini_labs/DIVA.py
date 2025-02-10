def cipher(s):
#s="Eternity is far too cruel a fate for you"
    words=s.split()
    rev=[i[::-1] for i in words]
    s1=""
    for v in rev:
        s1=s1+v+" "
    print("Зашифрованное сообщение:",s1)
print("Введите сообщение, которое нужно зашифровать")
s2=input()
print("Введите сообщение, которое нужно расшифровать")
s3=input()
def decipher(s):
    words = s.split()
    rev = [i[::-1] for i in words]
    s1 = ""
    for v in rev:
        s1 = s1 + v + " "
    print("Расшифрованное сообщение:",s1)
cipher(s2)
decipher(s3)
