from Node import Node


class Main:
    def __init__(self):
        self.open = []
        self.goal = self.getGoal()
        self.start = self.getStart()
        self.counter = 0

    def getGoal(self):
        return [
            ['0', '1', '2'],
            ['3', '4', '5'],
            ['6', '7', '8']
        ]

    def getStart(self):
        array2D = []
        with open('mp1input.txt', 'r') as reader:
            for line in reader.readlines():
                oneline = line.split(' ')
                newl = list(map(lambda x: x.rstrip('\n'), oneline))
                array2D.append(newl)
        return array2D

    def getFScore(self, inital, goal):
        hScore = self.getHScore(inital.data, goal)
        gScore = inital.level
        return hScore + gScore

    def getHScore(self, startData, goal):
        count = 0
        for i in range(len(startData)):
            for j in range(len(startData[0])):
                current = startData[i][j]
                other = goal[i][j]
                if current != other and current != '0':
                    count += 1
        return count

    def pintPuzzle(self, puzzle):
        for i in puzzle.data:
            for j in i:
                print(j, end=" ")
            print("")

    def applyAStar(self):
        print(
            'Artificial Intelligence \n MP1: A* for Sliding Puzzle \nSEMESTER: [Spring 2021]\nNAME: [Muhammed Kerim Kutuk]')
        print('##########')
        inital = Node(self.start, 0, None)
        inital.fscore = self.getFScore(inital, self.goal)
        self.open.append(inital)
        while True:
            puzzle = self.open[0]
            print(f"MOVE : {puzzle.direction}")
            self.pintPuzzle(puzzle)
            print('##########')
            if self.getHScore(puzzle.data, self.goal) == 0:
                break
            neighborPuzzles = puzzle.createSides()
            for sub in neighborPuzzles:
                self.counter += 1
                sub.fscore = self.getFScore(sub, self.goal)
                self.open.append(sub)
            del self.open[0]
            self.open.sort(key=lambda x: x.fscore)
        print(f"number of states visited {self.counter - 2}")


main = Main()
main.applyAStar()
