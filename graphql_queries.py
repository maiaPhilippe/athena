with open("queries/repoQuery.aql", "r") as repo_query:
    repo_query = repo_query.read()

with open("queries/devQuery.aql", "r") as dev_query:
    dev_query = dev_query.read()

with open("queries/teamsQuery.aql", "r") as teams_query:
    teams_query = teams_query.read()

# with open("queries/commitArango.aql", "r") as commit_arango:
#     commit_arango = commit_arango.read()

# commit_arango = "{'committed_today': True, 'org': self.org}"


with open("queries/commitQuery.aql", "r") as commit_query:
    commit_query = commit_query.read()

with open("queries/readmeArango.aql", "r") as readme_arango:
    readme_arango = readme_arango.read()

with open("queries/readmeQuery.aql", "r") as readme_query:
    readme_query = readme_query.read()

# with open("queries/statsQuery.aql", "r") as stats_query:
#     stats_query = stats_query.read()

with open("queries/forkArango.aql", "r") as fork_arango:
    fork_arango = fork_arango.read()

with open("queries/forkQuery.aql", "r") as fork_query:
    fork_query = fork_query.read()

# with open("queries/issueArango.aql", "r") as issue_mongo:
#     issue_mongo = issue_mongo.read()

with open("queries/issueQuery.aql", "r") as issue_query:
    issue_query = issue_query.read()

# with open("queries/teamsDevArango.aql", "r") as teams_dev_arango:
#     teams_dev_arango = teams_dev_arango.read()

with open("queries/teamsDevQuery.aql", "r") as teams_dev_query:
    teams_dev_query = teams_dev_query.read()

with open("queries/teamsRepoArango.aql", "r") as teams_repo_arango:
    teams_repo_arango = teams_repo_arango.read()

with open("queries/teamsRepoQuery.aql", "r") as teams_repo_query:
    teams_repo_query = teams_repo_query.read()


def query_stats_mongo(self):
    dictionary = [dict(x) for x in self.db.Commit.find({"additions": None, "org": self.org},
                                                       {'repoName': 1, 'oid': 1, '_id': 1})]
    return dictionary


def issue_mongo(self):
    dictionary = [dict(x) for x in self.db.Repo.find({"org": self.org, "issues": {"$gt": 0}},
                                                     {'repoName': 1, '_id': 0})]
    query_list = []
    [query_list.append(str(value["repoName"])) for value in dictionary]
    return query_list


def query_fork_mongo(self):
    dictionary = [dict(x) for x in self.db.Repo.find({"org": self.org, "forks": {"$gt": 0}},
                                                     {'repoName': 1, '_id': 0})]
    query_list = []
    [query_list.append(str(value["repoName"])) for value in dictionary]
    return query_list


def query_team_mongo(self):
    dictionary = [dict(x) for x in self.db.Teams.find({"org": self.org, "membersCount": {"$gt": 100}},
                                                      {'slug': 1, '_id': 0})]
    query_list = []
    [query_list.append(str(value["slug"])) for value in dictionary]
    return query_list


def query_commit_mongo(self):
    dictionary = [dict(x) for x in
                  self.db.Repo.find({'committed_today': True, 'org': self.org}, {'repoName': 1, '_id': 0})]
    query_list = []
    [query_list.append(str(value["repoName"])) for value in dictionary]
    return query_list


def stats_query(self, repository):
    return self.org + "/" + str(repository["repoName"]) + '/commits/'


def query_teams_dev_mongo(self):
    dictionary = [dict(x) for x in self.db.Teams.find({'org': self.org, "membersCount": {'$gt': 100}},
                                                      {'slug': 1, '_id': 0})]
    query_list = []
    [query_list.append(str(value["slug"])) for value in dictionary]
    return query_list


def query_teams_repo_mongo(self):
    dictionary = [dict(x) for x in self.db.Teams.find({'org': self.org, "repoCount": {'$gt': 100}},
                                                      {'slug': 1, '_id': 0})]
    query_list = []
    [query_list.append(str(value["slug"])) for value in dictionary]
    return query_list
