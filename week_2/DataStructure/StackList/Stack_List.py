import Stack_List_BL as SLL_ob

# --------------------------------------------------\
st = SLL_ob.stack_list()
print('Befor add in stack anagram numbers are : ')
for i in range(len(SLL_ob.anagram_list)):
    print(SLL_ob.anagram_list[i], end=' ')

for i in range(len(SLL_ob.anagram_list)):
    st.push(SLL_ob.anagram_list[i])

print('\n\nAfter add in stack we are removing from stack : ')
# st.display()
while st.size() > 0:
    print(st.peek(), end=' ')
    st.pop()
print()
# ---------------------------------------------------
