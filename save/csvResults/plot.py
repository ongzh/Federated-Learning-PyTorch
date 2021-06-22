import matplotlib
import matplotlib.pyplot as plt
import csv
matplotlib.use('Agg')


plt.figure()
plt.title('Test Accuracy vs Communication rounds')
plt.ylabel('Test Accuracy')
plt.xlabel('Communication Rounds')

E1B10=[]
E5B10 = []
E20B10 = []

E1B50 = []
E5B50 = []
E20B50 = []

E1B600 = []
E5B600 = []
E20B600 = [] 



with open ('mnist_cnn_200_C[0.1]_iid[1]_E[1]_B[10].csv','r') as datafile:
     ploting = csv.reader(datafile, delimiter=',')
     for ROWS in ploting:
         for COL in ROWS:
             E1B10.append(float(COL))
             
with open ('mnist_cnn_200_C[0.1]_iid[1]_E[1]_B[50].csv','r') as datafile:
     ploting = csv.reader(datafile, delimiter=',')
     for ROWS in ploting:
         for COL in ROWS:
             E1B50.append(float(COL))

with open ('mnist_cnn_200_C[0.1]_iid[1]_E[1]_B[600].csv','r') as datafile:
     ploting = csv.reader(datafile, delimiter=',')
     for ROWS in ploting:
         for COL in ROWS:
             E1B600.append(float(COL))
             
with open ('mnist_cnn_200_C[0.1]_iid[1]_E[5]_B[10].csv','r') as datafile:
     ploting = csv.reader(datafile, delimiter=',')
     for ROWS in ploting:
         for COL in ROWS:
             E5B10.append(float(COL))
             
with open ('mnist_cnn_200_C[0.1]_iid[1]_E[5]_B[50].csv','r') as datafile:
     ploting = csv.reader(datafile, delimiter=',')
     for ROWS in ploting:
         for COL in ROWS:
             E5B50.append(float(COL))

with open ('mnist_cnn_200_C[0.1]_iid[1]_E[5]_B[600].csv','r') as datafile:
     ploting = csv.reader(datafile, delimiter=',')
     for ROWS in ploting:
         for COL in ROWS:
             E5B600.append(float(COL))

with open ('mnist_cnn_200_C[0.1]_iid[1]_E[20]_B[10].csv','r') as datafile:
     ploting = csv.reader(datafile, delimiter=',')
     for ROWS in ploting:
         for COL in ROWS:
             E20B10.append(float(COL))

with open ('mnist_cnn_200_C[0.1]_iid[1]_E[20]_B[50].csv','r') as datafile:
     ploting = csv.reader(datafile, delimiter=',')
     for ROWS in ploting:
         for COL in ROWS:
             E20B50.append(float(COL))
             
with open ('mnist_cnn_200_C[0.1]_iid[1]_E[20]_B[600].csv','r') as datafile:
     ploting = csv.reader(datafile, delimiter=',')
     for ROWS in ploting:
         for COL in ROWS:
             E20B600.append(float(COL))
        
        
         

X = range(len(E1B10))

plt.ylim(0,1)
#plt.ylim(0.970,1)
plt.xlim(0,200)
plt.yticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])

plt.plot(X,E1B10, color='red')
plt.plot(X,E5B10, color = 'red', linestyle = 'dashed')
plt.plot(X,E20B10,color = 'red', linestyle = 'dashdot')
plt.plot(X,E1B50, color = 'orange')
plt.plot(X,E5B50, color = 'orange', linestyle = 'dashed')
plt.plot(X,E20B50, color = 'orange', linestyle = 'dashdot')
plt.plot(X,E1B600, color = 'blue')
plt.plot(X,E5B600, color = 'blue', linestyle = 'dashed')
plt.plot(X,E20B600, color = 'blue', linestyle = 'dashdot')

plt.legend(['B=10 E= 1','B=10 E= 5','B=10 E= 20', 'B=50 E= 1','B=50 E=5','B=50 E=20',
            'B=600 E= 1', 'B=600 E= 5','B=600 E= 20'])




plt.savefig('FedAvgtestAccVScomRounds.png')

#plt.savefig('FedAvgtestAccVScomRounds(small range).png')
