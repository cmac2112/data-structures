import BinarySearch1

def main():
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    bst = BinarySearch1.BSTree()
    for num in nums:
        bst.insert(num)
    print(f"Min value in tree: {bst.get_min()}")
    print(f"Max value in tree: {bst.get_max()}")
    print('----')
    print(bst.search(11))
    print("preorder:")
    print(bst.preorder([]))
    print('----')

    print('postorder:')
    print(bst.postorder([]))
    print('----')

    print('inorder:')
    print(bst.inorder([]))
    print('----')

    nums = [2, 6, 20]
    print('deleting '+str(nums))
    for num in nums:
        bst.delete(num)
    print('----')

    print('4 exists:')
    print(bst.exists(4))
    print('2 exists:')
    print(bst.exists(2))
    print('12 exists:')
    print(bst.exists(12))
    print('18 exists:')
    print(bst.exists(18))

main()
