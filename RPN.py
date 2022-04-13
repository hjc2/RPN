
from operator import le
from turtle import st


rpn = "6 7 8 / -"
stack = []

for elem in rpn:
  if(elem != " "):
    if(elem == "+"):
      right = stack.pop()
      left = stack.pop()
      print(str(left) + " + " + str(right))
      stack.append(left + right)

    elif(elem == "-"):
      right = stack.pop()
      left = stack.pop()
      print(str(left) + " - " + str(right))
      stack.append(left - right)

    elif(elem == "/"):
      right = stack.pop()
      left = stack.pop()
      print(str(left) + " / " + str(right))
      stack.append(left / right)

    elif(elem == "*"):
      right = stack.pop()
      left = stack.pop()
      print(str(left) + " * " + str(right))
      stack.append(left * right)

    else:
      stack.append(float(elem))

print(stack)
