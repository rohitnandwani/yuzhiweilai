import twitter


twitterApi = twitter.Api(consumer_key='BeJvMbvBdYoptsvMiTxCg', consumer_secret='Ny6nzkkPh3IIR56fY2jrBpqBjR547nBnxEeohDRlVo', access_token_key='306720614-JnMHe5U5XHGjlQ33IHkrsUcfmOFUChlHa2Jqtbgd', access_token_secret='eD7HxdD9u6zR0voZyvY5hiLGi9Kv6SoWplhV9w0tuXojE')


#def fetchUserTimeline(screenName): 
   # statuses = twitterApi.GetUserTimeline(screen_name=screenName)
   # return statuses


results_Sony = twitterApi.GetSearch(
    raw_query="q=Sony%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Sony


results_Beats = twitterApi.GetSearch(
    raw_query="q=Beats%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Beats


results_Bose = twitterApi.GetSearch(
    raw_query="q=Bose%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Bose


results_AKG = twitterApi.GetSearch(
    raw_query="q=AKG%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_AKG


results_Apple = twitterApi.GetSearch(
    raw_query="q=Apple%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Apple


results_AudioTechnica = twitterApi.GetSearch(
    raw_query="q=AudioTechnica%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_AudioTechnica


results_Beyerdynamic = twitterApi.GetSearch(
    raw_query="q=Beyerdynamic%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Beyerdynamic


results_Brainwavz = twitterApi.GetSearch(
    raw_query="q=Brainwavz%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Brainwavz


results_Creative = twitterApi.GetSearch(
    raw_query="q=Creative%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Creative


results_Grado = twitterApi.GetSearch(
    raw_query="q=Grado%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Grado


results_HarmanKardon = twitterApi.GetSearch(
    raw_query="q=Harman%20Kardon%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_HarmanKardon


results_JBL = twitterApi.GetSearch(
    raw_query="q=JBL%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_JBL


results_JLab = twitterApi.GetSearch(
    raw_query="q=JLab%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_JLab


results_JVC = twitterApi.GetSearch(
    raw_query="q=JVC%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_JVC


results_Klipsch = twitterApi.GetSearch(
    raw_query="q=Klipsch%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Klipsch


results_KOSS = twitterApi.GetSearch(
    raw_query="q=KOSS%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_KOSS


results_Logitech = twitterApi.GetSearch(
    raw_query="q=Logitech%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Logitech


results_MEEAudio = twitterApi.GetSearch(
    raw_query="q=MEE%20Audio%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_MEEAudio


results_Monster = twitterApi.GetSearch(
    raw_query="q=Monster%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Monster


results_Panasonic = twitterApi.GetSearch(
    raw_query="q=Panasonic%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Panasonic


results_Philips = twitterApi.GetSearch(
    raw_query="q=Philips%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Philips


results_Pioneer = twitterApi.GetSearch(
    raw_query="q=Pioneer%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Pioneer


results_Plantronics = twitterApi.GetSearch(
    raw_query="q=Plantronics%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Plantronics


results_Sennheiser = twitterApi.GetSearch(
    raw_query="q=Sennheiser%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Sennheiser


results_Shure = twitterApi.GetSearch(
    raw_query="q=Shure%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Shure


results_Skullcandy = twitterApi.GetSearch(
    raw_query="q=Skullcandy%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Skullcandy


results_SoundPeats = twitterApi.GetSearch(
    raw_query="q=SoundPeats%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_SoundPeats


results_VModa = twitterApi.GetSearch(
    raw_query="q=V-Moda%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_VModa


results_Westone = twitterApi.GetSearch(
    raw_query="q=Westone%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Westone


results_Xiaomi = twitterApi.GetSearch(
    raw_query="q=Xiaomi%20headphone%20&result_type=recent&since=2013-11-01&count=200")
results_Xiaomi


# Earphone

results_earphone_Sony = twitterApi.GetSearch(
    raw_query="q=Sony%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Sony


results_earphone_Beats = twitterApi.GetSearch(
    raw_query="q=Beats%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Beats


results_earphone_Bose = twitterApi.GetSearch(
    raw_query="q=Bose%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Bose


results_earphone_AKG = twitterApi.GetSearch(
    raw_query="q=AKG%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_AKG


results_earphone_Apple = twitterApi.GetSearch(
    raw_query="q=Apple%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Apple


results_earphone_AudioTechnica = twitterApi.GetSearch(
    raw_query="q=AudioTechnica%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_AudioTechnica


results_earphone_Beyerdynamic = twitterApi.GetSearch(
    raw_query="q=Beyerdynamic%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Beyerdynamic


results_earphone_Brainwavz = twitterApi.GetSearch(
    raw_query="q=Brainwavz%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Brainwavz


results_earphone_Creative = twitterApi.GetSearch(
    raw_query="q=Creative%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Creative


results_earphone_Grado = twitterApi.GetSearch(
    raw_query="q=Grado%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Grado


results_earphone_HarmanKardon = twitterApi.GetSearch(
    raw_query="q=Harman%20Kardon%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_HarmanKardon


results_earphone_JBL = twitterApi.GetSearch(
    raw_query="q=JBL%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_JBL


results_earphone_JLab = twitterApi.GetSearch(
    raw_query="q=JLab%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_JLab


results_earphone_JVC = twitterApi.GetSearch(
    raw_query="q=JVC%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_JVC


results_earphone_Klipsch = twitterApi.GetSearch(
    raw_query="q=Klipsch%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Klipsch


results_earphone_KOSS = twitterApi.GetSearch(
    raw_query="q=KOSS%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_KOSS


results_earphone_Logitech = twitterApi.GetSearch(
    raw_query="q=Logitech%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Logitech


results_earphone_MEEAudio = twitterApi.GetSearch(
    raw_query="q=MEE%20Audio%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_MEEAudio


results_earphone_Monster = twitterApi.GetSearch(
    raw_query="q=Monster%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Monster


results_earphone_Panasonic = twitterApi.GetSearch(
    raw_query="q=Panasonic%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Panasonic


results_earphone_Philips = twitterApi.GetSearch(
    raw_query="q=Philips%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Philips


results_earphone_Pioneer = twitterApi.GetSearch(
    raw_query="q=Pioneer%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Pioneer


results_earphone_Plantronics = twitterApi.GetSearch(
    raw_query="q=Plantronics%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Plantronics


results_earphone_Sennheiser = twitterApi.GetSearch(
    raw_query="q=Sennheiser%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Sennheiser


results_earphone_Shure = twitterApi.GetSearch(
    raw_query="q=Shure%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Shure


results_earphone_Skullcandy = twitterApi.GetSearch(
    raw_query="q=Skullcandy%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Skullcandy


results_earphone_SoundPeats = twitterApi.GetSearch(
    raw_query="q=SoundPeats%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_SoundPeats


results_earphone_VModa = twitterApi.GetSearch(
    raw_query="q=V-Moda%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_VModa


results_earphone_Westone = twitterApi.GetSearch(
    raw_query="q=Westone%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Westone


results_earphone_Xiaomi = twitterApi.GetSearch(
    raw_query="q=Xiaomi%20earphone%20&result_type=recent&since=2013-11-01&count=200")
results_earphone_Xiaomi







