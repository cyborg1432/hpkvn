x = [10,9,6,7,6]

def exe():

    print(x)

    try:

        for i in range(0, len(x)):

            if (x[i] <= x[i + 1]):
                pass
            else:
                temp_element = x[i]
                x.remove(x[i])
                x.append(temp_element)
                exe()


    except Exception as e:
        pass



exe()

print(x)
