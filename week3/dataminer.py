import re


def main():
    infile="lvl1_bozuk_veri.txt"
    outfile="lvl1_temiz_rehber.txt"
    print("\n====FILE 1====")
    fileprocess(infile,outfile)
    infile="lvl2_bozuk_veri.txt"
    outfile="lvl2_temiz_rehber.txt"
    print("\n====FILE 2====")
    fileprocess(infile,outfile)

def fileprocess(infile,outfile):
    open(outfile, "w").close()
    print("Opening File...")
    mails,phones=fileop(infile)
    print("Printing mail details to the file...")
    mailop(mails,outfile)
    print("Printing phone details to the file...")
    phoneop(phones,outfile)

def fileop(name):
    mails=[]
    phones=[]
    with open(name,"r") as file:
        for row in file:
            mail=re.findall(r"[a-zA-Z0-9]+(?:[._+-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+(?:[.-][a-zA-Z0-9]+)*\.[a-zA-Z]{2,}",row)
            mails.extend(mail)
            phone=re.finditer(r"(?<!\d)(?:\+\d{1,3}[\s\-]*)?0?[\s\-]*(?:\(\s*\d{3}\s*\)|(?:\(0\s*\d{3}\s*\))|\d{3})[\s\-]*\d{3}(?:[\s\-]*\d{2}){2}(?!\d)|(?<!\d)(?:\+\d{1,3}[\s\-]*)?0?[\s\-]*(?:\(\s*\d{3}\s*\)|\d{3})[\s\-]*\d{3}[\s\-]*\d{4}(?!\d)",row)
            #no lies, took some help from gpt for phone regex
            for i in phone:
                phones.append(i.group().strip())
    return mails,phones

def mailop(mails,name):
    with open(name,"a") as file:
        file.write("Mails:\n")
        for mail in mails:
            file.write(f"{mail}\n")

def phoneop(phones,name):
    with open(name,"a") as file:
        file.write("Phones:\n")
        for phone in phones:
            file.write(f"{phone}\n")


if __name__=="__main__":
    main()