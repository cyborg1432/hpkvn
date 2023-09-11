def kwarg_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Using the kwarg_function
kwarg_function(name="Alice", age=30, city="New York")


# #
# # def kwarg_fun(x,**kwargs):
# #
# #     print(x)
# #
# #     for key,value in kwargs.items():
# #         print(value)
# #
# # kwarg_fun("pp",name="Deepanshu")



#
# def kwarg_fun(**k):
#     print(k['name'])
#
# kwarg_fun(name="abc")
