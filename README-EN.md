# EnEx
## A Path Travesal Game with Wikipedia Winks

[auch auf deutsch erhältlich](README.md)

<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

- [What is EnEx](#what-is-EnEx)
- [How to Play/Gamerules](#how-to-playgamerules)
   * [UI Explanation](#ui-explanation)
- [How to Install](#how-to-install)
- [lorem ipsum for good measure](#lorem-ipsum-for-good-measure)

<!-- TOC end -->

<!-- TOC --><a name="what-is-EnEx"></a>
## What is EnEx
EnEx is a game in which you are given a start Wikipedia page and need to find a way to get to another given Wikipedia page only using the links on the page itself with the least possible steps. 

Because this game was made as a school project, it only features the German language for both the game and Wikipedia - feel free to fork and translate it. 

<!-- TOC --><a name="how-to-playgamerules"></a>
## How to Play/Gamerules
Depending on the game rules you selected prior to playing, you either start with a random or a specific Wikipedia page and need to find the shortest path to the either randomly or manually chosen target page. You do this by clicking links on pages until you find the target page or, if enabled, the time is up. If you ever want to go back, EnEx includes a path tree of pages you have discoverd and the distance from the start to said page. Once you found a path EnEx will give you a score based on the amount of steps your (shortest) solution has and the time you took to find it. It will also show *one* ¹ ideal solution as an example. 


¹ Because of how closely Wikipedia is linked, it is possible and not uncommon for multiple optimal solutions to exist. To save time and resources, EnEx will only show the one it found first; you can use pages like [Six Degrees of Wikipedia](https://www.sixdegreesofwikipedia.com) to view different solutions (just don't use it to cheat ;3). 

<!-- TOC --><a name="ui-explanation"></a>
### UI Explanation
On the left is the menu, and on the right is the web viewer where the Wikipedia pages are displayed.

<!-- TOC --><a name="how-to-install"></a>
## How to Install
Please ensure that the following packages are installed (e.g., using pip):
- pywebview
- PyQt5
- dotenv
- requests
- screeninfo

Afterwards, please execute the file [gui.py](src/gui.py). Further instructions can be found in the windows that open.

<!-- TOC --><a name="lorem-ipsum-for-good-measure"></a>
## lorem ipsum for good measure


Quia debitis ut autem non consequatur aut doloribus. Fugit et accusantium veniam qui voluptas ut suscipit. Natus fugiat pariatur in vel. Doloribus est sed dolor accusantium. Consectetur consequatur tenetur itaque ut.

Commodi optio reprehenderit labore. Eius fugiat cum occaecati earum laudantium amet esse. Necessitatibus ratione fugiat et ratione dicta quia tenetur. Sint error ut eaque officiis qui perferendis officia aut.

Qui omnis omnis sed voluptatem. Necessitatibus maiores dicta officia possimus eos est officiis. Nihil sint harum ad repellendus id.

Non dolorum consequatur ipsam. Modi fugit praesentium ad dolor est. Voluptate ipsam accusantium quo dolor iusto consequatur. Laborum rerum nesciunt eum iure. Perferendis dolores et perferendis consequuntur.

Vero placeat repellendus in perspiciatis accusamus eum laudantium. Doloremque facilis architecto quis iusto et sunt officia totam. Dolores ea dolorem atque. Pariatur eveniet enim quia nisi at quaerat pariatur quasi.
