def max_num(num_1, num_2, num_3):
    max_numb=num_1
    if num_2 > max_numb:
        max_numb = num_2
    if num_3 > max_numb:
        max_numb = num_3
    return  max_numb

print(max_num(1, 2, 3))

print(max_num(89, 56, 40))

print(max_num(33, 78, 5))

def multi_list(list_1):
    result=1
    for i in list_1:
        result=result*i
    return result

print(multi_list(
    [3, 5, 2]
))

def rev_string(string):
    for i in range(len(string)-1, -1,-1):
        print(string[i],end='')
    print()

rev_string("car")

def num_within(num, start, end):
    within=False   # = means make equal to or set something to  
    for i in range(start, end):
        if num == i:   # == means is something equal to something else
            within=True
    return within

# display on this screen the results of calling the num_within function 
# num_within returns true or false
print(num_within(5,9,15))


def pascal(n):
  triangle = [[1],[1,1]]
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)