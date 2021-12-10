from os import chdir, mkdir, listdir, path
from subprocess import call, check_output


def get_commit_list():
    commits = check_output(
        f'git log --oneline',
        shell=True, encoding='utf-8'
    )
    commits = commits.strip().split('\n')
    return commits


def git_reverse(dirname, new_dirname):
    chdir(dirname)
    call('git checkout main', shell=True)
    commits = get_commit_list()
    chdir('..')

    mkdir(new_dirname)
    chdir(new_dirname)
    call(f'git init', shell=True)
    chdir('..')

    for commit in commits:
        print(commit)
        commit_hash, message = commit.split(maxsplit=1)

        chdir(dirname)
        call(
            f'git checkout {commit_hash}',
            shell=True
        )
        chdir('..')

        call(
            f'rsync -a {dirname}/ {new_dirname}/ --delete --exclude .git',
            shell=True
        )

        chdir(new_dirname)
        call(f'git add -A', shell=True)
        call(f'git commit -m "{message}"', shell=True)
        chdir('..')

    chdir(dirname)
    call('git checkout main', shell=True)


if __name__ == '__main__':
    git_reverse('repo', 'repo_reversed')
