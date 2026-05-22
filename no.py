




parent_val=''
left_child='exit()'
right_child=''

if parent_val=='+':
    print (float(left_child)+float(right_child))
if parent_val=='-':
    print (float(left_child)-float(right_child))
if parent_val=='*':
    print (float(left_child)*float(right_child))

print(eval(left_child+parent_val+right_child))

print('hello')