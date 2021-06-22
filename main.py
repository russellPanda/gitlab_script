#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/5/27 17:25
# @Author : russell
# @File :  main


from gitlab_handle import GitlabServer
from pprint import pprint 

url = 'http://192.168.1.71'
private_token = 'iyoDMf-prsEY1HF9bVtF'




def main():
    server = GitlabServer(url, private_token)

    projects=[]
    try:
        for project in server.all_projects():
            branchs_name=[ branch.name for branch in project.branches.list() ]
            projects.append((project.http_url_to_repo,branchs_name))
        # repo_urls= [ p.http_url_to_repo for p in server.all_projects() ]
    except Exception as e:
        print(f"error {e}")


    pprint(projects)


if __name__ =='__main__':
    main()
