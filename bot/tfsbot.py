from tfs import TFSAPI
import requests, urllib.request, json, base64, os
from requests_ntlm import HttpNtlmAuth

username = # Your username
password = # Your password
DefaultCollectionURL = # Your company's tfs default page i.e https://secure.companyname.com/tfs/Product/

def get_closed_p1_defects(connect, project):
    query = """SELECT
    [System.WorkItemType]
    FROM workitems
    WHERE
        [System.TeamProject] = "%s" AND [Priority] = "1" AND [System.State] = "Closed"
    """
    project_query = query % (project)
    wiql = connect.run_wiql(project_query, params={'api-version':'2.2'})
    raw = wiql.result
    wi = raw['workItems']
    countwi = len(wi)
    return countwi

def get_total_defects(connect, project):
    query = """SELECT
    [System.WorkItemType]
    FROM workitems
    WHERE
        [System.TeamProject] = "%s" AND [System.WorkItemType] = "Defect"
    """
    project_query = query % (project)
    wiql = connect.run_wiql(project_query, params={'api-version':'2.2'})
    raw = wiql.result
    wi = raw['workItems']
    countwi = len(wi)
    return countwi

def main():
    word_end = ''
    print('Hey There!, What would project would you like to query?')
    print('Please type the exact project name as I am not that smart yet!')
    while word_end != 'Goodbye':
        project_name = input("Project 1 or Project 2:\n")
        if project_name == "":
            help = input("You didn't enter anything? would you like me to help?\n")
            if help == "No" or help == "":
                word_end = "Goodbye"
            else:
                print("Ok, What project would you like to query?")
        elif project_name == "Project 1" or project_name == "project 1":
            Project1_connect = TFSAPI(DefaultCollectionURL, project='Project1', user=username, password=password, auth_type=HttpNtlmAuth)
            print("--------------------------")
            print("All Defects")
            print(get_total_defects(Project1_connect, project_name))
            print("--------------------------")
            print("All Closed P1 Defects")
            print(get_closed_p1_defects(Project1_connect, project_name))
            print("--------------------------")
        elif project_name == "Project2 or project_name == "project2":
            Project2_connect = TFSAPI(DefaultCollectionURL, project='Project2', user=username, password=password, auth_type=HttpNtlmAuth)
            print("--------------------------")
            print("All Defects")
            print(get_total_defects(Project2_connect, project_name))
            print("--------------------------")
            print("All Closed P1 Defects")
            print(get_closed_p1_defects(Project2_connect, project_name))
            print("--------------------------")
        elif project_name != "Project1" or project_name != "Project2":
            print("I cannot access that project!, I can only access Project 1 or Project 2")
    print("Ok, Goodbye")    

if __name__ == "__main__":
    main()