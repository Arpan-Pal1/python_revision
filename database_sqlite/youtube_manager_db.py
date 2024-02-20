import sqlite3

con = sqlite3.connect('youtube_video.db')

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
 ''')

def list_videos():
    cursor.execute("SELECT * FROM videos") # return tuple
    data = cursor.fetchall()
    if len(data) > 0:
        print("*" * 70)
        for row in data:
            print(f'Video id : {row[0]} || Video name : {row[1]} || video duration : {row[2]}')
        print("*" * 70)
    else:
        print("*" * 70)
        print("Empty list")
        print("*" * 70)

def add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES(?, ?)", (name, time))
    con.commit()
    list_videos()

def update_video(video_id, new_name, new_time):
    list_videos()
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()
    list_videos()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id, ))
    con.commit()
    list_videos()

def main():
    while True:

        print("\nYouTube manager | Choose an option")
        print("1. List all youtube videos ")
        print("2. add a youtube video ")
        print("3. update a youtube video ")
        print("4. delete a youtube video ")
        print("5. Exit the app ")

        choice = input('Enter your choice ')
        # print(videos)

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input('Enter video name: ')
                time = input('Enter video time: ')
                add_video(name, time)
            case '3':
                video_id = input('Enter your video id to update: ')
                name = input('Enter video name: ')
                time = input('Enter video time: ')
                update_video(video_id, name, time)
            case '4':
                video_id = input('Enter your video id to delete: ')
                delete_video(video_id)
            case '5':
                break
            case _:
                print('Invailed choice')

    con.close()


if __name__ == "__main__":
    main()