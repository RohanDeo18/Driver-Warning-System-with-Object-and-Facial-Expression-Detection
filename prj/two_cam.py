import matplotlib.pyplot as plt
'''
x = []
y = []
x.append(2)
y.append(1)
x.append(2)
y.append(2)
plt.figure(figsize=(6,4))
plt.plot(x,y,color="red",linewidth=1 )
plt.xlabel("time") 
plt.ylabel("TTC")
plt.title("TTC_map") 
plt.show()
'''
filename = 'static_fea_dis.txt'
frame_count_list=[]
frame_count=0
TTC_list=[]
with open(filename) as file_object:
    for line in file_object:
	    #print(line.rstrip())
        #if float(line.rstrip())>10 or float(line.rstrip())<0:
        #    continue
        TTC_list.append(float(line.rstrip()))
        frame_count+=1
        frame_count_list.append(frame_count)
plt.figure(figsize=(6,4))
plt.plot(frame_count_list,TTC_list,color="red",linewidth=1 )
plt.xlabel("Index") 
plt.ylabel("delta")
plt.title("static_map") 
plt.show()
