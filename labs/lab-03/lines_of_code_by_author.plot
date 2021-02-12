set terminal png transparent size 640,240
set size 1.0,1.0

set terminal png transparent size 640,480
set output 'lines_of_code_by_author.png'
set key left top
set yrange [0:]
set xdata time
set timefmt "%s"
set format x "%Y-%m-%d"
set grid y
set ylabel "Lines"
set xtics rotate
set bmargin 6
plot 'lines_of_code_by_author.dat' using 1:2 title "Justin Gaskins" w lines, 'lines_of_code_by_author.dat' using 1:3 title "Hannah Lim" w lines, 'lines_of_code_by_author.dat' using 1:4 title "gwild37" w lines, 'lines_of_code_by_author.dat' using 1:5 title "Gabriel Wild" w lines, 'lines_of_code_by_author.dat' using 1:6 title "Samuel Obe" w lines, 'lines_of_code_by_author.dat' using 1:7 title "Christopher Pence" w lines, 'lines_of_code_by_author.dat' using 1:8 title "saprap1" w lines, 'lines_of_code_by_author.dat' using 1:9 title "Unachieved" w lines, 'lines_of_code_by_author.dat' using 1:10 title "dependabot[bot]" w lines, 'lines_of_code_by_author.dat' using 1:11 title "Unknown" w lines, 'lines_of_code_by_author.dat' using 1:12 title "samuelobe" w lines, 'lines_of_code_by_author.dat' using 1:13 title "gaskij" w lines, 'lines_of_code_by_author.dat' using 1:14 title "crtp05" w lines, 'lines_of_code_by_author.dat' using 1:15 title "Kristina Adams" w lines, 'lines_of_code_by_author.dat' using 1:16 title "Justin Mai" w lines, 'lines_of_code_by_author.dat' using 1:17 title "Glitch (rpicampusmap)" w lines, 'lines_of_code_by_author.dat' using 1:18 title "Glitch (gaskij-rpicampusmap)" w lines, 'lines_of_code_by_author.dat' using 1:19 title "Carl Stadtler" w lines
