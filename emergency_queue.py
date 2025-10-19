class Patient:
    def __init__(self, name, urgency):
        self.name = name #patient
        self.urgency = urgency #level of urgency



class MinHeap:
    def __init__(self):
        self.data = [] #list of patient objects 
    
    def heapifyUp(self, index): #index is the urgency level, 0 being the most urgent
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency < self.data[parent].urgency: #comparing old patient with new patient, if new patient is more urgent then swaps them
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def heapifyDown(self, index): #function will be used after a patient is removed or being taken care of
        size = len(self.data)
        while index < size:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            #comparing patients and updating the order
            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right
            
            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    #core heap methods
    # 
    def insert(self, patient): #adds a new patient and calls heapify to restore order if needed
        self.data.append(patient)
        self.heapifyUp(len(self.data) - 1)    

    def printHeap(self):
        print("Current queue: ") 
        for patient in self.data:
            print(f"-Patient {patient.name} urgency ({patient.urgency})")

    def peek(self): #returns the most urgent patients
        return self.data[0] if self.data else None
    
    def removeMin(self): #removes the most urgent patient from the list, used when that patient has been taken care of
        if not self.data:
            return None
        minPatient = self.data[0]
        lastPatient = self.data.pop()
        if self.data:
            self.data[0] = lastPatient
            self.heapifyDown(0)
        return minPatient






# Test your MinHeap class here including edge cases

heap = MinHeap()
heap.insert(Patient("Alex", 3))
heap.insert(Patient("Ella", 1))
heap.insert(Patient("Guti", 5))
heap.printHeap()

next_up = heap.peek()
print("Next up:", next_up.name, next_up.urgency)

served = heap.removeMin()
print("Helped:", served.name)
heap.printHeap()
