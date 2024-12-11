class List (list):
    def min(self):
        return min(self)

    def max(self):
        return max(self)



def main():
    temp_list = List([1, 2, 3, 4, 5])
    temp_list_2 = List()
    temp_list_2.append(1)
    temp_list_2.append(2)
    print("Minimal value of the first list:", temp_list.min())
    print("Maximum value of the first list:", temp_list.max())
    print("Minimal value of the second list:", temp_list_2.min())

if __name__ == '__main__':
    main()