from lib.action import BitBucketAction


class DeleteSshKeyAction(BitBucketAction):
    def run(self, repo, key_id):
        """
        Delete SSH key from BitBucket account
        """
        bb = self.perform_request(repo=repo)
        succ, res = bb.ssh.delete(key_id=key_id)
        return succ, res
