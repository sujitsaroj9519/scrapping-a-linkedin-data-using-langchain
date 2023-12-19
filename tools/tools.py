from langchain.serpapi import SerpAPIWrapper

def get_profile_url(text:str) ->str:
    ###Searching for linkedin of profile page ###
    search = SerpAPIWrapper()
    res = search.run(f'{text}')
    return res

