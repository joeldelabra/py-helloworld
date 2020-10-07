import matplotlib.pyplot as plt 

years = [1950, 1970, 1990, 2010]

population = [2.519, 3.692, 5.263, 6.972]

death = [515, 3.584,8.631,840]

plt.title('Poblacion Anual')

plt.xlabel('año')
plt.ylabel('Poblacion')

plt.plot(years, population,'b', years, death, 'g')
plt.scatter(years, population, color = 'red')
plt.plot(years,death,color = 'purple')
plt.scatter(years, death, color = 'g')
plt.legend(['crecimiento', 'muertes'])

plt.show()