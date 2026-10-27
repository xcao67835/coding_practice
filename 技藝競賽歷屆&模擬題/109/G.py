while 1:
    try:
        songs=list(map(int,input().split()))
        t=songs.pop(0)
        n=songs.pop(0)
        dp=[0]*(t+1)
        for song in songs:
            for i in range(t,song-1,-1):
                if i-song>=0:
                    dp[i]=max(dp[i-song]+song, dp[i])
        print(dp[-1])
    except EOFError:
        break