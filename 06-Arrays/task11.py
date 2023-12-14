months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']



def month():
    n = int(input('your month:'))
    return months[n-1]



print(month())