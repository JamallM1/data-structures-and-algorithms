from data_structures.queue import Queue

# Defining breadth_first function and passing in the tree as an argument
# Declaring search variable to equal the queue function
# Setting tree value to an empty list
def breadth_first(tree):
    search = Queue()
    tree_val = []
# if statement saying if not tree return tree_val and tree_val is == empty list
    if not tree:
        return tree_val
# if not the start of the tree return list or tree_val
    if not tree.root:
        return tree_val
# predifined in my queue module search is == to queue function. If not in front of the queue add to the back of the queue
    if not search.front:
        search.enqueue(tree.root)
# traversing left than right
    while search.front:
        root = search.dequeue()
        tree_val.append(root.value)
        if root.left:
            search.enqueue(root.left)
        if root.right:
            search.enqueue(root.right)
# Returning tree
    return (tree_val)

