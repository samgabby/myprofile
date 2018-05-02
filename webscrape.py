#ctrl shift p to open command console
#set syntax = python




from urllib.request import urlopen as uOpen
from bs4 import BeautifulSoup as soup





#get the url you want to use
my_url = 'https://www.amazon.co.uk/s/ref=nb_sb_noss_1/262-5127199-8693620?url=search-alias%3Daps&field-keywords=apple+juice'



#grab the webpage using the urlopen function, create a file variable and put the contents there
uFile = uOpen(my_url)



#create a text variable and read the html page into it
html_page = uFile.read()


#close the connection
uFile.close()



#using the beautiful soup function, parse the html page and pass it into a variable
#with the 'html.parser' argument, you tell the function how to parse the html page
parsed_page = soup(html_page, 'html.parser')



#test
#print(parsed_page.h1)
#print(parsed_page.p)





#now its time to traverse the html and convert desired items into a csv file

#use the findAll method to grab all the html elements you want and put them in a list

#syntax is list = parsed_page.findAll('htmlelement', {'attributename':'attributevalue'})

containers = parsed_page.findAll('div', {'class':"a-fixed-left-grid-col a-col-right"})




#test
#print(len(containers))
#print(len(name_containers))
#print(len(price_containers))






#view the below on jsbeautifier.org
#print(containers[0])






#bfore you build your loop prototype your loop to check it works once
#name_container = name_containers[0]
#price_container = price_containers[0]
#print(name_container)
#print(price_container)





#note
#to grab text from a html element, syntax is print(name_container.div.a.h2.text)
#to grab an attribute from a html element, syntax is print(name_container.div.a.h2['attribute'])




filename = 'products.csv'

f = open(filename, 'w') #f is the python convention

headers = 'product_name, price\n' #create header to be written to file, remember that csv's are comma delimited

f.write(headers)





for i in containers:

	product_name = i.div.div.a.h2.text

	price_container = i.findAll('span', {'class':'a-size-base a-color-price s-price a-text-bold'})
	price = price_container[0].text


	print(product_name)
	print(price)

	#write to file, remember that csv's are comma delimited
	f.write(product_name.replace(',', '|') + ',' +price)
	f.write('\n')




f.close()