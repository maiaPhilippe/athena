from collectors_and_savers.collector import *


class Commit:
    def __init__(self, db, org, query, query_db, collection_name, save_queue_type, edge_name="edges"):
        self.db = db
        self.org = org
        self.query = query
        self.query_db = query_db
        self.collection_name = collection_name
        self.save_queue_type = save_queue_type
        self.edge_name = edge_name

    def content(self, response, node):
        save_content = {
            "collection_name": string_validate(self.collection_name, not_none=True),
            "org": string_validate(self.org, not_none=True),
            "_id": not_null(find_key('commitId', node)),
            "repositoryId": string_validate(find_key('repositoryId', response), not_none=True),
            "repoName": string_validate(find_key('repoName', response), not_none=True),
            "branchName": string_validate(find_key('branchName', response)),
            "messageHeadline": string_validate(find_key('messageHeadline', node)),
            "oid": not_null(find_key('oid', node)),
            "committedDate": convert_datetime(find_key('committedDate', node)),
            "author": string_validate(find_key('login', node)),
            "devId": string_validate(find_key('devId', node)),
            "commitId": string_validate(find_key('commitId', node)),
            'additions': int_validate(find_key('additions', node)),
            'deletions': int_validate(find_key('deletions', node)),
            'numFiles': int_validate(find_key('changedFiles', node)),
            "db_last_updated": datetime.datetime.utcnow(),
        }
        return save_content

    @staticmethod
    def edges(node):
        save_edges = [{
            "edge_name": "dev_to_commit",
            "to": find_key('commitId', node),
            "from": find_key('devId', node),
            "db_last_updated": datetime.datetime.utcnow(),
        },
            {
                "edge_name": "repo_to_commit",
                "to": find_key('commitId', node),
                "from": find_key('repositoryId', node),
                "db_last_updated": datetime.datetime.utcnow(),
            },
            {
                "edge_name": "repo_to_dev",
                "to": find_key('devId', node),
                "from": find_key('repositoryId', node),
                "db_last_updated": datetime.datetime.utcnow(),
            }
        ]
        return save_edges

    def collect(self):
        start = CollectorRestricted(db=self.db, collection_name=self.collection_name, org=self.org,
                                    edges=self.edge_name, query=self.query, updated_utc_time=utc_time,
                                    query_db=self.query_db, number_of_repo=number_pagination, save_content=self.content,
                                    save_edges=self.edges)
        start.start(self.save_queue_type)
