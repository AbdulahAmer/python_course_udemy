blog_posts = ["","post1","post2","","post3",""]

for post in blog_posts:
    if post == "":
        continue
    else:
        print(post)
    
mystring = "String over here"

for letter in mystring:
    print(letter)

    #the one above prints every character in a string, including spaces

for x in range(0,10):
    print(x)


person = {"name":"Paul Torres","place":"New York","age":30,"gender":"male"}

for stat in person:
    print(stat,":",person[stat])



blog_posts = {"python":["post1","post2","post3"],"java":["post1","post2","post3"]}


for cat in blog_posts:
    print("Posts", cat)
    for key in blog_posts[cat]:
        print(key)
