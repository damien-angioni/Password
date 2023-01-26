import hashlib
import json
def main():
    process=True
    while (process == True):
        chk_majuscule=False
        chk_minuscule=False
        chk_cardinal=False
        Password = input("Saisissez votre mot de passe: ")
        if (len(Password)<8):
            print("Mont de passe trop court, veuillez essayer à nouveau")
            process = True
        else:
            if(Password.find("!")>=0) or (Password.find("@")>=0) or (Password.find("#")>=0) or (Password.find("$")>=0) or (Password.find("%")>=0) or (Password.find("*")>=0) or (Password.find("&")>=0) or (Password.find("^")>=0):
                for i in Password:
                    if i.isupper():
                        chk_majuscule=True
                if(chk_majuscule==True):
                    for j in Password:
                        if j.islower():
                            chk_minuscule=True
                    if(chk_minuscule==True):
                        for k in Password:
                            if k.isnumeric():
                                chk_cardinal=True
                        if(chk_cardinal==True):
                                print("Mot de passe correct")
                                process=False
                        else:
                            print("votre mot de passe doit contenir au moins un chiffre.")
                            process=True
                    else:
                        print("votre mot de passe doit contenir au moins une minuscule.")
                        process=True
                else:
                    print("votre mot de passe doit contenir au moins une majuscule.")
                    process=True
            else:
                print("Veuillez insérer au moins un caracrtère spécial dans votre mot de passe.")
                process=True
        Mashword=hashlib.sha256(Password.encode()).hexdigest()
        print("Mot de passe après Hashing:",Mashword)
        JSON_pw = {"Password":Mashword}
        file=open("Passwords.json", "a")
        json.dump(JSON_pw,file)
        print("pret à rentrer un nouveau mot de passe!")
        process=True
main()  