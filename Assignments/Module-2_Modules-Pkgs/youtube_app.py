from pytubefix import YouTube


url="https://www.youtube.com/watch?v=HV6RakCs2dc&list=RDHV6RakCs2dc&start_radio=1"

YouTube(url).streams.first().download()