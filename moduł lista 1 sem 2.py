import random
import math


class Vector():
    def __init__(self, size=3):
        """Konstruktor przyjmujący rozmiar wektora jako argument.
            Tworzę wektor(liste) o długości 3."""
        self.size = size
        self.values=[0]*size
    
    def random_generation(self):
        """Metoda do losowej generacji elementów wektora. 
            Losuje za pomocą funkcji random wartości i dodaje je do wektora(listy)."""
        self.values = []
        for i in range(self.size):
            self.values.append(random.randint(-10,10))
        return self.values
    
    def set_values_from_list(self, list1):
        """Metoda do wczytywania elementów wektora z listy podanej jako argument.
            Długość tej listy musi być taka sama jak długość wektora, podstawiam tę listę za wektor."""
        self.size = len(list1)
        self.values = list1
        return self.values
    
    def __add__(self, other):
        """Operator dodawania dwóch wektorów.
            Sprawdzam czy mają taki sam rozmiar, jeśli tak to dodaje element z wektora pierwszego z tym samym 
            elementem z wektora drugiego itd, jeśli nie to wypisuję błąd."""
        vectorsum = []
        if self.size == other.size:
            for i in range (self.size):
                vectorsum.append(self.values[i] + other.values[i])
            return vectorsum
        else: 
            raise ValueError("Vectors size is not the same")
            
    def __sub__(self, other):
        """Operator odejmowania dwóch wektorów.
            Sprawdzam czy mają taki sam rozmiar, jeśli tak to odejmuje element z wektora drugiego od tego samyego
            elementu z wektora pierwszego itd, jeśli nie to wypisuję błąd."""
        vectorsub = []
        if self.size == other.size:
            for i in range (self.size):
                vectorsub.append(self.values[i] - other.values[i])
            return vectorsub
        else: 
            raise ValueError("Vectors size is not the same")
            
    def __mul__(self, scalar):
        """Mnożenie wektora przez skalar.
            Mnożę po kolei wszystkie elemnty z wektora przez skalar."""
        scalarvector = []
        for i in range(self.size):
            scalarvector.append(self.values[i]*scalar)
        return scalarvector
    
    def vector_len(self):
        """Metoda wyliczająca długość wektora.
            Podnoszę do kwadratu po kolei wszystkie elementy wektora, sumując kwadraty tych elementów, a na koniec 
            biorę pierwiastek z tej sumy."""
        vectorlen = 0 
        for i in range(self.size):
            vectorlen = vectorlen + self.values[i]**2
        return math.sqrt(vectorlen)
    
    def vector_values_sum(self):
        """Metoda wyliczająca sumę elementów wektora.
            Biorę po kolei wartości wektora i sumuje je w zmiennej vectorvaluessum."""
        vectorvaluessum = 0
        for i in range(self.size):
            vectorvaluessum = vectorvaluessum + self.values[i]
        return vectorvaluessum
    
    def scalar_product(self, other):
        """Metoda wyliczającą iloczyn skalarny dwóch wektorów.
            Jeśli rozmiar wektora pierwszego jest taki sam jak rozmiar wektora drugiego, to po kolei mnożę te same elemnty wektorów
            i sumuje je w scalarproduct, jeśli nie to wypisuję błąd."""
        scalarproduct = 0
        if self.size == other.size:
            for i in range(self.size):
                scalarproduct += self.values[i]*other.values[i]
            return scalarproduct
        else: 
            raise ValueError("Vectors size is not the same")
            
    def __str__(self):
        """Reprezentacja tekstowa wektora"""
        return str(self.values)

    def __repr__(self):
        """Reprezentacja tekstowa wektora"""
        return print(self.values)
    
    def __getitem__(self, position):
        """Operator [] pozwalający na dostęp do konkretnych elementów wektora
            Sprawdzam czy pozycja jest większa od zera i czy nie jest większa od rozmiaru wektora, jeśli tak to
            za pomocą operatora [] wypisuje wartość jaka znajduje się pod tą pozycją, jeśli nie wypisuję błąd."""
        if position>0 and position <= self.size:
            return self.values[position-1]
        else: 
            raise ValueError("Improper value")
            
    def __contains__(self, element):
        """Operator in sprawdzający przynależność elementu do wektora.
            Sprawdzam za pomocą operatora in czy jest taka wartość w wektorze(na liście)"""
        if element in self.values:
            return "Tak"
        else: 
            return "Nie"