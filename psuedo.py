# Create and sort a list of Foodstuff objects based on length * depth

"""
# Logic for v1:
dict = {} # this will be filled with stacks with the key as the number stack on that shelf

For shelf in pantry
    While sum(dict.values) < shelf.width
         find item in dict.values where item <= shelf.height - item.height
                rearrange_stack(dict[stack_index], item)
"""

"""
rearrange_stack(stack, newItem) -> stack:
        temp = [newItem]
        while !stack.isEmpty:
                temp.append(stack.pop)
        sort temp by base-size (by width)
        for item in sorted_temp
                stack.push(item)
        return stack
"""

"""
# Testable output example:
>> Pantry(2)
>> Shelf(36, 8)
>> Shelf(36, 8)
>> Shelf(36, 8)
>> Items = [...Foodstuffs]

Valid Output:
        [4, 3]  [3,2]
[9,7]   [5, 1]  [3,2]
[10,3]  [9, 4]  [3,3]
# where l[0] = width, l[1] = height
"""