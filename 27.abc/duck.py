class Duck:
    def quack(self):
        print("Duck quacks")


class Cat:
    def meow(self):
        print("Cat meows")

counter = 0

def make_it_quack(duck):
    global counter

    if counter > 0:
        duck.quack()
    else:
        counter += 1

if __name__ == "__main__":
    cat = Cat()
    cat.meow()
    make_it_quack(cat)
    # make_it_quack(cat)