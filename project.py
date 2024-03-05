import psycopg2
from tkinter import *

conn = psycopg2.connect(
   database="your db name", user='your username', password='your password', host='your host name', port= 'your port'
)
cursor = conn.cursor()

def menu():
   while True:
      answer=input("What would you like to do? \n 1. Select all the events that start after 1st of January 2023 \n 2. Count all number of attendees based on events \n 3. Select speakers based on session \n 4. Retrieves all events with their corresponding venue names (using Join) \n 5. Find venues that have not hosted any events \n 6. Find venues that have not hosted any events \n 7. Using special operators (LIKE Operator): Used for pattern matching \n 8. IN Operator: Selects data within a set of given values \n 9. BETWEEN Operator: Retrieves data within a specific range \n 10. Inserts a new venue into the venues table \n 11. Updates the address of a venue \n 12. Deletes a venue from the venues table \n 13. Exit \n")
      if int(answer)==1:
         cursor.execute('''SELECT * FROM events WHERE "start date" > '2023-01-01' ORDER BY "start date"''')
         data= cursor.fetchall()
         print(data)
      elif int(answer)==2:
         cursor.execute('''SELECT attendees."EventID", COUNT(*) AS NumberOfAttendees FROM attendees GROUP BY attendees."EventID"''')
         data= cursor.fetchall()
         print(data)
      elif int(answer)==3:
         cursor.execute('''SELECT sessions.Name, speakers.Name AS SpeakerName, sessions."start date"
   FROM sessions
   JOIN speakers ON sessions."SpeakerID" = speakers."SpeakerID"
   ORDER BY sessions."start date"''')
         data= cursor.fetchall()
         print(data)
      elif int(answer)==4:
         cursor.execute('''SELECT e."EventID", e.name AS event_name, v.name AS venue_name
FROM events e
JOIN venues v ON e."VenueID" = v."VenueID" ''')
         data= cursor.fetchall()
         print(data)
      elif int(answer)==5:
         cursor.execute('''SELECT * FROM venues LEFT JOIN events ON venues."VenueID" = events."VenueID"
   WHERE events."EventID" IS NULL''')
         data= cursor.fetchall()
         print(data)
      elif int(answer)==6:
         cursor.execute('''SELECT sessions."EventID", AVG("end date" - "start date") AS AverageDuration
   FROM sessions
   WHERE sessions."EventID" = '1005'
   GROUP BY sessions."EventID"''')
         data= cursor.fetchall()
         print(data)
      elif int(answer)==7:
         cursor.execute('''SELECT * FROM events WHERE Name LIKE '%Annual%' ''')
         data= cursor.fetchall()
         print(data)
      elif int(answer)==8:
         cursor.execute('''SELECT * FROM attendees WHERE "EventID" IN ('1001', '1003', '1005') ''')
         data= cursor.fetchall()
         print(data)
      elif int(answer)==9:
         cursor.execute('''SELECT * FROM sessions WHERE "start date" BETWEEN '2022-01-01 09:00:00' AND '2022-01-01 18:00:00' ''')
         data= cursor.fetchall()
         print(data)
      elif int(answer)==10:
         cursor.execute('''INSERT INTO venues ("VenueID", name, address, capacity)
   VALUES (5007, 'New Venue', 'Street New number 7', 200)''')
         conn.commit()
         print("New venue entered.")
      elif int(answer)==11:
         cursor.execute('''UPDATE venues
   SET address = 'Updated Street number 8'
   WHERE "VenueID" = 5003 ''')
         conn.commit()
         print("Venue updated.")
      elif int(answer)==12:
         cursor.execute('''DELETE FROM venues
   WHERE "VenueID" = 5007''')
         conn.commit()
         print("Venue deleted.")
      else:
         break
menu()
conn.close()
