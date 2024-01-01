import requests
import csv
import argparse
import logging
import pandas as pd
# import google
# from google.cloud import storage

def get_repo_data(context):
    try:
        response = requests.get(context)
        # logger(response)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            logging.error(f"Error {response.status_code} getting data from ")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request exception while getting data from: {str(e)}")

def extract_repo_details(repo_data):
    # repo_data = context['ti'].xcom_pull(key='repo_data', task_ids='get_repo_data')
    print(repo_data)
    users_details = []      
    for repo in repo_data:
        try:
            user_id = repo['userId']
            id = repo['id']
            title = repo['title']
            completed = repo['completed']
            users_details.append((id, user_id, title, completed))
        except requests.exceptions.RequestException as e:
            logging.error(f"Request exception while getting data")
    # logger(users_details)
    df = pd.DataFrame(users_details, columns=['id', 'userId', 'title','completed'])
    df.to_csv("D:/github_crawler/users_details.csv", index=False)





if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    repo_data = get_repo_data(url)
    repo_details = extract_repo_details(repo_data)

    
