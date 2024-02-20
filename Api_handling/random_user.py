import requests

def fetch_random_user():
    response = requests.get('https://api.freeapi.app/api/v1/public/randomusers/user/random')
    data = response.json()
    
    if data['success'] and 'data' in data:
        user_data = data['data']
        user_name = f'{user_data['name']['first']} {user_data['name']['last']}'
        user_country = user_data['location']['country']
        return user_name, user_country
    else:
        raise Exception("Failed to fetch user data")


def main():  # Always handle web request in a try exception
    try:
        user_name, user_country = fetch_random_user()
        print(f'User name is {user_name}')
        print(f'User Country is {user_country}')
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
