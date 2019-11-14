
<div class="rendered-markdown"><h1>Programming Assignment 4</h1>
<p><strong>Fundamentals of Modern Software</strong>
<br  /><strong>Fall 2019</strong>
<br  /><strong>Due 11:59 PM, Wednesday, October 2</strong></p>
<h2>Introduction</h2>
<p>This assignment will give you practice writing programs to work with large datasets in a variety of file formats.</p>
<p><strong>REMINDERS</strong></p>
<ol>
<li><strong>When you are done, be sure to submit your work.</strong></li>
<li><strong>You must adhere to the collaboration policy in the syllabus. You MAY NOT copy the code of someone else in the class or allow someone else to copy your code.</strong></li>
<li><strong>Be sure to test your programs thoroughly. We will.</strong></li>
</ol>
<h2>babynames.py</h2>
<p>The Social Security Administration maintains an annual list of all new baby names. The lists are available for download from <a href="https://www.ssa.gov/oact/babynames/limits.html">https://www.ssa.gov/oact/babynames/limits.html</a>; we have given you the national year-by-year lists in the <code>babies</code> subdirectory. The file <code>NationalReadMe.pdf</code> in that directory documents the format used by the SSA. Write a program that identifies the 100 most commonly used male and female baby names from 1880 through 2016 (i.e, the names given to the most total babies).</p>
<p>Your program should save the names to an output JSON file, <code>popularnames.json</code>, which lists the top 100 names for each gender in descending order of popularity.  The file should be formatted to match the following (with different names and counts, of course):</p>
<pre><code>{"male": [{"name": "mario", "count": 500000}, {"name": "luigi", "count": 300000}, {"name": "wario", "count": 1}], "female": [ {"name": "peach", "count": 400000}, {"name": "toadette", "count": 250000}]
</code></pre>
<p><strong>To open a file in the <code>babies</code> subdirectory, add <code>babies/</code> to the start of the filename, e.g. <code>open(babies/yob1932.txt</code>).</strong></p>
<h2>flights.py</h2>
<p>We have given you a dataset of airports around the world in the file <code>airports.json</code>.  Write a program which takes as a command-line argument the IATA code for an airport (e.g. <code>EWR</code> for Newark Liberty International) and prints out a list of airports one can connect to from that airport, sorted in order of distance from nearest to farthest.</p>
<pre><code>$ python flights.py ITH
EWR Newark Liberty Intl 276km
PHL Philadelphia Intl 308km
DTW Detroit Metro Wayne Co 568km
</code></pre>
<p>To compute distances from one point to another on the surface of the Earth, you can use the <a href="https://geopy.readthedocs.io/en/stable/">geopy</a> Python package.   To compute the distance from a point with latitude <code>lat1</code> and longitude <code>long1</code> to a point with latitude <code>lat2</code> and longitude <code>long2</code>, first <code>$ from geopy import distance</code> and then use the expression <code>distance.distance([lat1,long1],[lat2,long2]).km</code>.  It takes two arguments, each of which is a list with two elements (the latitude and longitude of a point, measured in degrees, just as in <code>airports.json</code>) and returns a distance measured in kilometers.</p>
<p>(We have installed geopy in the Codio environment used for the assignment.  If you ever need to use it in a different Codio environment, run the command <code>$ pip install geopy</code> from the command line. You should only need to do this once.)</p>
</div>
