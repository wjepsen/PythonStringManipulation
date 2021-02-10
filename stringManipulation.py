highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(',')
# print(highlighted_poems_list)
highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  stripped_poem = poem.strip(' ')
  highlighted_poems_stripped.append(stripped_poem)

# print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  detail = poem.split(':')
  highlighted_poems_details.append(detail)
titles, poets, dates = [],[],[]
for section in highlighted_poems_details:
  titles.append(section[0])
  poets.append(section[1])
  dates.append(section[2])


for i in range(len(titles)): 
  poem_desc = "The poem {} was published by {} in {}".format(titles[i],poets[i],dates[i])
  print(poem_desc)









