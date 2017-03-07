import meremedia
import fresh_tomatoes

the_notebook= meremedia.Movie("The Notebook", "A heart-throbing story of the difficulities a couple faces and how true love ultimately wins.", "http://www.impawards.com/2004/posters/notebook_ver2.jpg", "https://www.youtube.com/watch?v=4M7LIcH8C9U")
bridesmaids= meremedia.Movie("Bridesmaids", "A hilarious story of wedding planning gone wrong, a freidnship battle, and a wild bachelorette party", "http://www.impawards.com/2011/posters/bridesmaids.jpg", "https://www.youtube.com/watch?v=FNppLrmdyug")
the_devil_wears_prada= meremedia.Movie("The Devil Wears Prada", "The story of a aspiring writer,forced to write for a fashion magazine, opening the doors for her into the cut-throat fashion world","http://www.impawards.com/2006/posters/devil_wears_prada.jpg", "https://www.youtube.com/watch?v=LG0xYJJbko8" )
american_sniper= meremedia.Movie("American Sniper", "The story of an American Hero, the countless lives he saved, whom was tragically killed helping verterans that suffer from war related injuries and illnesses.", "http://www.limitedruns.com/media/cache/3f/57/3f57664c740c21156951dd304125c8ac.jpg","https://www.youtube.com/watch?v=99k3u9ay1gs")


movies=[the_notebook, bridesmaids, the_devil_wears_prada, american_sniper]
#fresh_tomatoes.open_movies_page(movies)
#print (meremedia.Movie.VALID_RATINGS)
print (meremedia.Movie.__doc__)

the_notebook.show_trailer()
bridesmaids.show_trailer()
