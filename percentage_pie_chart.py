import matplotlib.pyplot as plt



#if you want to have the percentage calculated automatically, remember to make the commented code available again
imported_values = []


#Enter the values, 
#the first is the percentage of the number you want to show, 
#the second must be the remainder of the percentage 
#Example: [70, 30]
#You can add more than two numbers, perhaps to show more percentages
outer_sizes = [70, 30]

#Here you can enter the colors for the percentages, the last part must always be white
outer_colors = ['color-1', 'color-2', 'color-n', 'white']

sum = 0
'''                                                              
for size in imported_values:
    sum += size

for size in imported_values:
    outer_sizes.append((size/sum)*100)

'''

_, _, autopct = plt.pie(outer_sizes,colors=outer_colors, startangle=90,frame=True, radius=4 , counterclock=False, autopct='%1.0f%%', pctdistance=0.3, textprops={'size': 13, 'fontweight': "bold"})


#Makes the percentage of the white part invisible
for txt, c in zip(autopct, outer_colors):
    if c == "white":
        txt.set_visible(False)



center_circle = plt.Circle((0,0), 2, color='black', fc='white', linewidth=0)

#It removes the inner part, but only for aesthetic purposes
plt.gca().add_artist(center_circle)

plt.gcf()
plt.axis('equal')
plt.tight_layout()
plt.show()