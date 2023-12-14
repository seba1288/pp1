movie_titles = ['IndianaJones1','Buzz Astral','Toy story','Toy story 2','Toy story 3']
f = open('movies.txt','w')

for i in movie_titles:
    f.write(i+'\n')

f = open('movies.txt','r')
print(f.read())
f.close()