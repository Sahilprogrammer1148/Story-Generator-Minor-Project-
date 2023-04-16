import random

def rand_story():
    start=['Once upon a time','Long time ago','Few years ago','A century ago']
    character=[', there lived a king.\n',', there was a man named Ashley.\n',', there lived a girl.\n']
    time=['One day, ','One night, ','Few days ago, ']
    story_plot1=['he told his daughter that they will go to ','he told his son that they will go to ','his father told him that they will have a visit ']
    place=['Shimla ','Manali ','Dehradun ','Hill station ','Musoorie ']
    story_plot2=['for trekking.','for a trip.','on a vacation.']
    story_plot3=[' They both were excited.',' They both were happy.']
    story_plot4=['\nThe day arrived.','\nAtlast, the day came.']
    story_plot5=[' It was a cold morning.',' It was a sunny day.',' The weather was hazy.',' It was a rainy day.']
    story_plot5=[' Both of them enjoyed their day and did lot of fun.',' Both of them did trekking and did many adventurous activity.',
                 ' Both of them enjoyed and did a lot of swimming in the hot water spring.',' Both of them played games and together and spend an awesome day.']
    story_plot6=['\n\nOn their return, the child said that it was fun to be with you today.','\n\nOn their way back to home, the child said that this was the best time they had spent together.']
    story_plot7=[' Father smiled at his child and hugged him.',' This was also my happy time with you, father said with a smile on his face.']
    moral=['\n\nMoral: Sometimes, happiness is also found in little things','\n\nMoral: Happiness can neither be purchased nor bought.',
                 '\n\nMoral: Nothing is more valuable than spending time wid your loved ones.']
    
    
    print(random.choice(start)+random.choice(character)+random.choice(time)+random.choice(story_plot1)+random.choice(place)+random.choice(story_plot2)+random.choice(story_plot3)+
          random.choice(story_plot4)+random.choice(story_plot5)+random.choice(story_plot6)+random.choice(story_plot7)+random.choice(moral))


def intro():
    print("\t\t\t***********************************")
    print("\t\t\tRANDOM STORY GENERATOR")
    print("\t\t\t***********************************")
    print("\n\n\t\tPress ENTER to get the stories out of the BOX!!!")
    input()

def extro():
    print("\n\n\t\t\tProject created by:    1. SAKSHI R SHINDE\n\t\t\t\t\t 2. M S Mohamed Shahasin \n\t\t\t\t\t 3. Ayush Kumar Ankit")

#Main execution of the program starts here...
ch='Y'
intro()

while ch != 'N' or ch != 'n':
    if ch=='Y' or ch=='y':
        rand_story()
    else:
        print('Sorry, its a wrong choice!!\nHit your chances once again.')

    ch=input('\nWant to read one more story??? (Y/N) ')
    if ch=='N' or ch=='n':
        print('\n\tTHANK YOU for reading the story!!! Hope to see you again.')
        break

extro()
