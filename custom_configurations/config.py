import os

token = os.getenv("GRAPHQL_TOKEN")
db_name = os.getenv("DB_NAME")
db_url = os.getenv("MONGODB_URL")
username = os.getenv("MONGODB_USER")
password = os.getenv("MONGODB_PASS")
url = os.getenv("GITHUB_GRAPHQL_URL")  # GitHub GraphQL API url
url_rest_api = os.getenv("GITHUB_REST_URL")
number_of_repos = 100
repo_number_of_repos = 50
timeout = 100.001
since_time_days_delta = os.getenv("SINCE_TIME_DAYS_DELTA")  # days ago ex: -5
until_time_days_delta = os.getenv("UNTIL_TIME_DAYS_DELTA")  # delta days from now ex: +1
orgs = ["stone-payments", "mundipagg", "cappta", "equals-conc", "pagarme"]
update = 1  # update every x hours
queue_max_size = 1500000
num_of_threads = 1
queue_timeout = 15
rest_minutes = 20  # minutes to rest and start collect again
rate_limit_to_sleep = 10  # minimum remaining api value to wait next reset
hash_indexes = [["Dev", "devName"], ["Dev", "login"], ["Teams", "teamName"],
                ["Commit", "org"], ["Issue", "repoName"], ["Repo", "readme"], ["Commit", "author"],
                ["Repo", "repoName"], ["Repo", "openSource"], ["Repo", "licenseId"], ["Repo", "licenseType"],
                ["Issue", "closeAt"], ["Issue", "createdAt"], ["Commit", "committedDate"], ["Fork", "createdAt"]]
hash_indexes_unique = []
skip_list_indexes = [["Issue", "closeAt"], ["Issue", "createdAt"], ["Commit", "committedDate"], ["Fork", "createdAt"]]
full_text_indexes = [["Repo", "repoName"], ["Teams", "teamName"], ["Issue", "org"],
                     ["Commit", "org"], ["Fork", "org"], ["Dev", "login"]]
abuse_time_sleep = 2
max_interval = 50  # max interval time for requests
max_retries = 10  # max request retries