from pywebcopy import save_website
import sys
save_website(
url=sys.argv[1],
project_folder="savedpages/",
project_name="downloaded_site",
bypass_robots=True,
debug=True,
open_in_browser=True,
delay=None,
threaded=False,
)
