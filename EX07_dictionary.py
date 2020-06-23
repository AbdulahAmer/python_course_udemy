person = {"name":"Paul","gender":"male","age":30,"address":"690","phone":917}
question = input("What information do you want?: ").lower()
print(person.get(question,"That information is not available"))
