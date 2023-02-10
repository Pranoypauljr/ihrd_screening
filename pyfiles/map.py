import gmplot

# GoogleMapPlotter return Map object
# Pass the center latitude and
# center longitude
gmap1 = gmplot.GoogleMapPlotter(43.466682433333304,
                                11.866801716666389, 13)
gmap1.marker(43.466682433333304, 11.866801716666389, color='cornflowerblue')

# Pass the absolute path
gmap1.draw(r'C:\Users\Tittu\Desktop\work\ihrd\pyfiles\hello.html')

