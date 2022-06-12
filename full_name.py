# full name program string
# these are f-strings, f is for format b/c python formats the string, by replacing any names in braces with its value.
# previous to python 3.6 f-strings do not work, will need to use format()
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

full_name =  "{} {}".format(first_name, last_name)
print(full_name)
full_name =  "Hello {} {}".format(first_name, last_name)
print(full_name)

print("Languages:\n\tPython\n\tC\n\tJavaScript")

