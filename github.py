#/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth

class GithubApi():
    def __init__(self, credentials: dict):
        self.auth = HTTPBasicAuth(credentials['username'], credentials['password'])

    def get_request(self, uri: str):
        resp = requests.get(f'https://api.github.com/{uri}', auth=self.auth).json()
        return resp
    
class GithubRepo():
    def __init__(self, api, owner, repo):
        self.owner = owner
        self.repo = repo
        self.api = api

    def workflows(self):
        resp = self.api.get_request(f'repos/{self.owner}/{self.repo}/actions/workflows')
        return resp.get('workflows', [])

    def workflow_runs(self, workflow_id: int):
        resp = self.api.get_request(f'repos/{self.owner}/{self.repo}/actions/workflows/{workflow_id}/runs')
        return resp.get('workflow_runs', [])

    def workflow_run_timings(self, run_id: int):
        resp = self.api.get_request(f'repos/{self.owner}/{self.repo}/actions/runs/{run_id}/timing')
        return resp

