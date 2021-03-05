#/usr/bin/python3

import requests
from typing import NoReturn, List

from github import GithubApi, GithubRepo

def main(repo: GithubRepo) -> NoReturn:
    workflow_ids = [w['id'] for w in repo.workflows()]
    # print(workflow_ids)

    # print([data['id'] for data in repo.workflow_runs(2991279)])

    # print(repo.workflow_run_timings(620771442)['run_duration_ms'])

    ordered_run_timings = {}
    for wid in workflow_ids:
        workflow_runs = repo.workflow_runs(wid)
        ordered_run_timings[wid] = [r['id'] for r in workflow_runs]

    print(ordered_run_timings.keys())
    
if __name__ == '__main__':
    gh_api = GithubApi(credentials={
        'username': 'GuyARoss',
        'password': ''
    })

    main(GithubRepo(gh_api, 'quick-lint', 'quick-lint-js'))
