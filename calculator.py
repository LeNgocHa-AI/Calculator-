import tkinter as tk
import math as m
from sympy import *
import re

expression = ["|"]
output = ""
ans = 0
enter_eq = 0
limit_low = -10**300
limit_high = 10**300
limit_low_result = 10**(-7)
limit_high_result = 10**10
mode = "d"
imag = "OFF"
deci = "OFF"
list_cal = ["sin(", "cos(", "tan(", "asin(", "acos(", "atan(", "log(", "frac(", "GCD(", "LCM(", "(", "√(", "π", "e", "∆"]
list_num = ["0", "1", "2", "3", "4", "5", "6", "7" ,"8", "9", ".", ")", "∆", "π", "e"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
power_number = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
out1_cache = ""
out2_cache = ""
expression_cache = []
cache_count = -1

def output_exp(output):
	output = output.replace("**", "^")
	output = output.replace("*", "×")
	output = output.replace("pi", "π")
	output = output.replace("E", "e")
	output = output.replace("I", "i")
	output = output.replace("sqrt", "√")
	output = re.sub(r"exp\((.*?)\)", r"e^\1", output)
	output = output.replace("e+", "×10^")
	return output

def solve_exp(real_exp):
	real_exp = real_exp.replace("∆", "(" + str(ans) +")")
	real_exp = real_exp.replace("×", "*")
	real_exp = real_exp.replace("÷", "/")
	real_exp = real_exp.replace("√", "sqrt")
	real_exp = real_exp.replace("^", "**")
	real_exp = real_exp.replace("π", "pi")
	real_exp = real_exp.replace("e", "E")
	return real_exp

def scr_exp(exp_input):
	exp_output = ""
	for i in exp_input:
		exp_output += i
	return exp_output
	
def bar_up():
	
	global cache_count, expression, enter_eq
	
	button_prime_number_analysis.config(state = "disable")
	
	text = out1.cget("text")
	
	if "ERROR" in text:
		return None
	
	elif "reset" in text:
		return None
	
	elif expression_cache == []:
		return None
	
	elif ("|" in expression) and (expression != ["|"]):
		return None
	
	else:
		
		try:
			if expression_cache[-1][1] == None:
				copy_expression_cache = expression_cache[0 : -1]
			else:
				copy_expression_cache = expression_cache
		except:
			pass
			
		if cache_count == 0:
				cache_count = len(copy_expression_cache)
	
		if "|" not in expression:
			if cache_count > 1:
				cache_count -= 1
				
		expression = copy_expression_cache[cache_count - 1][0]
		out1.config(text = scr_exp(expression))
		out2.config(text = f"= {copy_expression_cache[cache_count - 1][1]}")
		enter_eq = 0
		up_down_cache()

def bar_down():
	
	global cache_count, expression, enter_eq
	
	button_prime_number_analysis.config(state = "disable")
	
	text = out1.cget("text")
	
	if "ERROR" in text:
		return None
	
	elif "reset" in text:
		return None
	
	elif expression_cache == []:
		return None
	
	elif ("|" in expression) and (expression != ["|"]):
		return None
	
	elif ("|" not in expression) or (expression == ["|"]):
		try:
			if expression_cache[-1][1] == None:
				copy_expression_cache = expression_cache[0 : -1]
			else:
				copy_expression_cache = expression_cache
		except:
			pass
		if cache_count == 0:
			cache_count = len(copy_expression_cache)
		if cache_count < len(copy_expression_cache):
			cache_count += 1
		else:
			pass
			
		expression = copy_expression_cache[cache_count - 1][0]
		out1.config(text = scr_exp(expression))
		out2.config(text = f"= {copy_expression_cache[cache_count - 1][1]}")
		enter_eq = 0
		up_down_cache()
		
def bar_left():
	
	global expression, enter_eq, cache_count
	
	text = out1.cget("text")
	
	if "ERROR" in text:
		return None
	
	elif "reset" in text:
		return None
	
	elif enter_eq == 0:
		if expression == ["|"]:
			try:
				expression = expression_cache[-1][0] + ["|"]
				out1.config(text = scr_exp(expression))
				if expression_cache[-1][1] != None:
					out2.config(text = "")
				else:
					out2.config(text = "")
				return None
			except:
				pass
		else:
			if "|" in expression:
				if expression[0] == "|":
					del expression[0]
					expression += ["|"]
				else:
					k = expression.index("|")
					expression[k - 1], expression[k] = expression[k], expression[k - 1]
			else:
				expression += ["|"]
					
	else:
		if "|" not in expression:
			expression += ["|"]
			enter_eq = 0
	
	output = ""
	out2.config(text = "")
	out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")
	cache_count = 0
	up_down_cache()

def bar_right():
	
	global expression, enter_eq, cache_count
	
	text = out1.cget("text")
	
	if "ERROR" in text:
		return None
	
	elif "reset" in text:
		return None
	
	elif enter_eq == 0:
		if expression == ["|"]:
			try:
				expression = ["|"] + expression_cache[-1][0]
				out1.config(text = scr_exp(expression))
				if expression_cache[-1][1] != None:
					out2.config(text = "")
				else:
					out2.config(text = "")
				return None
			except:
				pass
		else:
			if "|" in expression:
				if expression[-1] == "|":
					del expression[-1]
					expression = ["|"] + expression
				else:
					k = expression.index("|")
					expression[k + 1], expression[k] = expression[k], expression[k + 1]
			else:
				expression = ["|"] + expression
			
	else:
		if "|" not in expression:
			expression = ["|"] + expression
			enter_eq = 0
	
	output = ""
	out2.config(text = output)
	out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")
	cache_count = 0
	up_down_cache()

def bar_add(var):
	global expression, cache_count
	try:
		k = expression.index("|")
		expression = list(expression[: k]) + [var] + list(expression[k :])
	except:
		pass
	cache_count = 0
	up_down_cache()

def bar_del():
	global expression
	if expression == ["|"]:
		pass
	else:
		if "|" in expression:
			k = expression.index("|")
			if k == 0:
				del expression[1]
			else:
				del expression[k - 1]
		else:
			pass
	out1.config(text = scr_exp(expression))
	cache_count = 0
	up_down_cache()

def add(var):
	global expression, enter_eq
	
	text = out1.cget("text")
	
	if "ERROR" in text:
		return None
	
	elif "reset" in text:
		return None
	
	elif "|" in expression:
		if enter_eq != 0:
			expression = ["|"]
			enter_eq = 0
		bar_add(var)
		out1.config(text = scr_exp(expression))
		
	else:

		expression = ["|"]
		output = ""
		out1.config(text = "|")
		out2.config(text = output)
		button_prime_number_analysis.config(state = "disable")

		if (var == "×") or (var == "÷") or (var == "+") or (var == "-") or (var == "^"):
			if enter_eq != 0:
				bar_add("∆")
		bar_add(var)
		out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")
	
	enter_eq = 0

def up_down_cache():
	
	if expression_cache == []:
		up_cache.config(fg = "black")
		down_cache.config(fg = "black") 
	
	elif len(expression_cache) == 1:
		up_cache.config(fg = "white")
		down_cache.config(fg = "black")
	
	elif len(expression_cache) > 1:
		if expression_cache[-1][1] == None:
			max = len(expression_cache) - 1
		else:
			max = len(expression_cache)
		if cache_count == 1:
			down_cache.config(fg = "white")
			up_cache.config(fg = "black")
		elif (cache_count == max) or (cache_count == 0):
			up_cache.config(fg = "white")
			down_cache.config(fg = "black")
		else:
			up_cache.config(fg = "white")
			down_cache.config(fg = "white")
	
def delete():
	global expression
	bar_del()
	out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")
	
def ac():
	global expression, enter_eq, cache_count
	
	text = out1.cget("text")
	
	if "reset" in text:
		out1.config(text = out1_cache)
		out2.config(text = out2_cache)
		PNA_button()
		
	else:
		
		expression = ["|"]
		output = ""
		out1.config(text = "|")
		out2.config(text = output)
		button_prime_number_analysis.config(state = "disable")
		enter_eq = 0
		cache_count = 0
		up_down_cache()

def on():
	
	global expression, expression_cache, cache_count, enter_eq
	
	expression = ["|"]
	expression_cache = []
	out1.config(text = "|")
	out2.config(text = "")
	cache_count = -1
	button_prime_number_analysis.config(state = "disable")
	enter_eq = 0
	up_down_cache()
	
def error_message():
	
	out1.config(text = "Math ERROR")
	out2.config(text = "Return: [OK] or [=]")
	cache_count = 0
	up_down_cache

def check_result(result):
	real, imag = result.as_real_imag()
	if limit_low <= real <= limit_high:
		if limit_low <= imag <= limit_high:
			return True
	else:
		return False

def MB10(input_result, limit_low, limit_high):
	
	result = eval(str(N(input_result)))
	
	if result == 0:
		return "0"
	
	power = 0
	sign = ""
	
	if result.imag == 0:
	
		if result < 0:
			sign = "-"
		
		if abs(result) >= limit_high:
			while result >= 10:
				result /= 10
				power += 1
			
			return f"{sign}{round(result, 9)}×10^{power}"
		
		elif abs(result) < limit_low:
			while result < 1:
				result *= 10
				power -= 1
		
			return f"{sign}{round(result, 9)}×10^{power}"
		
		else:
			return str(input_result)
	
	elif result.real == 0:
		
		result = result.imag
	
		if result < 0:
			sign = "-"
		
		if abs(result) >= limit_high:
			while result >= 10:
				result /= 10
				power += 1
			
			return f"{sign}{round(result, 9)}×10^{power}*I"
		
		elif abs(result) < limit_low:
			while result < 1:
				result *= 10
				power -= 1
		
			return f"{sign}{round(result, 9)}×10^{power}*I"
		
		else:
			return f"str(input_result)*I"
	
	else:
		
		result_real = result.real
		result_imag = result.imag
		power_real = 0
		power_imag = 0
		output_result = ""
		
		if result_real < 0:
			sign = "-"
		
		if abs(result_real) >= limit_high:
			while result_real >= 10:
				result_real /= 10
				power_real += 1
			
			output_result = f"{sign}{round(result_real, 9)}×10^{power_real}"
		
		elif abs(result_real) < limit_low:
			while result_real < 1:
				result_real *= 10
				power_real -= 1
		
			output_result = f"{sign}{round(result_real, 9)}×10^{power_real}"
		
		else:
			output_result = str(result_real)
		
		if result_imag < 0:
			sign = "-"
		
		else:
			sign = "+"
		
		if abs(result_imag) >= limit_high:
			while result_imag >= 10:
				result_imag /= 10
				power_imag += 1
			
			output_result += f"{sign}{round(result_imag, 9)}×10^{power_imag}*I"
		
		elif abs(result_imag) < limit_low:
			while result_imag < 1:
				result_imag *= 10
				power_imag -= 1
		
			output_result += f"{sign}{round(result_imag, 9)}×10^{power_imag}*I"
		
		else:
			output_result += f"{result_imag}*I"
		
		return output

def GCD(a, b):
	if a % 1 != 0:
		return 0/0
	if b % 1 != 0:
		return 0/0
	while b != 0:
		a, b = b, a % b
	return a

def LCM(a, b):
	if a % 1 != 0:
		return 0/0
	if b % 1 != 0:
		return 0/0
	return (a * b) / GCD(a, b)

def frac(n):
	return factorial(n)

def PNA_button():
	output = out2.cget("text")
	if (output == "") or ("ERROR" in out1.cget("text")) or ("reset" in out1.cget("text")):
		button_prime_number_analysis.config(state = "disable")
	else:
		output = output.replace("=", "")
		output = output.replace(" ", "")
		output = solve_exp(output)
		result = N(output)
		if result.is_complex == False:
			button_prime_number_analysis.config(state = "disable")
		elif result % 1 != 0:
			button_prime_number_analysis.config(state = "disable")
		elif result <= 1:
			button_prime_number_analysis.config(state = "disable")
		else:
			button_prime_number_analysis.config(state = "normal")

def PNA():
	output = out2["text"]

	for i in output:
		if i in power_number:
			return None
	output = output.replace("=", "")
	output = output.replace(" ", "")
	output = solve_exp(output)
	output = N(output)
	output = int(output)
	output= factorint(output)
	output= str(output)
	output= output.replace(" ", "")
	output= output.replace("{", "")
	output= output.replace("}", "")
	output= output.split(",")
	text = []
	for i in output:
		i = i.split(":")
		n = ""
		if i[1] != "1":
			for j in i[1]:
				j = str(j)
				k = number.index(j)
				n += power_number[k]
			text.append(str(i[0]) + n)
		else:
			text.append(str(i[0]))
	output = text
	output= " × ".join(output)
	out2.config(text = "= " + output)
			

def sin(a):
	global mode
	if mode == "r":
		return m.sin(a)
	if mode == "d":
		return m.sin(m.radians(a))
		
def cos(a):
	global mode
	if mode == "r":
		return m.cos(a)
	if mode == "d":
		return m.cos(m.radians(a))
		
def tan(a):
	global mode
	if mode == "r":
		return m.tan(a)
	if mode == "d":
		return m.tan(m.radians(a))
		
def asin(a):
	global mode
	if mode == "r":
		return m.asin(a)
	if mode == "d":
		return m.degrees(m.asin(a))
		
def acos(a):
	global mode
	if mode == "r":
		return m.acos(a)
	if mode == "d":
		return m.degrees(m.acos(a))
		
def atan(a):
	global mode
	if mode == "r":
		return m.atan(a)
	if mode == "d":
		return m.degrees(m.atan(a))
		
def mode_degree(degree):
	global mode
	if degree == "d":
		button_d_mode.config(state = "disabled")
		button_r_mode.config(state = "normal")
		mode = "d"
	if degree == "r":
		button_r_mode.config(state = "disabled")
		button_d_mode.config(state = "normal")
		mode = "r"
	
def on_imag_num():
	global imag
	button_ON_imagnum_mode.config(state = "disabled")
	button_OFF_imagnum_mode.config(state = "normal")
	imag = "ON"
	
def off_imag_num():
	global imag
	button_OFF_imagnum_mode.config(state = "disabled")
	button_ON_imagnum_mode.config(state = "normal")
	imag = "OFF"

def on_deci_num():
	global deci
	button_ON_decimal_mode.config(state = "disabled")
	button_OFF_decimal_mode.config(state = "normal")
	deci = "ON"
	
def off_deci_num():
	global deci
	button_OFF_decimal_mode.config(state = "disabled")
	button_ON_decimal_mode.config(state = "normal")
	deci = "OFF"

def end_left():
	global expression
	
	text = out1.cget("text")
	
	if "ERROR" in text:
		return None
	
	elif "reset" in text:
		return None
	
	try:
		k = expression.index("|")
		del expression[k]
		expression = ["|"] + expression
	except:
		pass
	out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")

def end_right():
	global expression
	
	text = out1.cget("text")
	
	if "ERROR" in text:
		return None
	
	elif "reset" in text:
		return None
	
	try:
		k = expression.index("|")
		del expression[k]
		expression += ["|"]
	except:
		pass
	out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")
	
def reset_message():
	global out1_cache, out2_cache
	
	if "reset" not in out1.cget("text"):
		out1_cache = out1.cget("text")
		out2_cache = out2.cget("text")

	button_prime_number_analysis.config(state = "disable")

	out1.config(text = "Are you sure you want to reset?")
	out2.config(text = "Yes: [OK] or [=]\nNo: [AC]")

def reset():
	global expression, output, ans, enter_eq, mode, imag, deci, out1_cache, out2_cache, expression_cache, cache_count
	
	expression = ["|"]
	output = ""
	ans = 0
	enter_eq = 0
	mode = "d"
	imag = "OFF"
	deci = "OFF"
	out1.config(text = scr_exp(expression))
	out2.config(text = "")
	button_Ans.config(text = "∆ = 0")
	mode_degree("d")
	off_imag_num()
	off_deci_num()
	button_prime_number_analysis.config(state = "disable")
	out1_cache = ""
	out2_cache = ""
	expression_cache = []
	cache_count = -1
	up_down_cache()
	
def solve():
	global expression, output, ans, enter_eq, list_cal, expression_cache, cache_count
	
	text = out1.cget("text")
	
	if "ERROR" in text:
		expression += "|"
		out1.config(text = scr_exp(expression))
		out2.config(text = "")
	
	elif "reset" in text:
		reset()
	
	elif expression == ["|"]:
		pass
	
	else:
		
		try:
			k = expression.index("|")
			del expression[k]
		except:
			pass
		
		previous_character = None
		real_exp = ""
		error = 0
		
		for i in range(len(expression)):
			if (previous_character in list_num) and (expression[i] in list_cal):
				real_exp += "*" + expression[i]
		
			elif (previous_character not in list_num) and (expression[i] == "."):
				real_exp += "0."
		
			else:
				real_exp += expression[i]
			
			previous_character = expression[i]
		
		real_exp = solve_exp(real_exp)
		
		if imag == "OFF":
			try:
				if deci == "OFF":
					output = eval(real_exp)
				else:
					output = N(eval(real_exp))
				if "I" in str(output):
					error += 1
			except :
				error_message()
		else:
			try:
				if deci == "OFF":
					output = eval(real_exp)
				else:
					output = N(eval(real_exp))
			except:
				error_message()
		
		try:
			check = check_result(N(eval(real_exp)))
			if check == False:
				error += 1
		except:
			error += 1
	
		if error == 0:
			output = MB10(output, limit_low_result, limit_high_result)
			ans_real = output
			output = output_exp(output)
			out2.config(text = "= " + str(output))
			ans = ans_real
			out1.config(text = scr_exp(expression))
			button_Ans.config(text = "∆ = " + output_exp(output))
			enter_eq += 1
			try:
				if expression_cache[-1][1] != None:
					pass
				else:
					del expression_cache[-1]
			except:
				pass
			expression_cache.append([expression, output])
			if len(expression_cache) > 30:
				del expression_cache[0]

		else:
			try:
				if expression_cache[-1][1] != None:
					pass
				else:
					del expression_cache[-1]
			except:
				pass
			expression_cache.append([expression, None])
			error_message()
		
		PNA_button()
	cache_count = 0
	up_down_cache()

app = tk.Tk()
app.geometry("720x1650")

up_cache = tk.Label(app, text = "↑", bg = "black", fg = "black")
up_cache.place(x = 685, y = 250, height = 35, width = 35)

down_cache = tk.Label(app, text = "↓", bg = "black", fg = "black")
down_cache.place(x = 650, y = 250, height = 35, width = 35)

out1 = tk.Label(app, text = expression, bg = "black", fg = "white", justify = "left", anchor = "nw", wraplength = 720)
out1.place(x = 0, y = 0, height = 150, width = 720)

#----------expression input screen----------

out2 = tk.Label(app, text = output, bg = "black", fg = "white", anchor = "e")
out2.place(x = 0, y = 150, height = 90, width = 720)

#-----------output screen----------

button_Ans = tk.Button(app, text = "∆ = 0", bg = "black", fg = "white", anchor = "w", wraplength = 330, font = ("Arial", 5), command = lambda: add("∆"))
button_Ans.place(x= 455, y = 400, height = 60, width = 275)

button_ON = tk.Button(app, text = "ON", bg = "white", command = lambda: on())
button_ON.place(x = 5, y = 245, height = 70, width = 70)

button_left = tk.Button(app, text = "<", bg = "white", command = lambda: bar_left())
button_left.place(x = 215, y = 320, height = 65, width = 65)

button_right = tk.Button(app, text = ">", bg = "white", command = lambda: bar_right())
button_right.place(x = 365, y = 320, height = 65, width = 65)

button_OK = tk.Button(app, text = "OK", bg = "white", command = lambda: solve())
button_OK.place(x = 290, y = 320, height = 65, width = 65)

button_up = tk.Button(app, text = "˄", bg = "white", command = lambda: bar_up())
button_up.place(x = 290, y = 245, height = 65, width = 65)

button_down = tk.Button(app, text = "˅", bg = "white", command = lambda: bar_down())
button_down.place(x = 290, y = 395, height = 65, width = 65)

button_end_left = tk.Button(app, text = "←", fg = "blue", command = lambda: end_left())
button_end_left.place(x = 440, y = 320, height = 65, width = 65)

button_end_right = tk.Button(app, text = "→", fg = "blue", command = lambda: end_right())
button_end_right.place(x = 515, y = 320, height = 65, width = 65)

#----------navigation bar button---------

button_1 = tk.Button(app, text = "1", bg = "white", command = lambda: add("1"))
button_1.place(x = 15, y = 465, height = 100, width = 100)

button_2 = tk.Button(app, text = "2", bg = "white", command = lambda: add("2"))
button_2.place(x = 125, y = 465, height = 100, width = 100)

button_3 = tk.Button(app, text = "3", bg = "white", command = lambda: add("3"))
button_3.place(x = 235, y = 465, height = 100, width = 100)

button_del = tk.Button(app, text = "Del", bg = "white", command = lambda: delete())
button_del.place(x = 345, y = 465, height = 100, width = 100)

button_ac = tk.Button(app, text = "AC", bg = "white", command = lambda: ac())
button_ac.place(x = 455, y = 465, height = 100, width = 100)

#---------------line 1---------------

button_4 = tk.Button(app, text = "4", bg = "white", command = lambda: add("4"))
button_4.place(x = 15, y = 575, height = 100, width = 100)

button_5 = tk.Button(app, text = "5", bg = "white", command = lambda: add("5"))
button_5.place(x = 125, y = 575, height = 100, width = 100)

button_6 = tk.Button(app, text = "6", bg = "white", command = lambda: add("6"))
button_6.place(x = 235, y = 575, height = 100, width = 100)

button_time = tk.Button(app, text = "×", bg = "white", command = lambda: add("×"))
button_time.place(x = 345, y = 575, height = 100, width = 100)

button_div = tk.Button(app, text = "÷", bg = "white", command = lambda: add("÷"))
button_div.place(x = 455, y = 575, height = 100, width = 100)

#---------------line 2---------------

button_7 = tk.Button(app, text = "7", bg = "white", command = lambda: add("7"))
button_7.place(x = 15, y = 685, height = 100, width = 100)

button_8 = tk.Button(app, text = "8", bg = "white", command = lambda: add("8"))
button_8.place(x = 125, y = 685, height = 100, width = 100)

button_9 = tk.Button(app, text = "9", bg = "white", command = lambda: add("9"))
button_9.place(x = 235, y = 685, height = 100, width = 100)

button_plus = tk.Button(app, text = "+", bg = "white", command = lambda: add("+"))
button_plus.place(x = 345, y = 685, height = 100, width = 100)

button_minus = tk.Button(app, text = "-", bg = "white", command = lambda: add("-"))
button_minus.place(x = 455, y = 685, height = 100, width = 100)

#---------------line 3---------------

button_0 = tk.Button(app, text = "0", bg = "white", command = lambda: add("0"))
button_0.place(x = 15, y = 795, height = 100, width = 100)

button_dot = tk.Button(app, text = ".", bg = "white", command = lambda: add("."))
button_dot.place(x = 125, y = 795, height = 100, width = 100)

button_pi = tk.Button(app, text = "π", bg = "white", command = lambda: add("π"))
button_pi.place(x = 235, y = 795, height = 100, width = 100)

button_euler = tk.Button(app, text = "e", bg = "white", command = lambda: add("e"))
button_euler.place(x = 345, y = 795, height = 100, width = 100)

button_exe = tk.Button(app, text = "=", bg = "white", command = lambda: solve())
button_exe.place(x = 455, y = 795, height = 100, width = 100)

#---------------line 4---------------

#___________basic math operations__________



button_sin = tk.Button(app, text = "sin(", bg = "white", command = lambda: add("sin("))
button_sin.place(x = 15, y = 905, height = 100, width = 100)

button_cos = tk.Button(app, text = "cos(", bg = "white", command = lambda: add("cos("))
button_cos.place(x =125, y = 905, height = 100, width = 100)

button_tan = tk.Button(app, text = "tan(", bg = "white", command = lambda: add("tan("))
button_tan.place(x = 235, y = 905, height = 100, width = 100)

button_open_parenthesis = tk.Button(app, text = "(", bg = "white", command = lambda: add("("))
button_open_parenthesis.place(x = 345, y = 905, height = 100, width = 100)

button_sqrt = tk.Button(app, text = "√", bg = "white", command = lambda: add("√("))
button_sqrt.place(x = 455, y = 905, height = 100, width = 100)

button_asin = tk.Button(app, text = "asin(", bg = "white", command = lambda: add("asin("))
button_asin.place(x = 15, y = 1015, height = 100, width = 100)

button_acos = tk.Button(app, text = "acos(", bg = "white", command = lambda: add("acos("))
button_acos.place(x =125, y = 1015, height = 100, width = 100)

button_atan = tk.Button(app, text = "atan(", bg = "white", command = lambda: add("atan("))
button_atan.place(x = 235, y = 1015, height = 100, width = 100)

button_close_parenthesis = tk.Button(app, text = ")", bg = "white", command = lambda: add(")"))
button_close_parenthesis.place(x = 345, y = 1015, height = 100, width = 100)

button_sqrt = tk.Button(app, text = "^", bg = "white", command = lambda: add("^"))
button_sqrt.place(x = 455, y = 1015, height = 100, width = 100)



button_log = tk.Button(app, text = "log(", bg = "white", command = lambda: add("log("))
button_log.place(x = 15, y = 1125, height = 100, width = 100)

button_GCD = tk.Button(app, text = "GCD(", bg = "white", command = lambda: add("GCD("))
button_GCD.place(x = 125, y = 1125, height = 100, width = 100)

button_LCM = tk.Button(app, text = "LCM(", bg = "white", command = lambda: add("LCM("))
button_LCM.place(x = 235, y = 1125, height = 100, width = 100)

button_comma = tk.Button(app, text = ",", bg = "white", command = lambda: add(","))
button_comma.place(x = 345, y = 1125, height = 100, width = 100)

button_frac = tk.Button(app, text = "frac(", bg = "white", command = lambda: add("frac("))
button_frac.place(x = 455, y = 1125, height = 100, width = 100)


degree_mode_txt = tk.Label(app, text = "Degree mode", fg = "blue", font = ("Arial", 5))
degree_mode_txt.place(x = 575, y = 460)

button_d_mode = tk.Button(app, text = "d", fg = "blue", command = lambda: mode_degree("d"), state = "disabled")
button_d_mode.place(x = 575, y = 490, height = 50, width = 50)

button_r_mode = tk.Button(app, text = "r", fg = "blue", command = lambda: mode_degree("r"), state = "normal")
button_r_mode.place(x = 635, y = 490, height = 50, width = 50)

text_imagnum_mode = tk.Label(app, text = "Imaginary number mode", fg = "blue", font = ("Arial", 4))
text_imagnum_mode.place(x = 555, y = 550)

button_ON_imagnum_mode = tk.Button(app, text = "ON", fg = "blue", command = lambda: on_imag_num(), state = "normal")
button_ON_imagnum_mode.place(x = 575, y = 590, height = 50, width = 50)

button_OFF_imagnum_mode = tk.Button(app, text = "OFF", fg = "blue", command = lambda: off_imag_num(), state = "disabled")
button_OFF_imagnum_mode.place(x = 635, y = 590, height = 50, width = 50)

text_decimal_mode = tk.Label(app, text = "Decimal number mode", fg = "blue", font = ("Arial", 4))
text_decimal_mode.place(x = 555, y = 645)

button_ON_decimal_mode = tk.Button(app, text = "ON", fg = "blue", command = lambda: on_deci_num(), state = "normal")
button_ON_decimal_mode.place(x = 575, y = 675, height = 50, width = 50)

button_OFF_decimal_mode = tk.Button(app, text = "OFF", fg = "blue", command = lambda: off_deci_num(), state = "disable")
button_OFF_decimal_mode.place(x = 635, y = 675, height = 50, width = 50)

button_reset_mode = tk.Button(app, text = "Reset", fg = "blue", command = lambda: reset_message())
button_reset_mode.place(x = 575, y = 735, height = 50, width = 110)

button_prime_number_analysis = tk.Button(app, text = "PNA", fg = "blue", command = lambda: PNA(), state = "disable")
button_prime_number_analysis.place(x = 575, y = 795, height = 50, width = 110)

app.mainloop()