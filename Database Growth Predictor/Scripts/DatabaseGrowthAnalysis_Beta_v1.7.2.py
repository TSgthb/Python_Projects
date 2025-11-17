###################################################################################################################
#                                               !!! Important !!!                                                 #
#                This is application is stil in development phase. Use it at your own discretion.                 #
###################################################################################################################
# Notes:                                                                                                          #
# 1. This program analyzes and forecasts the growth of a database by means of statistical data modelling process, #
#    linear regression. Historical data is provided in terms of date and backup size based upon which the growth  #
#    is forecasted.                                                                                               #
# 2. This works on the assumption that there is no abrupt data growth and the database backup size over different #
#    months, grows linearly.                                                                                      #
# 3. The file to be provided must be an Excel file with a single sheet. It should contain 3 columns, specifically #
#    named as 'Database', 'Size' and 'Date'. The 'Date' column should contain 'datetime' type object and should   #
#    be sorted in latest to oldest order per database.                                                            #
###################################################################################################################
# Changelog:                                                                                                      #
# 1. Beta_v1.1: Introduced a loop to iterate, analyze and forecast multiple databases.                            #
# 2. Beta_v1.2: Added summarization of growth per month by means of graph and groupby().                          #
# 3. Beta_v1.3: Added GUI for accessibility.                                                                      #
# 4. Beta_v1.4: Added a null value validator in the file path field and an exit button.                           #
# 5. Beta_v1.5: UI streamlining.                                                                                  #
# 6. Beta_v1.6: Added a new window for printing analysis information.                                             #
# 7. Beta_v1.7: UI streamlining.                                                                                  #  
# 8. Beta_v1.7.2: Modified code for optimized processing and closure of windows                                   #
###################################################################################################################

# Importing required libraries.
# import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from sklearn.linear_model import LinearRegression
from datetime import timedelta
#from tkinter import *
from customtkinter import *
from PIL import Image

# Declaring variables for printing text on the welcome screen
acknow='Welcome! This application is still under development phase. Help make it better with valuable suggestions.'
line1='The program uses linear regression to analyze and forecast the growth of a database. Historical data, which is provided in terms of date and backup size, is used to predict future growth trends.'
line2="The statement implies that a certain process or method is being used assuming that there won't be any sudden or unexpected increase in the data and that the size of the backup of the database will increase steadily over different months in a linear fashion."
line3="Before proceeding ahead, make sure below prerequisites are fulfilled to avoid any errors:"
line3_1='1. The file must be an Excel file with a single sheet. The same can be provided via file path or selected using the browse button.'
line3_2="2. The file provided must contain 3 columns, specifically, 'Database', 'Size' and 'Date'."
line3_3="3. The 'Date' column should be a 'datetime' type object and sorted in the latest to oldest order per database."

# Creating GUI.
# Root window title and dimension.
root = CTk()
set_appearance_mode("dark")
set_default_color_theme("green")    
root.title("Database Growth Predictor")
# Set geometry (widthxheight)
root.geometry('1000x600')
img = Image.open(r"C:\\Users\\tejvesin\\OneDrive - Capgemini\\Desktop\\Personal\\Python\\Browse.png")

def browse_file():
   filepath = filedialog.askopenfilename()
   txt.insert(END,filepath)

# Defining close operation.
def Close():
    # Close all Matplotlib figures
    plt.close('all')
    # Destroy all windows
    for window in root.winfo_children():
        try:
            window.destroy()
        except:
            pass
    root.quit()      # Stop mainloop
    root.destroy()   # Destroy root window
    sys.exit()       # Terminate Python process

# Defining the click operation.
def clicked():
    global file_path
    file_path = txt.get()
    if file_path:
        lbl.configure(text = 'File parsed successfully.')
        print(f'File path: {file_path}')        
    
        # Defining new window properties.
        new = CTkToplevel(root)
        new.geometry("800x640")
        new.title("Analysis Output")
        new.wm_attributes('-topmost',True)

        # Defining graph window properties.
        gnew = CTkToplevel(root)
        gnew.geometry("800x640")
        gnew.title("Graph Output")
        gnew.wm_attributes('-topmost',True)

        # Initializing a new text widget in the new window.
        res = CTkTextbox(master=new, font=('Calibri',12))
        res.place(relx=0.5, rely=0.5, anchor='center')

        # Printing output to the new window.
        res.insert(END,'Database Growth Analysis'+'\n')
        res.insert(END,f'File path: {file_path}'+'\n')
        
        # Reading the Excel file from the path.
        #file_path = input('Provide path to the Excel: ')
        read_data = pd.read_excel(file_path)

        # Coverting the read file into a dataframe
        table_df = pd.DataFrame(read_data)
        #print(table_df)

        # Initializing a counter for determining forcasted total size.
        Backups_sizes = 0
        old_backup_size = 0

        # Initializing an empty list to store known and predicted data for all databases.
        collection = []

        # Grouping and creating dataframes by database names.
        grouped_df_2 = table_df.groupby('Database')

        # Making the ouput a little neat.
        print('------------------------------------------------------------------------')
        res.insert(END,'------------------------------------------------------------------------'+'\n')

        # Iterating over each grouped dataframe. Each dataframe contains data exclusive to a particular database.
        for db, grouped_df in grouped_df_2:
            
            # Coverting date column to date type format.
            grouped_df['Date'] = pd.to_datetime(grouped_df['Date'])

            # Storing and printing the latest known size of the database.           
            old_size = grouped_df.iat[0,1] # Storing the latest known size of the database.
            print(f"Current {db} size is {old_size:.2f} GB")
            res.insert(END,f"Current {db} size is {old_size:.2f} GB"+"\n")

            # Initializing a regression model.
            regression_model = LinearRegression() 
            grouped_df['DaysSinceStart'] = (grouped_df['Date'] - grouped_df['Date'].min()).dt.days # Appending a column 'DaysSinceStart' to the 'grouped_df' dataframe denoting number of days that have passed since the first date in the dataframe.
            regression_model.fit(grouped_df[['DaysSinceStart']], grouped_df['Size']) # Calculating the coefficients of the regression_model.

            # Predicting the future backup sizes.
            future_dates = [grouped_df['Date'].max() + timedelta(days=i) for i in range(1, 181)] # Storing the future dates.
            future_days_since_start = [(date - grouped_df['Date'].min()).days for date in future_dates] # Storing the number of days in future from last known date, as a list.
            future_predictions = regression_model.predict(pd.DataFrame({'DaysSinceStart': future_days_since_start})) # Predicting the future backup values based on the model defined above using above list of days in future from last known date.

            # Printing predicted size for each database.
            print(f'Estimated data growth of {db} by {future_dates[-1].date()} is {future_predictions[-1]:.2f} GB'+'\n\n')
            res.insert(END,f'Estimated data growth of {db} by {future_dates[-1].date()} is {future_predictions[-1]:.2f} GB'+'\n\n')
            
            # Adding the forcasted backup sizes for all databases.
            Backups_sizes = Backups_sizes + future_predictions[-1]

            # Adding the old backup sizes for all databases.
            old_backup_size = old_backup_size + old_size

            # Initializing new dataframe to store predicted values for the current database in the iteration.
            new_df = pd.DataFrame({'Database':db,'Date':future_dates,'Size':future_predictions,'DaysSinceStart':future_days_since_start})

            # Joining the old and predicted values dataframes together.
            new_concat_df = pd.concat([grouped_df,new_df],ignore_index=True)

            # Appending the newly formed dataframe to the list initalized above.
            collection.append(new_concat_df)

        # Joining all the dataframes in the list to get a master dataframe containg old and predicted values for all the databases.
        original_df = pd.DataFrame()
        for dtframe in collection:        
                original_df = pd.concat([original_df,dtframe])
        

        # Printing predicted size information for all databases.
        print('------------------------------------------------------------------------')
        res.insert(END,'------------------------------------------------------------------------'+'\n')
        print(f'Total databases: {len(collection)}')
        res.insert(END,f'Total databases: {len(collection)}'+'\n')
        print(f'Total current size: {old_backup_size:.2f} GB')
        res.insert(END,f'Total current size: {old_backup_size:.2f} GB'+'\n')
        print(f'Total predicted growth by {future_dates[-1].date()}: {Backups_sizes:.2f} GB')
        res.insert(END,f'Total predicted size by {future_dates[-1].date()}: {Backups_sizes:.2f} GB'+'\n')
        print(f'Total growth: {Backups_sizes - old_backup_size:.2f} GB')
        res.insert(END,f'Total growth: {Backups_sizes - old_backup_size:.2f} GB'+'\n')
        
        # Initalizing a new dataframe to summarize the average growth for all databases altogether each month.
        months_df = original_df

        # Changing the data format to 'month_name year'.
        months_df['Date'] = months_df['Date'].dt.strftime('%b %Y')
        months_df['Date'] = pd.to_datetime(months_df['Date'],format='%b %Y')

        # Summarizing data by 'month_name year' for all databases. 
        grouped_df_month = pd.DataFrame(months_df.groupby('Date')['Size'].mean())
        grouped_df_month.reset_index(level=0, inplace=True)
        grouped_df_month['Date'] = grouped_df_month['Date'].dt.strftime('%b %Y')
        print('------------------------------------------------------------------------')
        res.insert(END,f'------------------------------------------------------------------------'+'\n')
        print('Forecasted average backup size per month')
        print(grouped_df_month)
        res.insert(END,'Forecasted average backup size per month'+'\n')
        res.insert(END,grouped_df_month)
        
        # Activating scrollbar and making textbox un-editable.
        res.configure(state='disabled')
        res.pack(expand=True,fill='both')

        # Ploting the predictions.
        plt.figure(figsize=(15, 10))
        plt.plot(grouped_df_month['Date'], grouped_df_month['Size'], marker='', linestyle='-')
        plt.title('Average Backup Size Forecasted Growth')
        plt.xlabel('Date')
        plt.ylabel('Backup Size (GB)')
        plt.grid(True)
        ##plt.show()
        graphcanvas = FigureCanvasTkAgg(plt.gcf(), master=gnew)     # A tk.DrawingArea.
        graphcanvas.draw()
        graphcanvas.get_tk_widget().pack()

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(graphcanvas, gnew)
        toolbar.update()    
        graphcanvas.get_tk_widget().pack()

    else:
        lbl.configure(text='No input provided.')
        
# Adding a label to the root window.
lbl_1 = CTkLabel(master=root, text='Database Growth Predictor', font=('Calibri',29,'bold'))
lbl_1.place(relx=0.25, rely=0.1, anchor='center')

# Defining version label.
lbl_version = CTkLabel(master=root, text='Version: Beta_v1.7', font=('Calibri',14,'italic'), text_color='#737373')
lbl_version.place(relx=0.25, rely=0.15, anchor='center')

# Adding instructions to the root window.
# Paragraph 1
lbl_para1 = CTkLabel(master=root, text=line1, font=('Calibri',12,),wraplength=400,justify=LEFT)
lbl_para1.place(relx=0.25, rely=0.3, anchor='center')

# Paragraph 2
lbl_para2 = CTkLabel(master=root, text=line2, font=('Calibri',12,),wraplength=401,justify=LEFT)
lbl_para2.place(relx=0.25, rely=0.42, anchor='center')

# Paragraph 3
lbl_para3 = CTkLabel(master=root, text=line3, font=('Calibri',12,),wraplength=400,justify=LEFT)
lbl_para3.place(relx=0.245, rely=0.55, anchor='center')

# Sub-points of paragraph 3
lbl_para3_1 = CTkLabel(master=root, text=line3_1, font=('Calibri',12,),wraplength=400,justify=LEFT)
lbl_para3_1.place(relx=0.242, rely=0.65, anchor='center')

lbl_para3_2 = CTkLabel(master=root, text=line3_2, font=('Calibri',12,),wraplength=400,justify=LEFT)
lbl_para3_2.place(relx=0.243, rely=0.72, anchor='center')

lbl_para3_3 = CTkLabel(master=root, text=line3_3, font=('Calibri',12,),wraplength=400,justify=LEFT)
lbl_para3_3.place(relx=0.244, rely=0.79, anchor='center')

# Adding an entry Field to recieve input.
txt = CTkEntry(master=root, placeholder_text='Enter a valid path', width=300, font=('Calibri',12), corner_radius=32,border_color='#3b3b3b',fg_color='#3b3b3b')
txt.place(relx=0.74, rely=0.4, anchor='center')

# Adding another label.
lbl = CTkLabel(master=root, text = 'No path provided.', font=('Calibri',12,'italic'),text_color='#4F4E4E')
lbl.place(relx=0.77, rely=0.45, anchor='center')

# Adding a analyze button.
btn = CTkButton(master=root, text = 'Analyze', command=clicked, corner_radius=32, font=('Calibri',12))
btn.place(relx=0.77, rely=0.53, anchor='center')

# Adding a exit button.
exit_button = CTkButton(master=root, text="Exit", command=Close, corner_radius=32, font=('Calibri',12),fg_color='#8B0000',hover_color='#630000') 
exit_button.place(relx=0.77, rely=0.59, anchor='center')

# Adding a browse button.
bt_browse = CTkButton(master=root,text="", corner_radius=32, command=browse_file, image=CTkImage(dark_image=img,light_image=img),width=10,fg_color='#3b3b3b',hover_color='#343434')
bt_browse.place_configure(relx=0.92, rely=0.4, anchor='center')

# Execute CustomTkinter
root.mainloop()