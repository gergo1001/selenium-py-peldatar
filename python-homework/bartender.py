kor=int(input("kérem adja meg az életkorát(csak egész szám): "))
ital=input("kérem adja meg mit szeretne rendelni (kóla vagy sör): ")
jo=True
if ital=="kóla":
    if kor>60:
        jo=False;
        print("a koffein megemelheti a vérnyomását")
elif ital=="sör":
    if (kor<18):
        jo=False;
        print("sajnos nem adhatok")
else:
    jo=False
    print("csak sör vagy kóla van")

if jo:
    print("itt a választott itala, ami "+ital)