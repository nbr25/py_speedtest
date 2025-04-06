import speedtest,pprint

servers = []
# If you want to test against a specific server

threads = 2

s = speedtest.Speedtest(secure=True)
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()

results_dict = s.results.dict()
print("Download speed is :"+str(results_dict['download']))
