from bs4 import BeautifulSoup
import os
import subprocess




def extractnames(path):

    usernames = []

    with open(path, 'r', encoding = 'utf-8') as file:
        html_content = file.read()

        soup = BeautifulSoup(html_content, 'lxml')
        links = soup.find_all('a', href=True)
        for link in links:
            href = link['href']
            if 'instagram.com' in href:
                usernames.append(href[26:])

    return usernames

path = input('Input the path of the folder you installed\n Ex: ' + r'(Users\Name\Downloads\instagrams...)' + '\n')

followingpath = path + r'\connections\followers_and_following\following.html'
followerspath = path + r'\connections\followers_and_following\followers_1.html'


try:
    users_following = extractnames(followingpath)
    users_followers = extractnames(followerspath)
except:
    print('The files you input do not exist')
    exit()

notfollowedback = []
notfollowingback = []

for following in users_following:
    if following not in users_followers:
        notfollowedback.append(following)

for follower in users_followers:
    if follower not in users_following:
        notfollowingback.append(follower)


with open('conclusion.txt', 'w') as file:
    file.write(f'There are {len(notfollowedback)} people not following you back\n')
    file.write('List of people not following you back: \n')

    for name in notfollowedback:
        file.write(f'{name} \n')
    
    file.write('\n' * 5)

    file.write(f'There are {len(notfollowingback)} people you dont follow back\n')
    for name in notfollowingback:
        file.write(f'{name} \n')

    print('File has been created.')
    os.startfile('conclusion.txt')


