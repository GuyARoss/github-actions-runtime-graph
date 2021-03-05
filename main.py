#/usr/bin/python3

import requests
import argparse
from typing import NoReturn, List

from github import GithubApi, GithubRepo
from plots import create_time_plt

def main(repo: GithubRepo) -> NoReturn:
    for workflow in repo.workflows():
        wid = workflow['id']
        create_time_plt(
            name=workflow.get('name', 'n/ a'),
            timings=[repo.workflow_run_timings(r['id']).get('run_duration_ms', 0) / 1000 for r in repo.workflow_runs(wid)]
        )

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', '--user', help='username of the generated token')
    parser.add_argument('--token', '--token', help='generated github token')
    parser.add_argument('--repo', '--repo', help='repo of the workflows')
    parser.add_argument('--owner', '--owner', help='owner of the repo')

    args = parser.parse_args()

    gh_api = GithubApi(credentials={
        'username': args['user'],
        'password': args['token']
    })

    main(GithubRepo(gh_api, args['owner'], args['repo']))
