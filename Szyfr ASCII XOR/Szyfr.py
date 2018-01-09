def wejsciowe():
    szyfr = raw_input("Wpisz szyfr: \n")
    kod = int(raw_input("Wpisz kod: \n"))
    print kod

    if kod > 255:
        print ("Error: za wysoka wartosc klucza")
        raise SystemExit


    klucz = int(kod)
    klucz_dziesietny = "{0:b}".format(klucz)
    klucz_decmb = 8 - len(klucz_dziesietny)
    klucz_f = "0" * klucz_decmb + klucz_dziesietny
    wyn = ''


    for i in range(len(szyfr)):
            l1 = szyfr[i]
            l1_dec = ord(l1)
            l1_x = "{0:b}".format(l1_dec)
            l1_lenx = len(l1_x)
            l1_mb = 8 - l1_lenx
            l1_f = "0" * l1_mb + l1_x
    xor1 = ''
    for j in range(0, 8):
            if l1_f[j] == klucz_f[j]:
                xor1 = xor1 + "0"
            else:
                xor1 = xor1 + "1"
    wyn = wyn + chr(int(xor1, 2))


    text_file = open("kod.txt", "w")
    text_file.write("-"wyn+"-z kodem" + str(kod))
    print ("Zaszyfrowana wiadomosc zostala zapisana w folderze kod.txt")


wejsciowe()
