#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter as tk
from tkinter import * 
from tkinter.ttk import Progressbar



class Interface:
	def __init__(self,list_items,pourcentage,details):
		window = tk.Tk()
		window.title('MR ROBOT')
		 
		window.geometry('650x300')
		
		e=sorted(pourcentage)
		row=1		
		p_row=1
		title=tk.Label(window,text="TOP 10 CV")
		title.grid(column=2,row=0)
		
		for j in e:
			index = pourcentage.index(j)
			names = tk.Label(window,text=list_items[index])
			names.grid(column=1,row=row)
			bar = Progressbar(window, length=220, style='black.Horizontal.TProgressbar')
			bar['value'] = j
			bar.grid(column=2, row=p_row)
			lb = tk.Label(window,text=str(j)+"%")
			lb.grid(column=3,row=p_row)

			row+=1
			p_row+=1
		
		row=1
		col=3
		"""
		for i in details:
			filename = tk.Label(window,text=str(i['filename'])+'\n'+str(i['name'])+'\n'+str(i['email'])+'\n'+str(i['mobile_number'])+'\n'+str(i['degree'])+'\n'+str(i['experience'])+'\n'+str(i['skills'])+'\n'+str(i['languages']))
			filename.grid(column=col,row=row)
			col+=1
		"""


		window.mainloop()


