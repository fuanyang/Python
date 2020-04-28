# Name Fu An Yang
# StudentId 1051888
# Date 4/28/2020

def build_catalog_entry (Title, Author, Publisher):
    bookinfo={}
    bookinfo["Title"]=Title
    bookinfo["Author"]=Author
    bookinfo["Publisher"]=Publisher
    return bookinfo

active=True
library_catalog=[]
while True:
    Title=input("Title:")
    Author=input("Author:")
    Publisher=input("Publisher:")
    x=build_catalog_entry(Title, Author, Publisher)
    library_catalog.append(x)
    ans=input("Enter another book? Y/N")
    if ans.upper()=="N" :
        break
print("-------------------------------------------")
print("Library Catalog")
print("-------------------------------------------")
for i in library_catalog:
    for j,q in i.items():
        if j=="Title":
            print("-----" + i[j] + "-----")
        else:
            print(j + ":" +q)
    