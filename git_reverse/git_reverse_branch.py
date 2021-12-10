from os import chdir
from subprocess import call, check_output


def get_commit_list():
    commits = check_output(
        'git log --oneline',
        shell=True, encoding='utf-8'
    )
    commits = commits.strip().split('\n')
    return commits


def git_reverse_branch(dirname):
    chdir(dirname)

    call('git checkout main', shell=True)
    commits = get_commit_list()

    prev_commit = None

    for commit in commits:
        commit_hash, message = commit.split(maxsplit=1)

        commit_info = check_output(
            f'git cat-file -p {commit_hash}',
            shell=True, encoding="utf-8"
        )

        commit_info = commit_info.split('\n')
        tree_hash = commit_info[0].split()[1]

        new_commit = check_output(
            f'git commit-tree {tree_hash} -m "{message}"' +
            (f' -p {prev_commit}' if prev_commit else ''),
            shell=True, encoding='utf-8'
        )

        prev_commit = new_commit

    call(f'git checkout -b reversed {prev_commit}', shell=True)
    chdir('..')


if __name__ == '__main__':
    git_reverse_branch('repo')
