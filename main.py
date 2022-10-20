import os

repo_folder = '/Users/senolsahin/test'

def main():
    createFolder()
    
def createFolder():
    project_name = input('Enter new project name: ')
    if os.path.exists(repo_folder + '/{}'.format(project_name)):
        print('Project already exists')
        createFolder()
    else:
        os.mkdir(repo_folder + '/{}'.format(project_name))
        print('Project created')
    create_readme_md(project_name)
    return project_name

def create_readme_md(project_name):
    with open(repo_folder + '/{}/README.md'.format(project_name), 'w') as f:
        f.write('''
#Setup

python3 -m venv env

source env/bin/activate

pip install -r requirements.txt
''')
    print('README.md Created')
    create_main_py(project_name)

def create_main_py(project_name):
    with open(repo_folder + '/{}/main.py'.format(project_name), 'w') as f:
        f.write('# {}'.format(project_name))
    print('main.py Created')
    createvenv(project_name)
    
def createvenv(project_name):
    # we need to run this command inside the project folder
    os.chdir(repo_folder + '/{}'.format(project_name))
    os.system('python3 -m venv env')
    print('venv Created')
    createRequirementsTxt(project_name)

def createRequirementsTxt(project_name):
    userchoice = input('Do you want to install any packages? (y/n): ')
    if userchoice == 'y':
        packagename = input('Enter package name: ')
        with open(repo_folder + '/{}/requirements.txt'.format(project_name), 'w') as f:
            f.write(packagename)
        print('requirements.txt Created')
        copygitignore(project_name)
    elif userchoice == 'n':
        with open(repo_folder + '/{}/requirements.txt'.format(project_name), 'w') as f:
            f.write('')
        print('requirements.txt Created')
        copygitignore(project_name)
    else:
        print('Please enter y or n')
        createRequirementsTxt(project_name)
    copygitignore(project_name)

def copygitignore(project_name):
    source = '/Users/senolsahin/test/envCreator/.gitignore'
    dest = repo_folder + '/{}/.gitignore'.format(project_name)
    open(dest, 'w').write(open(source).read())
    print('Gitigore file copied')
    openVSCode(project_name)

def openVSCode(project_name):
    filepath = repo_folder + '/{}'.format(project_name)
    os.system('code {}'.format(filepath))
    print('VSCode Opened for project')

if __name__ == '__main__':
    main()