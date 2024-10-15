from random import choice,randint
from api import *
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered == '!airing':
        titles = get_anime_titles_airing()
        if titles:
            titles_text = '\n'.join(titles)
            return f"```Airing Animes (Limit 20):\n{titles_text}```"
        return 'Algo errado '
    elif '!help' in lowered:
        return '```HELP: \n Command: !Airing - Top 20 Airing Anime \n Command: !Upcoming - Top 20 Upcoming Anime```'
    
    elif '!upcoming' in lowered:
        titles = get_anime_titles_upcoming()
        if titles:
            titles_text = '\n'.join(titles)
            return f"```Upcoming Animes (Limit 20):\n{titles_text}```"
    else:
        return choice(['I do not understand','What are you talking about?'])

