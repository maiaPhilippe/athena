from apistar import Route, Response, http
from apistar.frameworks.wsgi import WSGIApp as Webhook
from queue import Queue
from webhook.webhook_event_router import WebhookEventRouter

webhook_queue = Queue(10000)
event_router = WebhookEventRouter(webhook_queue)
event_router.start()


def hook(request: http.Request, data: http.RequestData):
    event = dict(request.headers)['x-github-event']
    status, headers = github_event(event, data)
    if status:
        return Response({}, status=202, headers=headers)
    else:
        return Response({}, status=500, headers=headers)


def github_event(event, data):
    headers = {}
    data = {
      "ref": "refs/heads/master",
      "before": "9049f1265b7d61be4a8904a9a27120d2064dab3b",
      "after": "0d1a26e67d8f5eaf1f6ba5c57fc3c7d91ac0fd1c",
      "created": False,
      "deleted": False,
      "forced": False,
      "base_ref": None,
      "compare": "https://github.com/baxterthehacker/public-repo/compare/9049f1265b7d...0d1a26e67d8f",
      "commits": [
        {
          "id": "0d1a26e67d8f5eaf1f6ba5c57fc3c7d91ac0fd1c",
          "tree_id": "f9d2a07e9488b91af2641b26b9407fe22a451433",
          "distinct": True,
          "message": "Update README.md",
          "timestamp": "2018-04-03T15:55:02-03:00",
          "url": "https://github.com/baxterthehacker/public-repo/commit/0d1a26e67d8f5eaf1f6ba5c57fc3c7d91ac0fd1c",
          "author": {
            "name": "baxterthehacker",
            "email": "baxterthehacker@users.noreply.github.com",
            "username": "baxterthehacker"
          },
          "committer": {
            "name": "baxterthehacker",
            "email": "baxterthehacker@users.noreply.github.com",
            "username": "baxterthehacker"
          },
          "added": [

          ],
          "removed": [

          ],
          "modified": [
            "README.md"
          ]
        }
      ],
      "head_commit": {
        "id": "0d1a26e67d8f5eaf1f6ba5c57fc3c7d91ac0fd1c",
        "tree_id": "f9d2a07e9488b91af2641b26b9407fe22a451433",
        "distinct": True,
        "message": "Update README.md",
        "timestamp": "2015-05-05T19:40:15-04:00",
        "url": "https://github.com/baxterthehacker/public-repo/commit/0d1a26e67d8f5eaf1f6ba5c57fc3c7d91ac0fd1c",
        "author": {
          "name": "baxterthehacker",
          "email": "baxterthehacker@users.noreply.github.com",
          "username": "baxterthehacker"
        },
        "committer": {
          "name": "baxterthehacker",
          "email": "baxterthehacker@users.noreply.github.com",
          "username": "baxterthehacker"
        },
        "added": [

        ],
        "removed": [

        ],
        "modified": [
          "README.md"
        ]
      },
      "repository": {
        "id": 35129377,
        "name": "cof-accountcontrol-accountmanager",
        "full_name": "baxterthehacker/public-repo",
        "owner": {
          "name": "baxterthehacker",
          "email": "baxterthehacker@users.noreply.github.com"
        },
        "private": False,
        "html_url": "https://github.com/baxterthehacker/public-repo",
        "description": "",
        "fork": False,
        "url": "https://github.com/baxterthehacker/public-repo",
        "forks_url": "https://api.github.com/repos/baxterthehacker/public-repo/forks",
        "keys_url": "https://api.github.com/repos/baxterthehacker/public-repo/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/baxterthehacker/public-repo/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/baxterthehacker/public-repo/teams",
        "hooks_url": "https://api.github.com/repos/baxterthehacker/public-repo/hooks",
        "issue_events_url": "https://api.github.com/repos/baxterthehacker/public-repo/issues/events{/number}",
        "events_url": "https://api.github.com/repos/baxterthehacker/public-repo/events",
        "assignees_url": "https://api.github.com/repos/baxterthehacker/public-repo/assignees{/user}",
        "branches_url": "https://api.github.com/repos/baxterthehacker/public-repo/branches{/branch}",
        "tags_url": "https://api.github.com/repos/baxterthehacker/public-repo/tags",
        "blobs_url": "https://api.github.com/repos/baxterthehacker/public-repo/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/baxterthehacker/public-repo/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/baxterthehacker/public-repo/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/baxterthehacker/public-repo/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/baxterthehacker/public-repo/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/baxterthehacker/public-repo/languages",
        "stargazers_url": "https://api.github.com/repos/baxterthehacker/public-repo/stargazers",
        "contributors_url": "https://api.github.com/repos/baxterthehacker/public-repo/contributors",
        "subscribers_url": "https://api.github.com/repos/baxterthehacker/public-repo/subscribers",
        "subscription_url": "https://api.github.com/repos/baxterthehacker/public-repo/subscription",
        "commits_url": "https://api.github.com/repos/baxterthehacker/public-repo/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/baxterthehacker/public-repo/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/baxterthehacker/public-repo/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/baxterthehacker/public-repo/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/baxterthehacker/public-repo/contents/{+path}",
        "compare_url": "https://api.github.com/repos/baxterthehacker/public-repo/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/baxterthehacker/public-repo/merges",
        "archive_url": "https://api.github.com/repos/baxterthehacker/public-repo/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/baxterthehacker/public-repo/downloads",
        "issues_url": "https://api.github.com/repos/baxterthehacker/public-repo/issues{/number}",
        "pulls_url": "https://api.github.com/repos/baxterthehacker/public-repo/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/baxterthehacker/public-repo/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/baxterthehacker/public-repo/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/baxterthehacker/public-repo/labels{/name}",
        "releases_url": "https://api.github.com/repos/baxterthehacker/public-repo/releases{/id}",
        "created_at": 1430869212,
        "updated_at": "2015-05-05T23:40:12Z",
        "pushed_at": 1430869217,
        "git_url": "git://github.com/baxterthehacker/public-repo.git",
        "ssh_url": "git@github.com:baxterthehacker/public-repo.git",
        "clone_url": "https://github.com/baxterthehacker/public-repo.git",
        "svn_url": "https://github.com/baxterthehacker/public-repo",
        "homepage": False,
        "size": 0,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": False,
        "has_issues": False,
        "has_downloads": False,
        "has_wiki": False,
        "has_pages": False,
        "forks_count": 0,
        "mirror_url": False,
        "open_issues_count": 0,
        "forks": 0,
        "open_issues": 0,
        "watchers": 0,
        "default_branch": "master",
        "stargazers": 0,
        "master_branch": "master"
      },
      "pusher": {
        "name": "baxterthehacker",
        "email": "baxterthehacker@users.noreply.github.com"
      },
      "sender": {
        "login": "baxterthehacker",
        "id": 6752317,
        "avatar_url": "https://avatars.githubusercontent.com/u/6752317?v=3",
        "gravatar_id": "",
        "url": "https://api.github.com/users/baxterthehacker",
        "html_url": "https://github.com/baxterthehacker",
        "followers_url": "https://api.github.com/users/baxterthehacker/followers",
        "following_url": "https://api.github.com/users/baxterthehacker/following{/other_user}",
        "gists_url": "https://api.github.com/users/baxterthehacker/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/baxterthehacker/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/baxterthehacker/subscriptions",
        "organizations_url": "https://api.github.com/users/baxterthehacker/orgs",
        "repos_url": "https://api.github.com/users/baxterthehacker/repos",
        "events_url": "https://api.github.com/users/baxterthehacker/events{/privacy}",
        "received_events_url": "https://api.github.com/users/baxterthehacker/received_events",
        "type": "User",
        "site_admin": False
      }
    }
    if event == 'ping':
        headers['x-stone-event'] = 'pong'
        return True, headers
    else:
        webhook_queue.put([event, data])
        headers['x-stone-event'] = event
        return True, headers


routes = [
    Route('/hook', 'POST', hook),
]

app = Webhook(routes=routes)


if __name__ == '__main__':
    app.main()
