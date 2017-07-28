# -*- coding: utf-8 -*-
import timeit
def timed(method):
    def timer(*args, **kwargs):
        ts     = timeit.default_timer()
        result = method(*args, **kwargs)
        te     = timeit.default_timer()
        print '%r, %2.10f sec' % (method.__name__, te-ts)
        return result
    return timer
    
class Sorting(object):
    
    @timed
    def selectionSort(self, a):
        for i in range(len(a)):
            min = i
            for j in range(i+1, len(a)):
                if a[j] < a[min]:
                    min = j
            a[i], a[min] = a[min], a[i]
        return a
    
    @timed
    def insertionSort(self, a):
        for i in xrange(len(a)):
            for j in xrange(i, 0, -1):
                if a[j] < a[j-1]:
                    a[j], a[j-1] = a[j-1], a[j]
                else: break
        return a
    
    def merge(self, left, right):
        i, j, res, m, n = 0, 0, [], len(left), len(right) 
        while i< m and j<n:
            if left[i]<right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        res += (left[i:] + right[j:])
        return res
    
    def mergeSort(self, a):
        k = len(a)
        if k==1: return a
        m = k/2
        return self.merge(self.mergeSort(a[:m]), self.mergeSort(a[m:]))
    
    def mergeSort2(self, a):
        k = len(a)
        if k < 2: return a
        half = k // 2
        left = self.mergeSort2(a[:half])
        right = self.mergeSort2(a[half:])
        out =[]
        li, ri, m, n = 0, 0, len(left), len(right)
        while li<m and ri<n:
            if left[li] < right[ri]:
                out.append(left[li])
                li += 1
            else:
                out.append(right[li])
                ri += 1
        out += (left[li:] + right[ri:])
        return out
    
    def quickSort(self, a):
        if not a: return a
        pivot = a[random.choice(range(len(a)))]
        head = self.quickSort([i for i in a if i < pivot])
        tail = self.quickSort([i for i in a if i > pivot])
        return head + [i for i in a if i==pivot] + tail
    
    
    def quickSort2(self, a, first, last):
        if first>=last: return
        
        i, j = first, last
        pivot = a[random.randint(first, last)]
        
        while i<=j:
            while a[i]<pivot:
                i+=1
            while a[j]>pivot:
                j-=1
            if i<=j:
                a[i], a[j] = a[j], a[i]
                i, j = i+1, j-1
        self.quickSort2(a, first, j)
        self.quickSort2(a, i, last)
    
        

s = Sorting()
import random
a = range(100000)
random.shuffle(a)

#s.selectionSort(a)
#s.insertionSort(a)
st = timeit.default_timer()
s.mergeSort(a)
print timeit.default_timer()-st
st = timeit.default_timer()
s.mergeSort2(a)
print timeit.default_timer()-st
st = timeit.default_timer()
s.quickSort(a)
print timeit.default_timer()-st
st = timeit.default_timer()
s.quickSort2(a, 0, len(a)-1)
print timeit.default_timer()-st