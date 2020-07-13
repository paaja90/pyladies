class Movie:
    def __init__(self, name):
        self.name = name
    def origin(self, country):
        print("The movie called '{}' was made in {}".format(self.name,country))
    def main_actor(self,actor):
        print("{} starred in the movie called '{}'".format(actor,self.name))

class Horror(Movie):
    def mood(self):
        print('This movie will scare you!')

class Commedy(Movie):
    def mood(self):
        print('This movie will make you laugh.')

class Documentary(Movie):
    def mood(self):
        print('You will listen to some facts in this movie.')
    def main_actor(self):
        print('There is no real actor in documentary movies.')
    



saw = Horror('Saw')
saw.origin('USA')
saw.main_actor('John D.')
earth = Documentary('Earth')
earth.main_actor()
