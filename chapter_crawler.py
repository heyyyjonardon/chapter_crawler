from tkinter import *
from selenium import webdriver

#x = webdriver.Firefox()

def next_chapter():
    x.get('https://www.learncbse.in/cbse-notes-class-11-chemistry/')
    xpath = "/html/body/div[1]/div[1]/div/main/article/div/div[2]/ul/li[{}]/a".format(int(input_field.get()))
    chap = x.find_element_by_xpath(xpath)
    chap.click()
    
#

widget = Tk()

var = StringVar()
text = Label(widget,textvariable=var)
var.set('Enter next chapter to jump to: ')
text.grid()

input_field = Entry(widget)
input_field.grid()


jump = Button(widget,text="JUMP",command=next_chapter)
jump.grid()

quit_button = Button(widget,text="Hmm..QUIT!",command=widget.quit)
quit_button.grid()


widget.title('Chapter Crawler')

widget.geometry('200x100')

widget.mainloop()
