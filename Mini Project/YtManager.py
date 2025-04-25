import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="root",
   database="YtManager"
)

cur = db.cursor()

# Createing table videos
cur.execute('''
   CREATE TABLE IF NOT EXISTS videos(
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      time VARCHAR(255) NOT NULL
   )
''')

# Function to list videos
def list_videos():
   cur.execute("SELECT * FROM videos")
   rows = cur.fetchall()
   if not rows:
      print("** No data Available **")
   else:
      print("\n{:<5} {:<25} {:<15}".format("ID", "Title", "Time"))
      print("-" * 50)
      for row in rows:
         print("{:<5} {:<25} {:<15}".format(row[0], row[1], row[2]))
      print("-" * 50)

# Function to add a new video
def add_video(name, time):
   cur.execute("INSERT INTO videos(name, time) VALUES (%s, %s)", (name, time))
   db.commit()
   print("✅ Video added successfully!")

# Function to update a video
def update_video(video_id, new_name, new_time):
   cur.execute("UPDATE videos SET name=%s, time=%s WHERE id=%s", (new_name, new_time, video_id))
   db.commit()
   print("✅ Video updated successfully!")

# Function to delete a video
def delete_video(video_id):
   cur.execute("DELETE FROM videos WHERE id=%s", (video_id,))
   db.commit()
   print("🗑️ Video deleted successfully!")

# Main app loop
def main():
   while True:
      print("\n Youtube Manager with MySQL DB")
      print("1. List videos")
      print("2. Add video")
      print("3. Update video")
      print("4. Delete video")
      print("5. Exit App")
      choice = input("Enter your choice: ")

      if choice == '1':
         list_videos()
      elif choice == '2':
         name = input("Enter the Title of video: ")
         time = input("Enter the Time of video: ")
         add_video(name, time)
      elif choice == '3':
         video_id = input("Enter video id to update: ")
         name = input("Enter the new Title of video: ")
         time = input("Enter the new Time of video: ")
         update_video(video_id, name, time)
      elif choice == '4':
         video_id = input("Enter video id to delete: ")
         delete_video(video_id)
      elif choice == '5':
         print("👋 Exiting the app. Goodbye!")
         break
      else:
         print("⚠️ Invalid choice! Please enter a number between 1 and 5.")

   cur.close()
   db.close()

if __name__ == '__main__':
    main()
