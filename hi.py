import requests 
import json 
 
#Insert facebook token here 
access_token = "EAANHMin5uKQBANdJpOiTcerZC8RZBFpZCc29eeiGjZAWZB6ZBk0UEyJE2aeo3jtcdkZAkx8DwXs2yHQ9u3sE5V0tgENKC1voJns7GE7AZBhCerLmZCjGvmUyvGwtagYsToshhut8XHwCWpSgv1yKkZC0ff1BmfE0lzDNeFrJUJkqUoPwpQqTh3HAFP" 
 
def comment_on_posts(posts, amount): 
    counter = 0 
    for post in posts: 
        if counter >= amount: 
            break 
        else: 
            counter = counter + 1 
        url = "https://graph.facebook.com/{0}/comments".format(post['id']) 
        message = "Hi bro!" 
        parameters = {'access_token' : access_token, 'message' : message} 
        s = requests.post(url, data = parameters) 
 
def get_posts(): 
    payload = {'access_token' : access_token} 
    r = requests.get('https://graph.facebook.com/me/feed', params=payload) 
    result = json.loads(r.text) 
    return result['data'] 
 
if __name__ == "__main__": 
    posts = get_posts() 
    comment_on_posts(posts, 25) 