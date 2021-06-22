#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/5/18 21:11
# @Author : russell
# @File :  test


import gitlab
from pprint import pprint




class GitlabServer:

    def __init__(self, url: str, private_token: str):
        self.server = gitlab.Gitlab(url=url, private_token=private_token)
        self.projects = self.all_projects()
        self.users = self.all_user()
        self.groups = self.all_groups()

    def get_user(self, name: str):
        user = self.server.users.list(username=name)[0]
        return user

    def get_group(self, name: str):
        group = self.server.groups.list(groupname=name)[0]
        return group

    def get_project(self, name):
        project = self.server.projects.list(projectname=name)[0]
        return project

    def all_user(self):
        return self.server.users.list(all=True)

    def all_groups(self):
        return self.server.groups.list(all=True)

    def all_projects(self):
        return self.server.projects.list(all=True)

    @classmethod
    def projects_of_group(cls, group):
        return group.projects.list(all=True)

    @classmethod
    def users_of_group(cls, group):
        return group.members.list()

    @classmethod
    def branches_of_project(cls, project):
        try:
            branches=project.branches.list(all=True)
        except Exception as e:
            print(f'get branches error :{e}')
            branches=[]
        return branches

    def create_repo(self,name):
        return self.server.projects.create({'name': name})


