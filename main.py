import random as r
import sys
sys.path.append('./1/1.1')
sys.path.append('./1/1.2')
sys.path.append('./2/2.1')
sys.path.append('./3')

import oneDotOne
import oneDotTwo
import twoDotOne
import three

if __name__ == "__main__":
    print("Hi! This is to learn about shared objects.")
    print("I shall collect one random number from each sub-module.")

    initFirst = oneDotOne.ready()
    first = oneDotOne.get()

    initSecond = oneDotTwo.ready()
    second = oneDotOne.get()

    initThird = twoDotOne.ready()
    third = twoDotOne.get()

    initFourth = three.ready()
    fourth = three.get()

    print("Following is what I collected. Also, here is a random number from me - ", r.randint(5,100))
    print("1 - ", first, "2 - ", second, "3 - ", third, "4 - ", fourth)
    print("Exiting gracefully.")


