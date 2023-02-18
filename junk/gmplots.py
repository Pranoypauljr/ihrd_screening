import gmplot
gmap1 = gmplot.GoogleMapPlotter(43.466682433333304,
                                11.866801716666389, 13)
gmap1.marker(43.466682433333304, 11.866801716666389, color='cornflowerblue')
gmap1.draw("./xyz.html")