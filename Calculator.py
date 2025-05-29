from tkinter import *
import math as m

window= Tk()
window.geometry("400x750+470+20")
#window.minsize(400,600)
#window.maxsize(500,800)
window.title("Simple Calculator")
window.config(bg="gray25")
window.resizable(True,True)
#window.overriderected(1)

def close():
    window.destroy()

def clear():
    entry.delete(0,"end")

def back():
    last_number=len(entry.get())-1
    entry.delete(last_number)

def press(input):
    length=len(entry.get())
    entry.insert(length,input)

def add(a,b):
    return float(a)+float(b)
def subtract(a,b):
    return float(a)-float(b)
def multiply(a,b):
    return float(a)*float(b)
def divide(a,b):
    return float(a)/float(b)

def expression_break(sign,expression):
    values=expression.split(sign,1)
    return values

def scientific(expression):
    data=expression_break("(",expression)
    if data[0]=="tan":
        result=m.tan(float(data[1]))
    elif data[0]=="cos":
        result=m.cos(float(data[1]))
    elif data[0]=="sin":
        result=m.sin(float(data[1]))
    elif data[0]=="sqrt":
        result=m.sqrt(float(data[1]))
    elif data[0]=="log":
        result=m.log10(float(data[1]))
    elif data[0]=="ln":
        result=m.log(float(data[1]))
    elif data[0]=="deg":
        result=m.degrees(float(data[1]))
    elif data[0]=="rad":
        result=m.radians(float(data[1]))
    elif data[0]=="fac":
        number=float(data[1])
        if number.is_integer() and number >=0:
            result=m.factorial(int(number))
    
        else:
            raise ValueError("Factorial is only defined for non-negative integers.")
    return result

def equal():
    expression=entry.get()
    clear()
    try:
        if expression.find("(")>0:
            result=scientific(expression)
        elif expression.find("pow")>0:
            data=expression_break("pow",expression)
            result=m.pow(float(data[0]),float(data[1]))
        elif expression.find("rem")>0:
            data=expression_break("rem",expression)
            result=m.remainder(float(data[0]),float(data[1]))
        elif expression.find("X")>0:
            data=expression_break("X",expression)
            result=multiply(data[0],data[1])
        elif expression.find("x")>0:
            data=expression_break("x",expression)
            result=multiply(data[0],data[1])
        elif expression.find("*")>0:
            data=expression_break("*",expression)
            result=multiply(data[0],data[1])
        elif expression.find("÷")>0:
            data=expression_break("÷",expression)
            result=divide(data[0],data[1])
        elif expression.find("/")>0:
            data=expression_break("/",expression)
            result=divide(data[0],data[1])
        elif expression.find("+")>0:
            first=expression.find("+")
            second=expression.find("+",(first+1),(first+5))
            if first>second:
                data=expression_break("+",expression)
                result=add(data[0],data[1])
            else:
                result=add(expression[0:second],expression[second+1:])
        elif expression.rindex("-")>0:
            sign=expression.rindex("-")
            result=subtract(expression[0:sign],expression[sign+1:])

        entry.insert(0,result)

    except:
        entry.insert(0,"Error")
        

entry_string=StringVar()
entry= Entry(window,textvariable= entry_string, foreground="White",background="Black",
             border=2,font=("Times New Roman",30))
entry.grid(columnspan=4,ipady=15)

font_value=("Times New Roman",18)
btn_tan=Button(window,text="tan",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press("tan("))
btn_tan.grid(row=1,column=0,sticky=E+W,ipady=15)

btn_cos=Button(window,text="cos",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press("cos("))
btn_cos.grid(row=1,column=1,sticky=E+W,ipady=15)

btn_sin=Button(window,text="sin",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press("sin("))
btn_sin.grid(row=1,column=2,sticky=E+W,ipady=15)

btn_sqrt=Button(window,text="sqrt",background="gray20",foreground="White",font=font_value,
                borderwidth=1,relief=SOLID,command= lambda:press("sqrt("))
btn_sqrt.grid(row=1,column=3,sticky=E+W,ipady=15)

btn_log=Button(window,text="log",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press("log("))
btn_log.grid(row=2,column=0,sticky=E+W,ipady=15)

btn_ln=Button(window,text="ln",background="gray20",foreground="White",font=font_value,
              borderwidth=1,relief=SOLID,command= lambda:press("ln("))
btn_ln.grid(row=2,column=1,sticky=E+W,ipady=15)

btn_deg=Button(window,text="deg",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press("deg("))
btn_deg.grid(row=2,column=2,sticky=E+W,ipady=15)

btn_rad=Button(window,text="rad",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID, command= lambda:press("rad("))
btn_rad.grid(row=2,column=3,sticky=E+W,ipady=15)

btn_fac=Button(window,text="fac",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press("fac("))
btn_fac.grid(row=3,column=0,sticky=E+W,ipady=15)

btn_pow=Button(window,text="pow",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press("pow"))
btn_pow.grid(row=3,column=1,sticky=E+W,ipady=15)

btn_rem=Button(window,text="rem",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press("rem"))
btn_rem.grid(row=3,column=2,sticky=E+W,ipady=15)

btn_pie=Button(window,text="π",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID, command= lambda:press(3.141592))
btn_pie.grid(row=3,column=3,sticky=E+W,ipady=15)

btn_clr=Button(window,text="C",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID, command= clear)
btn_clr.grid(row=4,columnspan=2,column=0,sticky=E+W,ipady=15)

btn_back=Button(window,text="⌫",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID, command= back)
btn_back.grid(row=4,columnspan=2,column=2,sticky=E+W,ipady=15)

btn_seven=Button(window,text="7",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press(7))
btn_seven.grid(row=5,column=0,sticky=E+W,ipady=15)

btn_eight=Button(window,text="8",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press(8))
btn_eight.grid(row=5,column=1,sticky=E+W,ipady=15)

btn_nine=Button(window,text="9",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press(9))
btn_nine.grid(row=5,column=2,sticky=E+W,ipady=15)

btn_div=Button(window,text="÷",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press("÷"))
btn_div.grid(row=5,column=3,sticky=E+W,ipady=15)

btn_four=Button(window,text="4",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press(4))
btn_four.grid(row=6,column=0,sticky=E+W,ipady=15)

btn_five=Button(window,text="5",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press(5))
btn_five.grid(row=6,column=1,sticky=E+W,ipady=15)

btn_six=Button(window,text="6",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press(6))
btn_six.grid(row=6,column=2,sticky=E+W,ipady=15)

btn_mul=Button(window,text="*",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press("*"))
btn_mul.grid(row=6,column=3,sticky=E+W,ipady=15)

btn_one=Button(window,text="1",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press(1))
btn_one.grid(row=7,column=0,sticky=E+W,ipady=15)

btn_two=Button(window,text="2",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press(2))
btn_two.grid(row=7,column=1,sticky=E+W,ipady=15)

btn_three=Button(window,text="3",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID, command= lambda:press(3))
btn_three.grid(row=7,column=2,sticky=E+W,ipady=15)

btn_sub=Button(window,text="-",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press("-"))
btn_sub.grid(row=7,column=3,sticky=E+W,ipady=15)

btn_dot=Button(window,text=".",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press("."))
btn_dot.grid(row=8,column=0,sticky=E+W,ipady=15)

btn_zero=Button(window,text="0",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command =lambda:press(0))
btn_zero.grid(row=8,column=1,sticky=E+W,ipady=15)

btn_e=Button(window,text="e",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press(2.71828))
btn_e.grid(row=8,column=2,sticky=E+W,ipady=15)

btn_add=Button(window,text="+",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= lambda:press("+"))
btn_add.grid(row=8,column=3,sticky=E+W,ipady=15)

btn_equals=Button(window,text="=",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID,command= equal)
btn_equals.grid(row=9,columnspan=3,column=0,sticky=E+W,ipady=15)

btn_close=Button(window,text="close",background="gray20",foreground="White",font=font_value,
               borderwidth=1,relief=SOLID, command= close)
btn_close.grid(row=9,columnspan=1,column=3,sticky=E+W,ipady=15)

mainloop()
