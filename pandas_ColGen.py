import pandas as pd
try:
    df = pd.read_csv("C:\\Users\\donep\\OneDrive\\Desktop\\TASK_DAILY\\source\\surplus.csv")
    df['BONUS'] = [5000 if x <= 30000 else 0 for x in df['salary']]
    print(df)
except FileNotFoundError:
    print ("No such file or directory: 'C:\\Users\\donep\\OneDrive\\Desktop\\TASK_DAILY\\surplus.csv'")
except TypeError:
    print("'<=' not supported between instances of 'str' and 'int'")  
except Exception as e:
    print(e)
else:
    print("*******succesfull********")  
finally:
    print("execution completed..")