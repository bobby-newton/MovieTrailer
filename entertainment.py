import main
import media

# create movie instances to render on the webpage
i_am_legend = media.Movie("I Am Legend (2007)",
                          "An American post-apocalyptic action horror film",
                          "http://www.mafab.hu/static/2014/265/14869_34.jpg",
                          "https://www.youtube.com/watch?v=dtKMEAXyPkg")

full_metal_jacket = media.Movie("Full Metal Jacket (1987)",
                                "a 1987 British-American war film",
                                "https://encrypted-tbn0.gstatic.com/images?" +
                                "q=tbn:ANd9GcRpkczjxhVWtPE9jsy" +
                                "_fTUjxw5zgwFTWywOjWnXtzaZduU3is0x8w",
                                "https://www.youtube.com/watch?v=x9f6JaaX7Wg")

batman_vs_superman = media.Movie("Batman vs Superman (2016)",
                                 "Batman takes on the man of steel(Superman)",
                                 "https://encrypted-tbn0.gstatic.com/images?" +
                                 "q=tbn:ANd9GcQNVSqr-oewd2jSNUp1d7BZDJVf6PvZ" +
                                 "9L22K7tzniVytBU4Zfgn7Q",
                                 "https://www.youtube.com/watch?v=0WWzgGyAH6Y")

warrior = media.Movie("Warrior (2011)",
                      "Two brothers reunite",
                      "https://encrypted-tbn0.gstatic.com/images?" +
                      "q=tbn:ANd9GcSSgn4CUt3IpvYbYr8QTP65q9zzfsd" +
                      "_siIraIHsfeGcfs3MUE6v",
                      "https://www.youtube.com/watch?v=I5kzcwcQA1Q")

tmnt = media.Movie("Teenage Mutant Ninja Turtles (2014)",
                   "From their home in sewers of New York City, " +
                   "they battle petty criminals",
                   "https://encrypted-tbn0.gstatic.com/images?" +
                   "q=tbn:ANd9GcQvFX6IxeytOndA5-" +
                   "fxSBSSD3g8AUWT5naUD2U1V7rnReao6xcXFg",
                   "https://www.youtube.com/watch?v=VZZ0PnDZdZk")

thor = media.Movie("Thor (2011)",
                   "The story of the hammer-wielding Nordic god Thor",
                   "https://images-na.ssl-images-amazon.com/images/M/" +
                   "MV5BOGE4NzU1YTAtNzA3Mi00ZTA2LTg2YmYtMDJmMThiMjlkY" +
                   "jg2XkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_UX182_CR0,0,182," +
                   "268_AL_.jpg",
                   "https://www.youtube.com/watch?v=JOddp-nlNvQ")

# pass movie instances as a list to python class main
movies = [i_am_legend, full_metal_jacket, batman_vs_superman, warrior, tmnt,
          thor]
main.open_movies_page(movies)
