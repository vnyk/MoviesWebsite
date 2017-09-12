import roasted_tomatoes
import media

gangs=media.Movie("Gangs of Waseypur","life of a gangster","https://photos.filmibeat.com/ph-big/2012/07/gangs-of-wasseypur-2-poster_13419789820.jpg","https://www.youtube.com/watch?v=j-AkWDkXcMY")
mip=media.Movie("Midnight in Paris","i havent seen yet","https://images-na.ssl-images-amazon.com/images/I/81QO%2BfaevoL._SY445_.jpg","https://www.youtube.com/watch?v=BYRWfS2s2v4")

pursuit=media.Movie("Pursuit of Happiness","life of a struggling person","http://myworldtoyou.com/wp-content/uploads/The-pursuit-of-happiness.jpg","https://www.youtube.com/watch?v=89Kq8SDyvfg")

mov=[gangs,mip,pursuit]
#print(gangs.storyline)
roasted_tomatoes.open_movies_page(mov)
