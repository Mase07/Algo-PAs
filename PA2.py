# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 13:42:29 2024

@author: MGWhite
"""
import random
import time

SECONDS_PER_ITEM = 4
BASE_CHECKOUT_TIME = 45
TOTAL_TEST_TIME = 7200
DATA_INTERVAL = 50

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Register():
    def __init__(self, is_express = False):
        self.is_express = is_express
        self.queue = Queue()
        self.total_customers = 0
        self.total_items = 0
        self.total_idle = 0
        self.total_wait = 0
        self.current_customer_end_time = None
        self.idle_start = 0
        
    def add_customer(self, customer, current_time):
        is_idle = self.busy()
        customer_enqueued = current_time
        self.queue.enqueue(customer)
        
        if is_idle():
            self.current_customer_end_time = current_time + customer.checkout_time()
            if self.idle_start is not None:
                self.total_idle_time += current_time - self.idle_start
                self.idle_start = None
                             
    def next_customer(self, current_time):
        if self.busy():
            customer = self.queue.dequeue()
            self.total_customer += 1
            self.total_items += customer.items
            self.total_wait += (current_time - customer.enqueue_time)
            
            if not self.busy():
                self.idle_start = current_time
            else:
                next_customer = self.queue.items[0]
                self.current_customer_end_time = current_time + next_customer.checkout_time()
                
    def busy(self):
        return not self.queue.isEmpty()
    
    def queue_length(self) :
        return self.queue.size()
    
    def wait_time(self):
        wait_time = 0
        for customer in self.queue.items:
            wait_time += customer.checkout_time()
        return wait_time
            
   
class Customer():
    def __init__(self):
        self.items = random.randint(6,20)
        self.enqueueu_time = None
        
    def items(self):
        return self.items
    
    def checkout_time(self) :
        return self.items * SECONDS_PER_ITEM + BASE_CHECKOUT_TIME
    
    
def choose_register(customer, registers):
    best_register = None
    minimum_wait = registers[0].wait_time()
    
    for register in registers:
        wait_time = register.wait_time()
        if wait_time < minimum_wait:
            minimum_wait = wait_time
            best_register = register
    return best_register

def simulation(registers):
    current_sim_time = 0
    next_customer_time = current_sim_time + 30
    
    while current_sim_time < TOTAL_TEST_TIME:
        if current_sim_time >= next_customer_time:
            new_customer = Customer()
            chosen_register = choose_register(new_customer, registers)
            chosen_register.add_customer(new_customer, current_sim_time)
            next_customer_time = current_sim_time + 30
        for register in registers:
            if register.busy(): 
                register.next_customer(current_sim_time)
