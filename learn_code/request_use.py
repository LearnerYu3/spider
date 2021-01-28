import requests
"""
r = requests.get("https://github.com/favicon.ico")
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
print(r.content)
"""
headers = {
    'Cookies': '_zap=802255d2-da27-43f2-abeb-d0d6793cde2b;\
         d_c0="AEAaAJ5J2hGPTvo7rptSImrzUBZr2un-0qs=|1599486806";\
         _ga=GA1.2.1448227959.1599486813; _xsrf=ebdf3992-e417-4b1a-9b35-62101c63d905;\
         l_n_c=1; r_cap_id="MWEzMzFmMDk2YTYxNDNhNThiZjRjYjI2MDZmODhiMjc=|1610525287|ee1af329a6097dc4eb3ff939b5d2688050f3927d";\
         cap_id="ODNhYWE3ZGRlMzQyNDI5Yjg4N2U2ZTE2MjU0MDc0OTI=|1610525287|050327f85232fb7d76e31cd8aa391544b217aab6";\
         l_cap_id="NTQ5ZWRhM2NiYzUxNDdjZDhiMmI0ZTljYzRiOTk1OTU=|1610525287|cb18d3f9b4377f2324554117136ab0764d649ef2";\
         n_c=1; atoken=67E1EC017B5D43A5BC580CAEAA583961; atoken_expired_in=7776000;\
         client_id="NDQwNkNENkUwMEVBRTk1QUI1QjQwMDZGMTFEQzIyMTY=|1610525335|968bd340de07ec7689a3dc13f35ba48ca9d72e52";\
         Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1610092834,1610508933,1610509657,1610525379;\
         capsion_ticket="2|1:0|10:1610525378|14:capsion_ticket|44:YzAwYzc1NGE2YTg5NGU2ZWI5OGYzZGQwYTRlZjE4NTk=|9d6904ce138c7e5d72af62d4f6c8ab0518e9cf15f45abfaec85adbae413e0553";\
         SESSIONID=YQY5pbo1pKLhYWVfJzJr7uE8zhK4Ca9p4pi9ZonuzhK; JOID=V1ETBUpGc1NpdbSbU0ULDdftz3dBEy0KWwHa-2IyNBABK-fBOobWqjV9t5RUjf5VhB418uky4n5T-bPZEbKzrzs=;\
         osd=VFsVB0JFeVVrfbeRVUcDDt3rzX9CGSsIUwLQ_WA6NxoHKe_CMIDUojZ3sZZcjvRThhY2-O8w6n1Z_7HREri1rTM=; z_c0="2|1:0|10:1610525473|4:z_c0|92:Mi4xRGtMVUlnQUFBQUFBUUJvQW5rbmFFU1lBQUFCZ0FsVk5JZm5yWUFERlZydllod1NIcHNhQWpSc050Uk04ZlhSSEN3|1e64261025ca0d2b149937c8d87267be8b261f6507ab6c40f0f1fb5e537df84b";\
         tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1610525487; KLBRSID=d1f07ca9b929274b65d830a00cbd719a|1610525486|1610525189',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)
