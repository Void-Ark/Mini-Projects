from tkinter import *
import difflib

# root window
root = Tk()

# title 
root.title("Plagiarism Checker")

# background color
root.configure(bg='#333333') # set background color to dark gray

# Set the window size
root.geometry('500x500')

# first input block
input_label_1 = Label(root, text="Text 1:", bg='#333333', fg='white', font=('Helvetica', 12, 'bold'))
input_label_1.pack(pady=5)
input_block_1 = Text(root, bg='#555555', fg='white', font=('Helvetica', 12), width=40, height=6)
input_block_1.pack(pady=5)

# second input block
input_label_2 = Label(root, text="Text 2:", bg='#333333', fg='white', font=('Helvetica', 12, 'bold'))
input_label_2.pack(pady=5)
input_block_2 = Text(root, bg='#555555', fg='white', font=('Helvetica', 12), width=40, height=6)
input_block_2.pack(pady=5)

# output block
output_label = Label(root, text="Plagiarism Score:", bg='#333333', fg='white', font=('Helvetica', 12, 'bold'))
output_label.pack(pady=5)
output_block = Label(root, bg='#555555', fg='white', font=('Helvetica', 12), height=2, width=30)
output_block.pack(pady=5)

#function to calculate the plagiarism score
def calculate_plagiarism_score():
    # Getting data
    text1 = input_block_1.get("1.0", END)
    text2 = input_block_2.get("1.0", END)

    # Remove newlines and extra spaces
    text1 = ' '.join(text1.split())
    text2 = ' '.join(text2.split())

    # Calculating the similarity score using the SequenceMatcher
    similarity_score = difflib.SequenceMatcher(None, text1, text2).ratio()

    # Display the plagiarism score as a percentage
    output_block.config(text=f"{similarity_score*100:.2f}%")

# Create a button to trigger the plagiarism checker
button = Button(root, text='Check Plagiarism', bg='#00a8e8', fg='white', font=('Helvetica', 12), command=calculate_plagiarism_score)
button.pack(pady=10)

# Run the main event loop
root.mainloop()
