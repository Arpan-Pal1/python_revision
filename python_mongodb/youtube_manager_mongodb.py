from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.iew4tvo.mongodb.net/")

# Id and password

try:
    db = client['ytmanager']
    video_collection = db['videos']
except Exception as e:
    print(e)

# print(video_collection)



def list_videos():
    print("*" * 70)
    for video in video_collection.find():
        print(f'ID {video['_id']} | name : {video['name']} | Duration : {video['time']}')
        print('-'*70)
    print("*" * 70)

def add_video(name, time):
    video_collection.insert_one({
        'name' : name,
        'time' : time
    })
    list_videos()

def update_video(video_id, name, time):
    video_collection.update_one(
        {'_id' : ObjectId(video_id)}, 
        {"$set" : {'name' : name, 'time' : time}}
        )
    list_videos()

def delete_video(video_id):
    video_collection.delete_one({'_id' : ObjectId(video_id)})
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



if __name__ == '__main__':
    main()