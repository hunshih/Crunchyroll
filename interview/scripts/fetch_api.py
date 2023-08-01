import requests
# from api.models import Todo

def fetch(url):
    try:
        response = requests.get(url)
        data = response.json()
        # print(data) # print all
        '''
        # print individual fields
        print("userId ", data['userId'])
        print("title ", data['title'])
        print("completed ", data['completed'])
        '''


    except requests.exceptions.RequestException as e:
        print(f'Failed to fetch data from "{url}": {e}')
    except Exception as e:
        print(f'Failed to save instance: {e}')

if __name__ == '__main__':
    '''
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    fetch(url)
    '''
    url = input("url: ")
    fetch(url)