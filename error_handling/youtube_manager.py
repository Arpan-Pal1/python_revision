import json

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f'{index}. video name - {video['name']} duration - {video['time']}')

def add_video(videos):
    video_name = input('Enter video name: ')
    video_time = input('Enter video time:  ')
    videos.append({'name' : video_name, 'time' : video_time})
    save_data_helper(videos)

def update_video(videos):
    print('\nchoose which one you want to update ')
    list_all_videos(videos)
    choice = int(input('Enter your choice '))
    if choice in range(1, len(videos)+1):
        name = input('enter updated name ')
        time = input('enter your time ')
        videos[choice - 1] = {'name' : name, 'time' : time}
        save_data_helper(videos)

    else:
        print('invaild choice | Please enter 3 and then choose the right option')

def delete_video(videos):
    print('\nchoose which one you want to delete ')
    list_all_videos(videos)
    choice = int(input('Enter your choice '))
    if choice in range(1, len(videos)+1):
        videos.pop(choice - 1)
        save_data_helper(videos)
        print('Successfully Deleted')
        list_all_videos(videos)

    else:
        print('invaild choice | Please enter 4 and then choose the right option')

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def main():
    videos = load_data()

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
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print('Invailed choice')


if __name__ == "__main__":
    main()