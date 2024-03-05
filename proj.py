from tkinter import *
import psycopg2

conn = psycopg2.connect(
   database="your db name", user='your username', password='your password', host='your host name', port= 'your port'
)
cursor = conn.cursor()

root=Tk()
root.title("Event database")
lbl=Label(root, text="Hi")
lbl.grid()
root.geometry("1500x1500")
def clicked1():
    cursor.execute('''SELECT * FROM events WHERE "start date" > '2024-06-20' ORDER BY "start date"''')
    data= cursor.fetchall()
    lbl.configure(text=data)
def clicked2():
    cursor.execute('''SELECT attendees."EventID", COUNT(*) AS NumberOfAttendees FROM attendees GROUP BY attendees."EventID"''')
    data= cursor.fetchall()
    lbl.configure(text=data)
def clicked3():
    cursor.execute('''SELECT sessions.Name, speakers.Name AS SpeakerName, sessions."start date"
   FROM sessions
   JOIN speakers ON sessions."SpeakerID" = speakers."SpeakerID"
   ORDER BY sessions."start date"''')
    data= cursor.fetchall()
    lbl.configure(text=data)
def clicked4():
    cursor.execute('''SELECT e."EventID", e.name AS event_name, v.name AS venue_name
FROM events e
JOIN venues v ON e."VenueID" = v."VenueID" ''')
    data= cursor.fetchall()
    lbl.configure(text=data)
def clicked5():
    cursor.execute('''SELECT * FROM venues LEFT JOIN events ON venues."VenueID" = events."VenueID"
   WHERE events."EventID" IS NULL''')
    data= cursor.fetchall()
    lbl.configure(text=data)
def clicked6():
    cursor.execute('''SELECT sessions."EventID", AVG("end date" - "start date") AS AverageDuration
   FROM sessions
   WHERE sessions."EventID" = '1005'
   GROUP BY sessions."EventID"''')
    data= cursor.fetchall()
    lbl.configure(text=data)
def clicked7():
    cursor.execute('''SELECT * FROM events WHERE Name LIKE '%Birth%' ''')
    data= cursor.fetchall()
    lbl.configure(text=data)
def clicked8():
    cursor.execute('''SELECT * FROM attendees WHERE "EventID" IN ('1001', '1003', '1005') ''')
    data= cursor.fetchall()
    lbl.configure(text=data)
def clicked9():
    cursor.execute('''SELECT * FROM sessions WHERE "start date" BETWEEN '2022-01-01 09:00:00' AND '2022-01-01 18:00:00' ''')
    data= cursor.fetchall()
    lbl.configure(text=data)
def clicked10():
    cursor.execute('''INSERT INTO venues ("VenueID", name, address, capacity)
   VALUES (5007, 'New Venue', 'Street New number 7', 200)''')
    conn.commit()
    lbl.configure(text="New venue entered.")
def clicked11():
    cursor.execute('''UPDATE venues
   SET address = 'Updated Street number 8'
   WHERE "VenueID" = 5003 ''')
    conn.commit()
    lbl.configure(text="Venue updated.")
def clicked12():
    cursor.execute('''DELETE FROM venues
   WHERE "VenueID" = 5007''')
    conn.commit()
    lbl.configure(text="Venue deleted.")
b1=Button(root, text="First query", command=clicked1)
b1.grid()
b2=Button(root,text="Second query", command=clicked2)
b2.grid()
b3=Button(root,text="Third query", command=clicked3)
b3.grid()
b4=Button(root,text="Forth query", command=clicked4)
b4.grid()
b5=Button(root,text="Fifth query", command=clicked5)
b5.grid()
b6=Button(root,text="Sixth query", command=clicked6)
b6.grid()
b7=Button(root,text="Seventh query", command=clicked7)
b7.grid()
b8=Button(root,text="Eight query", command=clicked8)
b8.grid()
b9=Button(root,text="Nineth query", command=clicked9)
b9.grid()
b10=Button(root,text="Insert query", command=clicked10)
b10.grid()
b11=Button(root,text="Update query", command=clicked11)
b11.grid()
b12=Button(root,text="Delete query", command=clicked12)
b12.grid()
root.mainloop()