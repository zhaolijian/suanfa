class AnimalShelf:

    def __init__(self):
        self.queue_cat = []
        self.queue_dog = []

    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0:
            self.queue_cat.append(animal[0])
        elif animal[1] == 1:
            self.queue_dog.append(animal[0])

    def dequeueAny(self) -> List[int]:
        if not self.queue_cat and not self.queue_dog:
            return [-1, -1]
        elif not self.queue_cat:
            return [self.queue_dog.pop(0), 1]
        elif not self.queue_dog:
            return [self.queue_cat.pop(0), 0]
        else:
            c, d = self.queue_cat[0], self.queue_dog[0]
            if c < d:
                return [self.queue_cat.pop(0), 0]
            else:
                return [self.queue_dog.pop(0), 1]


    def dequeueDog(self) -> List[int]:
        if not self.queue_dog:
            return [-1, -1]
        return [self.queue_dog.pop(0), 1]

    def dequeueCat(self) -> List[int]:
        if not self.queue_cat:
            return [-1, -1]
        return [self.queue_cat.pop(0), 0]