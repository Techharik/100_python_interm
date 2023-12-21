# print("Understanding local filesystems")
# ? file system read wirte open and close files in our file systems

# file = open("my_file.txt")
# content = file.read()

# print(content)


# #!need to close in order to free up the resources.
# file.close()

#?another way

#mode - r - w - a 



# with open("my_file.txt",'a') as file:
#     # content = file.read()
#     file.write('new edit in this file')


# with open('./letters/starting_letter.txt') as letter:
with open('./input/Names/invited_letters.txt') as name:
        Names = name.read().split()
        for N in Names:
                with open('./input/letters/starting_letter.txt') as letter:
                        content = letter.read().replace('[name]', N)
                        with open(f'./input/output/ReadyToSend/letter_to_{N}','w') as mail:
                                mail.write(content)
