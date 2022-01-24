# def switch(num):
#     dict = {
#         1: 'Sunday',
#         2: 'Monday',
#         3: 'Tuesday',
#         4: 'Wednesday',
#         5: 'Thursday',
#         6: 'Friday',
#         7: 'Saturday'
#     }
#     return dict.get(num, 'Invalid Day')
#
#
# num = 5
# print(' The number is:', num, 'and the day is:', switch(num))


def switch(cert):
    dict = {
        "U": 'Suitable for all ages',
        "PG": 'Parental Guidance',
        "12": '12 and over',
        "12A": '12 and over unless with an adult',
        "15": '15 and over',
        "18": '18 and over'
    }
    return dict.get(cert, 'Invalid Certificate')


cert = "12"
print('Current movie has:', cert.upper(), 'certificate, which means -', switch(cert))
